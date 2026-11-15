https://github.com/mchestr/home-cluster/tree/bc9a0546169bb64bee4f2312243504a43cce92db/kubernetes/apps

# home-cluster app inventory at bc9a054

Generated on 2026-11-15 from the Flux Kustomizations (`kubernetes/apps/*/*/ks.yaml`) and the YAML under each Kustomization `path`, with yq.
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
| database | dragonfly | app-template | ghcr.io/dragonflydb/operator:v1.8.0@sha256:953b5aab07963e2ccc4c61ab6e6bc0d27bfdda6301d81dc2b807396dfef6e6a3 |  |  |  |  |
| default | atuin | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/atuinsh/atuin:18.24.8@sha256:2bc3a558b236283cd64ce64cf9aa463c24e34f97fc36a4b1a5b2b1853a5dcb49 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | authelia | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/authelia/authelia:4.39.28 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, lldap, onepassword-store, smtp-relay | gateway-only ingress + kube-apiserver entity |
| default | esphome | app-template | ghcr.io/esphome/esphome:2026.10.2@sha256:4a918585150e95e7675be84a347384ff308fde1bd32d0e4472666e1252cc0e8f | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | frigate | app-template | ghcr.io/blakeblackshear/frigate:0.18.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | govee2mqtt | app-template | ghcr.io/wez/govee2mqtt:latest@sha256:d5427fa1524e3e6f87c59e5cbc59e782036a2b5274e4f96cfb581d844aa2b6dc | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | home-assistant | app-template | docker.io/library/busybox:1.38, ghcr.io/home-operations/home-assistant:2026.11.1 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | homepage | app-template | ghcr.io/gethomepage/homepage:v2.8.0 | envoy-internal |  | onepassword-store |  |
| default | immich | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/immich-app/immich-server:v3.3.6 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store | gateway-only ingress + kube-apiserver entity |
| default | lldap | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/lldap/lldap:v0.6.3-alpine-rootless@sha256:ba2c50930ea998eefd5454aa678a7977448019248b1827da87d330df0b71c284 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | matter-server | app-template | ghcr.io/home-assistant-libs/python-matter-server:8.1.0@sha256:170aa093ce91c76cde4cc390918307590f0f5558fcec93f913af3cb019e6562a | envoy-internal | volsync | home-assistant, onepassword-store, rook-ceph-cluster |  |
| default | mosquitto | app-template | public.ecr.aws/docker/library/eclipse-mosquitto:2.0.22 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| default | paperless | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/paperless-ngx/paperless-ngx:3.4.2 | envoy-internal | cnpg, dragonfly, volsync | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | radicale | app-template | tomsquest/docker-radicale:3.9.1.0 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| default | smtp-relay | app-template | ghcr.io/foxcpp/maddy:0.9.7 |  |  | onepassword-store | other policy |
| default | teslamate | app-template | ghcr.io/home-operations/postgres-init:18, teslamate/teslamate:4.4.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | thelounge | app-template | ghcr.io/thelounge/thelounge:4.5.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | zigbee2mqtt | app-template | ghcr.io/koenkk/zigbee2mqtt:2.14.3 | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | zwave-js-ui | app-template | ghcr.io/zwave-js/zwave-js-ui:11.26.2 | envoy-internal | volsync | mosquitto, onepassword-store, node-feature-discovery-rules, rook-ceph-cluster |  |
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
| media | autobrr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/autobrr/autobrr:v1.90.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | bazarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/bazarr:1.6.2@sha256:b8434a7339ebd9c2bfe4464c28db79944e0f52f47da85345fc7e0563c19f83ac | envoy-internal | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | cross-seed | app-template | ghcr.io/cross-seed/cross-seed:6.13.9@sha256:c310f84e040b82c140424f6377fa36487335261037175ef9cec3aefc92b93076 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| media | jellyseerr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/seerr-team/seerr:v3.5.2@sha256:aadee014b40e28cf9aa4928bc9d1183a6eb08f8c44d543cddc9efdcb16549be2 | envoy-external | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | kometa | app-template | docker.io/kometateam/kometa:v2.5.5@sha256:864cec57d099c71a26a5a5ce2784d34d9b53874c91269c3a12df3949eab96562 |  | volsync | onepassword-store, rook-ceph-cluster, plex, radarr, sonarr, tautulli |  |
| media | plex | app-template | ghcr.io/home-operations/plex:1.43.5.11079@sha256:06ef0fc23e9af9bbaf284c3f27972f94e703d13d6f745edeb6818fcbebf6c673 | envoy-external | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | prowlarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/prowlarr:3.0.1.5752@sha256:83cc967a3b7b754634e31773d4d58ea606714490b7e8592d41b608f7c249afe6 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | qbittorrent | app-template | ghcr.io/home-operations/qbittorrent:5.3.0@sha256:5a858e61f94cf2712391db32ed03556576c700858f3e62c4c6fcde262443ebd8 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | radarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/radarr:7.0.2.10888@sha256:69ea515df6e2a3ea1490cfa127ffaaf9597a9db84fffa2fa150a6fae98fe04cb | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | recyclarr | app-template | ghcr.io/recyclarr/recyclarr:8.8.1@sha256:3e9c41b9ec29bbf65fe846864058730d321a21f7695d8c0d9437b73e34d50ad9 |  | volsync | onepassword-store, rook-ceph-cluster, radarr, sonarr |  |
| media | sabnzbd | app-template | ghcr.io/home-operations/sabnzbd:5.1.3@sha256:c89b0322721c3eba47221e5f916505e7e742684651f73c5215717340b6b5402f | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | silo | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/silo-server/silo-server:build-2210@sha256:0a76ab3481667ef2ddd06e26fb40412fabbc7006bad99bfdbb51300ba34800dd | envoy-internal | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | sonarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/sonarr:5.0.0.2941@sha256:93b0923dd12afd43247739e19dac59d74c52a15ea12e036b7ced264cffb42574 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | subs | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/mchestr/plex-manager:0.12.0@sha256:f7ccc98e01f3eb1023e4848c4697c011e6b1ec1f6da7f3e82bb4b39aa4342278 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | tautulli | app-template | ghcr.io/home-operations/tautulli:2.19.1@sha256:de490b2e01593b4efa062ebe8ceb802a2bc119d727df0e545629394ac3667eb0 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | tqm | app-template | ghcr.io/home-operations/tqm:1.20.0@sha256:c5bdff16ca1107712fd61dc6c39a276488908c702e68e427db889419af042761 |  |  |  |  |
| media | unpackerr | app-template | ghcr.io/unpackerr/unpackerr:v1.0.1 |  |  | onepassword-store |  |
| media | whisper | app-template | onerahmet/openai-whisper-asr-webservice:v1.10.0@sha256:0616c3d5fc6924e9d59aa8a7a3a944fbe8f3a5d701e5fc1fa2ce5b933dfecb73 |  |  | bazarr, rook-ceph-cluster |  |
| networking | cloudflared | app-template | docker.io/cloudflare/cloudflared:2026.11.0@sha256:b94b96edf2c9c4360f8879c8580cfaa99077f19c849ec595ca2f711b27d4f344 |  |  | onepassword-store |  |
| networking | envoy | gateway-helm |  | envoy-external, envoy-internal |  | onepassword-store |  |
| networking | external-dns-cloudflare | external-dns |  |  |  | onepassword-store |  |
| networking | external-dns-unifi | external-dns | ghcr.io/kashalls/external-dns-unifi-webhook:v0.9.0@sha256:22f4106f44a0b9ac3c97cf29bbfef93026c1164492152dc797a1d6dc86ddfbb5 |  |  | onepassword-store |  |
| networking | multus | app-template | ghcr.io/home-operations/cni-plugins:1.10.0@sha256:42eac3f9ff0daa695cdb288afb4e52d73ef62346dcd3bef126b71cd84d6cee19, ghcr.io/k8snetworkplumbingwg/multus-cni:v4.3.2@sha256:82310e48db2eddf8c2329c1199d5693dc54532c773081a319bf19290a4ce6f73 |  |  |  |  |
| networking | multus-config |  |  |  |  | multus |  |
| observability | fluent-bit | fluent-bit |  |  |  |  |  |
| observability | gatus | app-template | ghcr.io/home-operations/gatus-sidecar:0.6.1@sha256:c2b24374a8a4c5551c0122f3a7ae383ff65a0ea0bcd3b541530db84490fea2af, ghcr.io/twin/gatus:v5.38.0@sha256:085ed63da963728965d00a3c78aa6167e3bf135218485b893201758e079e8415 | envoy-external |  | onepassword-store | gateway-only ingress + kube-apiserver entity |
| observability | grafana | grafana-operator |  |  |  | onepassword-store |  |
| observability | grafana-instance |  |  | envoy-internal | cnpg | cloudnative-pg-cluster, grafana, onepassword-store, rook-ceph-cluster |  |
| observability | kromgo | app-template | ghcr.io/kashalls/kromgo:v0.10.0@sha256:965ecc92d68dc1a4a969397855367bbc70da03227a941ea607b73bb7e0b78fd6 | envoy-external |  |  | gateway-only ingress + kube-apiserver entity |
| observability | kube-prometheus-stack | kube-prometheus-stack |  | envoy-internal |  | onepassword-store, rook-ceph-cluster | kube-apiserver entity |
| observability | silence-operator | silence-operator |  |  |  | silence-operator-crds |  |
| observability | silence-operator-crds | silence-operator-crds |  |  |  |  |  |
| observability | unpoller | app-template | ghcr.io/unpoller/unpoller:v5.9.5@sha256:092e6ef8c388fcc9d8b52e8a5e04e6662f85b25ea3a0d4bb7d0d13e43a9b9c8d |  |  | onepassword-store |  |
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

Total Kustomizations: 96
