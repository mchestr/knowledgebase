---
title: OCI chart pull denied (403)
type: issue
aliases: [charts-mirror 403, OCIRepository DENIED, requested access to the resource is denied]
systems: [flux, github-actions, charts-mirror]
created: 2026-10-28
updated: 2026-10-28
tags: [home-cluster, flux, ci, helm]
---

# OCI chart pull denied (403)

## Symptom

- An `OCIRepository` is `Ready=False` with `DENIED: requested access to the resource is denied` ([[incident-2026-10-28-fluent-bit-chart-mirror-403]]).
- CI fails to render the HelmRelease that uses it, with `response status code 403: denied`. On pull requests the image extract and diff jobs fail. On `renovate/**` pushes the test job fails. These jobs fail on every branch, not only on the branch that changed the app.
- The HelmRelease can stay `Ready` for some time, because helm-controller keeps the last release.

## Cause

The registry no longer lets anonymous clients pull the chart. Known cause:

| Cause | Sign |
| --- | --- |
| home-operations/charts-mirror deprecated the chart, and later the package stopped allowing anonymous pulls | A commit "feat: deprecate <chart>" in charts-mirror, and the URL starts with `oci://ghcr.io/home-operations/charts-mirror/` |

## Check

1. List the OCI sources that are not ready:

   ```bash
   flux get sources oci -A --status-selector ready=false
   ```

2. Read the message of the failed source. Look for `DENIED` or `403`.
3. Get the chart path from `spec.url`, without `oci://ghcr.io/`. Test anonymous access to it:

   ```bash
   curl -s -o /dev/null -w "%{http_code}\n" \
     "https://ghcr.io/token?scope=repository:<path>:pull&service=ghcr.io"
   ```

   HTTP 403 means denied. HTTP 200 means the registry allows the pull, so the cause is somewhere else.
4. For a charts-mirror chart, look for a deprecation commit:

   ```bash
   gh search commits "deprecate <chart>" --repo home-operations/charts-mirror
   ```

5. Find all the other charts that use the same registry path:

   ```bash
   grep -rn "charts-mirror" kubernetes/ bootstrap/
   ```

## Fix

1. Find the upstream OCI chart. The deprecation commit shows the old `chartRegistry`. The upstream project often publishes OCI on ghcr.io, for example `ghcr.io/fluent/helm-charts/fluent-bit`.
2. Make sure that the same tag exists upstream:

   ```bash
   repo=<owner>/<path>
   token=$(curl -s "https://ghcr.io/token?scope=repository:${repo}:pull&service=ghcr.io" | jq -r .token)
   curl -s -H "Authorization: Bearer ${token}" "https://ghcr.io/v2/${repo}/tags/list" | jq '.tags'
   ```

3. Change only `spec.url` in the app's `ocirepository.yaml`. Keep `spec.ref.tag`, so that the chart version does not change.
4. Open a pull request. Expect the CI jobs that also render the default branch to fail until the merge. The test job that renders only the pull request must pass.
5. After the merge, make sure that the source is ready and the release upgraded:

   ```bash
   flux get sources oci -n <namespace> <name>
   flux get hr -n <namespace> <name>
   ```

   The chart digest changes, so helm-controller upgrades the release with the same chart version.

## Prevention

- Do not add new charts from home-operations/charts-mirror when the upstream project publishes OCI.
- When charts-mirror deprecates a chart that the [[home-cluster]] uses, move to the upstream chart before the package stops allowing pulls.

## Related

- [[flux]]
- [[renovate]]
- [[victorialogs]]
