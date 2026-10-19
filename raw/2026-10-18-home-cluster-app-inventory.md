https://github.com/mchestr/home-cluster/tree/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps

# home-cluster app inventory at e36a8c8

Generated on 2026-10-18 from the Flux Kustomizations (`kubernetes/apps/*/*/ks.yaml`) and the YAML under each Kustomization `path`, with yq.
Gateway: `parentRefs` that name an `envoy-*` gateway. Main image: first two images in HelmRelease values.
NetworkPolicy: "gateway-only ingress" if the app path selects `gateway.envoyproxy.io/owning-gateway-name`; "kube-apiserver entity" if it admits the `kube-apiserver` Cilium entity; "other policy" for any other NetworkPolicy. Policies added through `components` (for example dragonfly) are not counted.

| Namespace | App | Chart | Main image | Gateway | Components | dependsOn | NetworkPolicy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| actions-runner-system | actions-runner-controller | gha-runner-scale-set-controller |  |  |  |  |  |
| actions-runner-system | actions-runner-controller-runners | gha-runner-scale-set |  |  |  | actions-runner-controller, onepassword-store, openebs |  |
| ai | claude-code | app-template | docker.io/library/busybox:1.38, docker.io/library/node:24-bookworm |  |  | onepassword-store, rook-ceph-cluster | other policy |
| ai | litellm |  |  | envoy-internal | dragonfly | litellm-operator, dragonfly, onepassword-store |  |
| ai | litellm-operator | litellm-operator |  |  |  |  |  |
| ai | memini | memini |  | envoy-internal | volsync | rook-ceph-cluster, onepassword-store, volsync, text-embeddings |  |
| ai | text-embeddings | app-template | ghcr.io/huggingface/text-embeddings-inference:cpu-1.8@sha256:8de25e75ce39617f17f2f6c77d60a4f75b65e779ed5005420eb1400072a15c1c |  |  |  |  |
| cert-manager | cert-manager | cert-manager |  |  |  |  |  |
| cert-manager | cert-manager-issuers |  |  |  |  | cert-manager, onepassword-store |  |
| database | cloudnative-pg | cloudnative-pg |  |  |  | onepassword-store |  |
| database | cloudnative-pg-cluster |  |  |  |  | cloudnative-pg, openebs |  |
| database | cloudnative-pg-roles |  |  |  |  | onepassword-store |  |
| database | dragonfly | app-template | ghcr.io/dragonflydb/operator:v1.7.1@sha256:bc0067369a456810d00715d7292da32b82f6df491fd51d6c57f2b2b3193ab490 |  |  |  |  |
| default | atuin | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/atuinsh/atuin:18.24.1@sha256:b9a8369b4016dddcd90d23906f1d63dd883f459c6aaecec3be87cf481e8ac88d | envoy-internal | cnpg | cloudnative-pg-cluster |  |
| default | authelia | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/authelia/authelia:4.39.28 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, lldap, onepassword-store, smtp-relay |  |
| default | esphome | app-template | ghcr.io/esphome/esphome:2026.9.1@sha256:776a845d508909bf426d2ee7bdd81796361ebe6a7f091807ce1d6d0b48985413 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | frigate | app-template | ghcr.io/blakeblackshear/frigate:0.18.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | govee2mqtt | app-template | ghcr.io/wez/govee2mqtt:latest@sha256:d5427fa1524e3e6f87c59e5cbc59e782036a2b5274e4f96cfb581d844aa2b6dc | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | home-assistant | app-template | docker.io/library/busybox:1.38, ghcr.io/home-operations/home-assistant:2026.10.2 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | homepage | app-template | ghcr.io/gethomepage/homepage:v2.6.0 | envoy-internal |  | onepassword-store |  |
| default | immich | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/immich-app/immich-server:v3.3.3 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store | gateway-only ingress + kube-apiserver entity |
| default | lldap | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/lldap/lldap:v0.6.3-alpine-rootless@sha256:ba2c50930ea998eefd5454aa678a7977448019248b1827da87d330df0b71c284 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | matter-server | app-template | ghcr.io/home-assistant-libs/python-matter-server:8.1.0@sha256:170aa093ce91c76cde4cc390918307590f0f5558fcec93f913af3cb019e6562a | envoy-internal | volsync | home-assistant, onepassword-store, rook-ceph-cluster |  |
| default | mosquitto | app-template | public.ecr.aws/docker/library/eclipse-mosquitto:2.0.22 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| default | paperless | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/paperless-ngx/paperless-ngx:3.3.2 | envoy-internal | cnpg, dragonfly, volsync | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | radicale | app-template | tomsquest/docker-radicale:3.8.3.0 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| default | smtp-relay | app-template | ghcr.io/foxcpp/maddy:0.9.6 |  |  | onepassword-store | other policy |
| default | teslamate | app-template | ghcr.io/home-operations/postgres-init:18, teslamate/teslamate:4.3.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | thelounge | app-template | ghcr.io/thelounge/thelounge:4.5.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | windmill | windmill |  | envoy-external | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | zigbee2mqtt | app-template | ghcr.io/koenkk/zigbee2mqtt:2.14.2 | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | zwave-js-ui | app-template | ghcr.io/zwave-js/zwave-js-ui:11.24.3 | envoy-internal | volsync | mosquitto, onepassword-store, node-feature-discovery-rules, rook-ceph-cluster |  |
| external-secrets | external-secrets | external-secrets |  |  |  |  |  |
| external-secrets | onepassword | app-template | docker.io/1password/connect-api:1.8.3@sha256:656e4b10df83ca258d8a75b2a051f7c06dd608212f8ae5ba4722e3fe164099d3, docker.io/1password/connect-sync:1.8.3@sha256:a760350c941a3e7c98dd66394e9fc3c7e68b6a0a2246a837c74084e534f75f6b |  |  | external-secrets |  |
| external-secrets | onepassword-store |  |  |  |  | onepassword |  |
| flux-system | flux-instance | flux-instance |  | envoy-external |  | onepassword-store, flux-operator |  |
| flux-system | flux-operator | flux-operator |  | envoy-internal |  |  |  |
| kube-system | cilium | cilium |  | envoy-internal |  |  |  |
| kube-system | cilium-config |  |  |  |  | cilium |  |
| kube-system | coredns | coredns |  |  |  | cilium |  |
| kube-system | descheduler | descheduler |  |  |  |  |  |
| kube-system | intel-device-plugin-gpu | intel-device-plugins-gpu |  |  |  | intel-device-plugin-operator |  |
| kube-system | intel-device-plugin-operator | intel-device-plugins-operator |  |  |  | node-feature-discovery |  |
| kube-system | irqbalance | app-template | ghcr.io/home-operations/irqbalance:1.9.5@sha256:0c4b233e7f3bf6753afc22082547ba7980b24e1cf7a9dabadfb149f4381232ee |  |  |  |  |
| kube-system | kubelet-csr-approver | kubelet-csr-approver |  |  |  |  |  |
| kube-system | metrics-server | metrics-server |  |  |  |  |  |
| kube-system | node-feature-discovery | node-feature-discovery |  |  |  |  |  |
| kube-system | node-feature-discovery-rules |  |  |  |  | node-feature-discovery |  |
| kube-system | reloader | reloader |  |  |  |  |  |
| kube-system | spegel | spegel |  |  |  |  |  |
| media | autobrr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/autobrr/autobrr:v1.88.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | bazarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/bazarr:1.6.2@sha256:17dc1cff22e99694ffbfb06555526cb47a66b362b4d6c982f06b557f7caae2bb | envoy-internal | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | cross-seed | app-template | ghcr.io/cross-seed/cross-seed:6.13.7@sha256:a1fed512261fd968c55cb03c51cff9c6620aa76a34b3b591afca95c890aa8225 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| media | jellyfin | app-template | docker.io/jellyfin/jellyfin:12.2@sha256:357724bf0ae27a672c7cbaa899db2d9abeb13dbd8657ccce750258a4c059d037 | envoy-internal | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | jellyplex-watched | app-template | luigi311/jellyplex-watched:8.5.3@sha256:e23a0d3dc686e4bbc9eeb655aeb96a2a1352bd2a26297ec77e06ef6f8eb2d5e1 |  |  | jellyfin, onepassword-store, plex |  |
| media | jellyseerr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/seerr-team/seerr:v3.5.0@sha256:27602401178d54f1964442287b9f23f67a3fa2252645ee8065839ea1c3f69e45 | envoy-external | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | kometa | app-template | docker.io/kometateam/kometa:v2.5.3@sha256:48c3cb318ec984213587f221e8e762c5ad2dbd0e6966efc7bba0a5868a6c5758 |  | volsync | onepassword-store, rook-ceph-cluster, plex, radarr, sonarr, tautulli |  |
| media | plex | app-template | ghcr.io/home-operations/plex:1.43.4.10903@sha256:fdc6fe82bc7d8acd08fc0aa581fcb76722803ba5905e2537135a697347dd6149 | envoy-external | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | prowlarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/prowlarr:2.6.5.5623@sha256:6152751c3ea2e7751564f5952173d5e83eed0e09f3fabd2cb6bdb58690c39e2f | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | qbittorrent | app-template | ghcr.io/home-operations/qbittorrent:5.2.4@sha256:9307627e03981d5473aa31175ea76ed56ea3752333ca49d601b6af45e281e7ba | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | radarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/radarr:6.4.4.10685@sha256:be53998a2d39cfa3c3315b70c7509a6a1f2a10c3aee9337653efc9f4c970430e | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | recyclarr | app-template | ghcr.io/recyclarr/recyclarr:8.8.0@sha256:b1fbb929ba718fdbdac2c1fc25b32b0ae916d7a5a0892c2068c9bfae6f1a9209 |  | volsync | onepassword-store, rook-ceph-cluster, radarr, sonarr |  |
| media | sabnzbd | app-template | ghcr.io/home-operations/sabnzbd:5.1.3@sha256:b1795982db498ed5691a7b1231f0fac7eed2a1d53e9c81b8e834d02695e76104 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | sonarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/sonarr:5.0.0.2668@sha256:64fc190929b50091a8d6c3d6b5f4a3df7d3b8f98d076735f5cb223f7d77b0cc3 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | subs | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/mchestr/plex-manager:0.1.0@sha256:66821cd15afe8b8972e7f6c5a520c67812e961980ff00857eb19ff663669ebc7 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | tautulli | app-template | ghcr.io/home-operations/tautulli:2.18.2@sha256:5d55eb06f2b77eb09001b2f884b0b3a9ed3adf8416c6209c563796e18eaa43a4 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | tqm | app-template | ghcr.io/home-operations/tqm:1.20.0@sha256:c5bdff16ca1107712fd61dc6c39a276488908c702e68e427db889419af042761 |  |  |  |  |
| media | unpackerr | app-template | ghcr.io/unpackerr/unpackerr:v0.16.1 |  |  | onepassword-store |  |
| media | whisper | app-template | onerahmet/openai-whisper-asr-webservice:v1.10.0@sha256:0616c3d5fc6924e9d59aa8a7a3a944fbe8f3a5d701e5fc1fa2ce5b933dfecb73 |  |  | bazarr, rook-ceph-cluster |  |
| networking | cloudflared | app-template | docker.io/cloudflare/cloudflared:2026.10.1@sha256:a15a3b50b8dabd57ac2090e9484c0247dba9dfa1f0df4d298d4317f9d69eb2d5 |  |  | onepassword-store |  |
| networking | envoy | gateway-helm |  | envoy-external, envoy-internal |  | onepassword-store |  |
| networking | external-dns-cloudflare | external-dns |  |  |  | onepassword-store |  |
| networking | external-dns-unifi | external-dns | ghcr.io/kashalls/external-dns-unifi-webhook:v0.9.0@sha256:22f4106f44a0b9ac3c97cf29bbfef93026c1164492152dc797a1d6dc86ddfbb5 |  |  | onepassword-store |  |
| networking | multus | app-template | ghcr.io/home-operations/cni-plugins:1.9.1@sha256:e17cc64a81579a163646425d25d2e48065cfb0dc449d2de447b1fd29e9c2ca0f, ghcr.io/k8snetworkplumbingwg/multus-cni:v4.3.1@sha256:9dc8ca645a78552ed4151cf67c2998d18f260f172cc541580d8acce2ee3495c2 |  |  |  |  |
| networking | multus-config |  |  |  |  | multus |  |
| observability | fluent-bit | fluent-bit |  |  |  |  |  |
| observability | gatus | app-template | ghcr.io/home-operations/gatus-sidecar:0.5.3@sha256:b52ae9161639c7453308096aa8f5095d540196d097f5e3c681465737f22e8e76, ghcr.io/twin/gatus:v5.37.0@sha256:094eb186e55235db367e90e9d56140e5897b7044c41de23cde4cc18e6da1242e | envoy-external |  | onepassword-store |  |
| observability | grafana | grafana-operator |  |  |  |  |  |
| observability | grafana-instance |  |  | envoy-internal | cnpg | cloudnative-pg-cluster, grafana, rook-ceph-cluster |  |
| observability | kromgo | app-template | ghcr.io/kashalls/kromgo:v0.10.0@sha256:965ecc92d68dc1a4a969397855367bbc70da03227a941ea607b73bb7e0b78fd6 | envoy-external |  |  |  |
| observability | kube-prometheus-stack | kube-prometheus-stack |  | envoy-internal |  | onepassword-store, rook-ceph-cluster | kube-apiserver entity |
| observability | silence-operator | silence-operator |  |  |  | silence-operator-crds |  |
| observability | silence-operator-crds | silence-operator-crds |  |  |  |  |  |
| observability | unpoller | app-template | ghcr.io/unpoller/unpoller:v5.6.2@sha256:4ba1eab360adb75231ab05b7ee8adf252e6cf4c5d67ba39536492efd1e4605bd |  |  | onepassword-store |  |
| observability | victoria-logs | victoria-logs-single |  | envoy-internal |  | victoria-metrics-operator |  |
| observability | victoria-metrics-operator | victoria-metrics-operator |  |  |  |  |  |
| openebs-system | openebs | openebs |  |  |  |  |  |
| renovate | renovate-operator | renovate-operator |  | envoy-internal |  |  |  |
| renovate | renovate-operator-jobs |  |  |  |  | renovate-operator, onepassword-store |  |
| rook-ceph | rook-ceph | rook-ceph |  |  |  | onepassword-store |  |
| rook-ceph | rook-ceph-cluster | rook-ceph-cluster |  | envoy-internal |  | rook-ceph, rook-ceph-csi-drivers |  |
| rook-ceph | rook-ceph-csi-drivers | ceph-csi-drivers |  |  |  | rook-ceph |  |
| system-upgrade | etcd-defrag | app-template | ghcr.io/siderolabs/talosctl:v1.14.3@sha256:4d021d8951bc880667fa09e86c4c91ce69426d03f121d766c91736257d0edf38 |  |  |  |  |
| system-upgrade | tuppr | tuppr |  |  |  |  |  |
| system-upgrade | tuppr-upgrades |  |  |  |  | tuppr |  |
| volsync-system | snapshot-controller | snapshot-controller |  |  |  |  |  |
| volsync-system | volsync | volsync |  |  |  | snapshot-controller |  |
| waitlist | waitlist | app-template | ghcr.io/mchestr/waitlist-control:1.0.0@sha256:42c262ee983d32e1db0b49ff2639975b97dd3d4d1d1c78e7d5c4232353c1a159 | envoy-external | cnpg | onepassword-store, cloudnative-pg-cluster | gateway-only ingress + kube-apiserver entity |

Total Kustomizations: 98
