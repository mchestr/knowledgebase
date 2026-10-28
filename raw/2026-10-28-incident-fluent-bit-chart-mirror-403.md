# Incident: the Fluent Bit chart mirror denies pulls

Date: 2026-10-28
Systems: home-cluster, Fluent Bit (observability/fluent-bit, chart 0.55.0), Flux source-controller, GitHub Actions CI (flux-local, and flate in the open migration PR), home-operations/charts-mirror

## Symptom

- Every home-cluster CI run failed. On pull requests, both "Image Pull - Extract Images" jobs failed. On renovate/** pushes, "Flux Local Test" failed. All of them failed on the HelmRelease `observability/fluent-bit`.
- In the cluster, `OCIRepository observability/fluent-bit` was `Ready=False`.
- The migration PR from flux-local to flate (home-cluster PR #6313) failed its "Flate Test" job: 242 passed, 2 failed. The two failures were the same OCIRepository and HelmRelease.

## Evidence

- flux-local: `Error: failed to perform "FetchReference" on source: GET "https://ghcr.io/v2/home-operations/charts-mirror/fluent-bit/manifests/0.55.0": GET "https://ghcr.io/token?scope=repository%3Ahome-operations%2Fcharts-mirror%2Ffluent-bit%3Apull&service=ghcr.io": response status code 403: denied: requested access to the resource is denied`
- flate: `OCIRepository observability/fluent-bit resolve 0.55.0: HEAD "https://ghcr.io/v2/home-operations/charts-mirror/fluent-bit/manifests/0.55.0": ... response status code 403: denied: requested access to the resource is denied`
- source-controller, `OCIRepository observability/fluent-bit` Ready message: `failed to determine artifact digest: GET https://ghcr.io/token?scope=repository%3Ahome-operations%2Fcharts-mirror%2Ffluent-bit%3Apull&service=ghcr.io: DENIED: requested access to the resource is denied`
- An anonymous token request for `repository:home-operations/charts-mirror/fluent-bit:pull` returned HTTP 403. The same request for another chart in the mirror returned HTTP 200.

## Cause

home-operations/charts-mirror copies Helm charts from HTTP chart repositories to OCI on ghcr.io. It stopped copying fluent-bit on 2026-01-22 (commit e8f3b5cf, "feat: deprecate fluent-bit", PR #393). That commit removed `apps/fluent-bit/metadata.yaml`, which pointed at `https://fluent.github.io/helm-charts`. Later the ghcr.io package `charts-mirror/fluent-bit` stopped allowing anonymous pulls. The date of that change is unknown.

home-cluster still pointed `kubernetes/apps/observability/fluent-bit/app/ocirepository.yaml` at `oci://ghcr.io/home-operations/charts-mirror/fluent-bit`, tag 0.55.0. fluent-bit was the only chart in the repository that used charts-mirror.

## Fix

The fluent project publishes the same chart as OCI at `oci://ghcr.io/fluent/helm-charts/fluent-bit`. Tag 0.55.0 exists there, and later tags too (0.58.3 on 2026-10-28).

home-cluster PR #6314 changed only the `url` of the OCIRepository. The tag stayed 0.55.0.

- On the PR, "Flux Local Test" passed. "Flux Diff (helmrelease)" and "Image Pull - Extract Images (default)" failed, because they also render the default branch, which still had the old URL. They passed after the merge.
- After the merge, the OCIRepository became `Ready=True` with revision `0.55.0@sha256:4da7b482491d64387c63000ada116abe2a0974c2d7dc7705931420b90b3ead09`.
- The chart digest changed, so helm-controller upgraded the release to v17 with chart fluent-bit 0.55.0. The upgrade succeeded.
- PR #6313 then passed "Flate Test".

## Lessons

- A charts-mirror "feat: deprecate <chart>" commit is an early warning. The package can later stop allowing pulls, and then the OCIRepository fails.
- Test anonymous pull access with a token request: `curl -s -o /dev/null -w "%{http_code}\n" "https://ghcr.io/token?scope=repository:<path>:pull&service=ghcr.io"`. HTTP 403 means denied.
- A fix PR for a source that the default branch cannot render fails the CI jobs that render the default branch. The test job that renders only the PR shows whether the fix works.
- Find the upstream OCI chart and check that the same tag exists before you change the URL. Then the fix changes only the source, not the version.
