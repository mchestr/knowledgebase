https://github.com/mchestr/home-cluster/tree/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/kubernetes/apps

# home-cluster app inventory at 2d78212

Generated on 2026-10-28 from the Flux Kustomizations (`kubernetes/apps/*/*/ks.yaml`) and the YAML under each Kustomization `path`, with yq.
Gateway: `parentRefs` that name an `envoy-*` gateway. Main image: first two images in HelmRelease values.
NetworkPolicy: "gateway-only ingress" if the app path selects `gateway.envoyproxy.io/owning-gateway-name`; "kube-apiserver entity" if it admits the `kube-apiserver` Cilium entity; "other policy" for any other NetworkPolicy. Policies added through `components` (for example dragonfly) are not counted.

| Namespace | App | Chart | Main image | Gateway | Components | dependsOn | NetworkPolicy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| actions-runner-system | actions-runner-controller | gha-runner-scale-set-controller |  |  |  |  |  |
| actions-runner-system | actions-runner-controller-runners | gha-runner-scale-set |  |  |  | actions-runner-controller, onepassword-store, openebs |  |
| ai | claude-code | app-template | docker.io/library/busybox:1.38, docker.io/library/node:26-bookworm |  |  | onepassword-store, rook-ceph-cluster | other policy |
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
| default | atuin | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/atuinsh/atuin:18.24.2@sha256:d739b1f19ffee44f05c681cd3f9262d90e2da0ff51b15f23661a8d29f2d3f3c2 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | authelia | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/authelia/authelia:4.39.28 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, lldap, onepassword-store, smtp-relay |  |
| default | esphome | app-template | ghcr.io/esphome/esphome:2026.10.1@sha256:eab8cd6b4f51077c3883af4cedc058280ddc34a94f3b2ffee23e9d2cd5f1db64 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | frigate | app-template | ghcr.io/blakeblackshear/frigate:0.18.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | govee2mqtt | app-template | ghcr.io/wez/govee2mqtt:latest@sha256:d5427fa1524e3e6f87c59e5cbc59e782036a2b5274e4f96cfb581d844aa2b6dc | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | home-assistant | app-template | docker.io/library/busybox:1.38, ghcr.io/home-operations/home-assistant:2026.10.4 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | homepage | app-template | ghcr.io/gethomepage/homepage:v2.7.0 | envoy-internal |  | onepassword-store |  |
| default | immich | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/immich-app/immich-server:v3.3.5 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store | gateway-only ingress + kube-apiserver entity |
| default | lldap | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/lldap/lldap:v0.6.3-alpine-rootless@sha256:ba2c50930ea998eefd5454aa678a7977448019248b1827da87d330df0b71c284 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | matter-server | app-template | ghcr.io/home-assistant-libs/python-matter-server:8.1.0@sha256:170aa093ce91c76cde4cc390918307590f0f5558fcec93f913af3cb019e6562a | envoy-internal | volsync | home-assistant, onepassword-store, rook-ceph-cluster |  |
| default | mosquitto | app-template | public.ecr.aws/docker/library/eclipse-mosquitto:2.0.22 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| default | paperless | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/paperless-ngx/paperless-ngx:3.3.4 | envoy-internal | cnpg, dragonfly, volsync | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | radicale | app-template | tomsquest/docker-radicale:3.9.0.0 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| default | smtp-relay | app-template | ghcr.io/foxcpp/maddy:0.9.6 |  |  | onepassword-store | other policy |
| default | teslamate | app-template | ghcr.io/home-operations/postgres-init:18, teslamate/teslamate:4.4.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | thelounge | app-template | ghcr.io/thelounge/thelounge:4.5.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | zigbee2mqtt | app-template | ghcr.io/koenkk/zigbee2mqtt:2.14.2 | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | zwave-js-ui | app-template | ghcr.io/zwave-js/zwave-js-ui:11.25.2 | envoy-internal | volsync | mosquitto, onepassword-store, node-feature-discovery-rules, rook-ceph-cluster |  |
| external-secrets | external-secrets | external-secrets |  |  |  |  |  |
| external-secrets | onepassword | app-template | ghcr.io/1password/connect-api:1.8.4@sha256:37cf4d505f5c7bb08fa9290a2c44295646cbbaac960452667da9c499a78c3cc9, ghcr.io/1password/connect-sync:1.8.4@sha256:739688254d7a5ae757860e4165e925eb30028c71496299518c84d0361245d9bc |  |  | external-secrets |  |
| external-secrets | onepassword-store |  |  |  |  | onepassword |  |
| flux-system | flux-instance | flux-instance |  | envoy-external |  | onepassword-store, flux-operator |  |
| flux-system | flux-operator | flux-operator |  | envoy-internal |  |  |  |
| kube-system | cilium | cilium |  | envoy-internal |  |  |  |
| kube-system | cilium-config |  |  |  |  | cilium |  |
| kube-system | coredns | coredns |  |  |  | cilium |  |
| kube-system | descheduler | descheduler |  |  |  |  |  |
| kube-system | intel-device-plugin-gpu | intel-device-plugins-gpu |  |  |  | intel-device-plugin-operator |  |
| kube-system | intel-device-plugin-operator | intel-device-plugins-operator |  |  |  | node-feature-discovery |  |
| kube-system | irqbalance | app-template | ghcr.io/home-operations/irqbalance:1.9.5@sha256:c83a571c3759947288b98a60ca65ce12ec65a54622250d61cf0790841dc0d956 |  |  |  |  |
| kube-system | kubelet-csr-approver | kubelet-csr-approver |  |  |  |  |  |
| kube-system | metrics-server | metrics-server |  |  |  |  |  |
| kube-system | node-feature-discovery | node-feature-discovery |  |  |  |  |  |
| kube-system | node-feature-discovery-rules |  |  |  |  | node-feature-discovery |  |
| kube-system | reloader | reloader |  |  |  |  |  |
| kube-system | spegel | spegel |  |  |  |  |  |
| media | autobrr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/autobrr/autobrr:v1.89.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | bazarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/bazarr:1.6.2@sha256:b8434a7339ebd9c2bfe4464c28db79944e0f52f47da85345fc7e0563c19f83ac | envoy-internal | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | cross-seed | app-template | ghcr.io/cross-seed/cross-seed:6.13.9@sha256:9279fa3b4c6f09915614ec819c6dc97e1e844d863b35c009ababd54bad0489d5 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| media | jellyfin | app-template | docker.io/jellyfin/jellyfin:12.4@sha256:fea863d0cd9ec445985d9c75fc6ed64e38a1d2766cf0c250a33d553f4fc1b771 | envoy-internal | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | jellyplex-watched | app-template | luigi311/jellyplex-watched:8.5.3@sha256:e23a0d3dc686e4bbc9eeb655aeb96a2a1352bd2a26297ec77e06ef6f8eb2d5e1 |  |  | jellyfin, onepassword-store, plex |  |
| media | jellyseerr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/seerr-team/seerr:v3.5.1@sha256:d8fab675b55ad293ded98fd71efcfd46054cbad9746534ae1cc4794a88c0b3be | envoy-external | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | kometa | app-template | docker.io/kometateam/kometa:v2.5.3@sha256:48c3cb318ec984213587f221e8e762c5ad2dbd0e6966efc7bba0a5868a6c5758 |  | volsync | onepassword-store, rook-ceph-cluster, plex, radarr, sonarr, tautulli |  |
| media | plex | app-template | ghcr.io/home-operations/plex:1.43.5.11079@sha256:06ef0fc23e9af9bbaf284c3f27972f94e703d13d6f745edeb6818fcbebf6c673 | envoy-external | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | prowlarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/prowlarr:2.7.0.5723@sha256:fcf7498692f97698ea8b8f7078a0f81120a16e7354e4c232b5e3810e3e783dff | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | qbittorrent | app-template | ghcr.io/home-operations/qbittorrent:5.3.0@sha256:5a858e61f94cf2712391db32ed03556576c700858f3e62c4c6fcde262443ebd8 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | radarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/radarr:7.0.0.10815@sha256:c044b4df8e7b2546ef389481626a56fabe291575ff2d65481b1555432d6161ff | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | recyclarr | app-template | ghcr.io/recyclarr/recyclarr:8.8.1@sha256:3e9c41b9ec29bbf65fe846864058730d321a21f7695d8c0d9437b73e34d50ad9 |  | volsync | onepassword-store, rook-ceph-cluster, radarr, sonarr |  |
| media | sabnzbd | app-template | ghcr.io/home-operations/sabnzbd:5.1.3@sha256:c89b0322721c3eba47221e5f916505e7e742684651f73c5215717340b6b5402f | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | sonarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/sonarr:5.0.0.2838@sha256:5d4f89a36a06fe44039e7533e743b4c7bf0e0d82868c86ea8ed8178abd1cbe4b | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | subs | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/mchestr/plex-manager:0.6.0@sha256:642053068bbc6b20c9dfff2a2306b763d264e4ad9f48992ee92005ce12e68612 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | tautulli | app-template | ghcr.io/home-operations/tautulli:2.18.2@sha256:d7ea1a79cf8cc2603890287d7c0e5bc277e4909c1df93f48f000833d2771eca0 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | tqm | app-template | ghcr.io/home-operations/tqm:1.20.0@sha256:c5bdff16ca1107712fd61dc6c39a276488908c702e68e427db889419af042761 |  |  |  |  |
| media | unpackerr | app-template | ghcr.io/unpackerr/unpackerr:v1.0.0 |  |  | onepassword-store |  |
| media | whisper | app-template | onerahmet/openai-whisper-asr-webservice:v1.10.0@sha256:0616c3d5fc6924e9d59aa8a7a3a944fbe8f3a5d701e5fc1fa2ce5b933dfecb73 |  |  | bazarr, rook-ceph-cluster |  |
| networking | cloudflared | app-template | docker.io/cloudflare/cloudflared:2026.10.5@sha256:1b1d34d0a9c0bfca9de72db8460d328db3f19edd2b96169114e3e893a97bbe53 |  |  | onepassword-store |  |
| networking | envoy | gateway-helm |  | envoy-external, envoy-internal |  | onepassword-store |  |
| networking | external-dns-cloudflare | external-dns |  |  |  | onepassword-store |  |
| networking | external-dns-unifi | external-dns | ghcr.io/kashalls/external-dns-unifi-webhook:v0.9.0@sha256:22f4106f44a0b9ac3c97cf29bbfef93026c1164492152dc797a1d6dc86ddfbb5 |  |  | onepassword-store |  |
| networking | multus | app-template | ghcr.io/home-operations/cni-plugins:1.9.1@sha256:9215eb4c46b0b12cbc80a8adf8945e57370df2f9e02721ae58a3b4dbdd433382, ghcr.io/k8snetworkplumbingwg/multus-cni:v4.3.1@sha256:9dc8ca645a78552ed4151cf67c2998d18f260f172cc541580d8acce2ee3495c2 |  |  |  |  |
| networking | multus-config |  |  |  |  | multus |  |
| observability | fluent-bit | fluent-bit |  |  |  |  |  |
| observability | gatus | app-template | ghcr.io/home-operations/gatus-sidecar:0.6.0@sha256:1d3e6b0c50b9addcbbc68b67ab63b10718afcb3a47909f6644a1ee844dd9e6c2, ghcr.io/twin/gatus:v5.38.0@sha256:085ed63da963728965d00a3c78aa6167e3bf135218485b893201758e079e8415 | envoy-external |  | onepassword-store |  |
| observability | grafana | grafana-operator |  |  |  | onepassword-store |  |
| observability | grafana-instance |  |  | envoy-internal | cnpg | cloudnative-pg-cluster, grafana, onepassword-store, rook-ceph-cluster |  |
| observability | kromgo | app-template | ghcr.io/kashalls/kromgo:v0.10.0@sha256:965ecc92d68dc1a4a969397855367bbc70da03227a941ea607b73bb7e0b78fd6 | envoy-external |  |  |  |
| observability | kube-prometheus-stack | kube-prometheus-stack |  | envoy-internal |  | onepassword-store, rook-ceph-cluster | kube-apiserver entity |
| observability | silence-operator | silence-operator |  |  |  | silence-operator-crds |  |
| observability | silence-operator-crds | silence-operator-crds |  |  |  |  |  |
| observability | unpoller | app-template | ghcr.io/unpoller/unpoller:v5.8.3@sha256:6a474f5202d40864affe6be9882492061331d77d474593bb1cd4a8c737dc834f |  |  | onepassword-store |  |
| observability | victoria-logs | victoria-logs-single |  | envoy-internal |  | rook-ceph-cluster, victoria-metrics-operator |  |
| observability | victoria-metrics-operator | victoria-metrics-operator |  |  |  |  |  |
| openebs-system | openebs | openebs |  |  |  |  |  |
| renovate | renovate-operator | renovate-operator |  | envoy-internal |  |  |  |
| renovate | renovate-operator-jobs |  |  |  |  | renovate-operator, onepassword-store |  |
| rook-ceph | rook-ceph | rook-ceph |  |  |  | onepassword-store |  |
| rook-ceph | rook-ceph-cluster | rook-ceph-cluster |  | envoy-internal |  | rook-ceph, rook-ceph-csi-drivers |  |
| rook-ceph | rook-ceph-csi-drivers | ceph-csi-drivers |  |  |  | rook-ceph |  |
| system-upgrade | etcd-defrag | app-template | ghcr.io/siderolabs/talosctl:v1.14.5@sha256:0b852e35c1f513ee5eacc22183d6193486012420569fde39fcd5260c51938443 |  |  |  |  |
| system-upgrade | tuppr | tuppr |  |  |  |  |  |
| system-upgrade | tuppr-upgrades |  |  |  |  | tuppr |  |
| volsync-system | snapshot-controller | snapshot-controller |  |  |  |  |  |
| volsync-system | volsync | volsync |  |  |  | snapshot-controller |  |
| waitlist | waitlist | app-template | ghcr.io/mchestr/waitlist-control:1.0.0@sha256:42c262ee983d32e1db0b49ff2639975b97dd3d4d1d1c78e7d5c4232353c1a159 | envoy-external | cnpg | onepassword-store, cloudnative-pg-cluster | gateway-only ingress + kube-apiserver entity |

Total Kustomizations: 97
