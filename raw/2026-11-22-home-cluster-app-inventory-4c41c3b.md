https://github.com/mchestr/home-cluster/tree/4c41c3be0221cc0272473cfdd00c4a5d520e91b5/kubernetes/apps

# home-cluster app inventory at 4c41c3b

Generated on 2026-11-22 from the Flux Kustomizations (`kubernetes/apps/*/*/ks.yaml`) and the YAML under each Kustomization `path`, with yq.
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
| default | atuin | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/atuinsh/atuin:18.25.1@sha256:8049083e74727566e314ca5de07f4d9db6f7baf357035b3adb23cbe23bcc2926 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | authelia | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/authelia/authelia:4.39.28 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, lldap, onepassword-store, smtp-relay | gateway-only ingress + kube-apiserver entity |
| default | esphome | app-template | ghcr.io/esphome/esphome:2026.11.0@sha256:6351ae811202064bb3eb49dde982609b47acd523103a66d7b9c5c1431beea055 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | frigate | app-template | ghcr.io/blakeblackshear/frigate:0.18.3 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | govee2mqtt | app-template | ghcr.io/wez/govee2mqtt:latest@sha256:d5427fa1524e3e6f87c59e5cbc59e782036a2b5274e4f96cfb581d844aa2b6dc | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | home-assistant | app-template | docker.io/library/busybox:1.38, ghcr.io/home-operations/home-assistant:2026.11.2 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | homepage | app-template | ghcr.io/gethomepage/homepage:v2.8.0 | envoy-internal |  | onepassword-store |  |
| default | immich | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/immich-app/immich-server:v3.4.2 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store | gateway-only ingress + kube-apiserver entity |
| default | lldap | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/lldap/lldap:v0.6.3-alpine-rootless@sha256:ba2c50930ea998eefd5454aa678a7977448019248b1827da87d330df0b71c284 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | matter-server | app-template | ghcr.io/home-assistant-libs/python-matter-server:8.1.0@sha256:170aa093ce91c76cde4cc390918307590f0f5558fcec93f913af3cb019e6562a | envoy-internal | volsync | home-assistant, onepassword-store, rook-ceph-cluster |  |
| default | mosquitto | app-template | public.ecr.aws/docker/library/eclipse-mosquitto:2.0.23 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| default | paperless | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/paperless-ngx/paperless-ngx:3.5.1 | envoy-internal | cnpg, dragonfly, volsync | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress |
| default | radicale | app-template | tomsquest/docker-radicale:3.9.2.0 | envoy-external | volsync | onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| default | smtp-relay | app-template | ghcr.io/foxcpp/maddy:0.9.8 |  |  | onepassword-store | other policy |
| default | teslamate | app-template | ghcr.io/home-operations/postgres-init:18, teslamate/teslamate:4.5.0 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| default | thelounge | app-template | ghcr.io/thelounge/thelounge:4.5.2 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| default | zigbee2mqtt | app-template | ghcr.io/koenkk/zigbee2mqtt:2.14.3 | envoy-internal | volsync | mosquitto, onepassword-store, rook-ceph-cluster |  |
| default | zwave-js-ui | app-template | ghcr.io/zwave-js/zwave-js-ui:11.27.0 | envoy-internal | volsync | mosquitto, onepassword-store, node-feature-discovery-rules, rook-ceph-cluster |  |
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
| media | autobrr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/autobrr/autobrr:v1.91.1 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | bazarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/bazarr:1.6.2@sha256:6c40dfa683f767d28d1dc502837ed0a5a57682a84231f03e704e2b3f61b25a46 | envoy-internal | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | cross-seed | app-template | ghcr.io/cross-seed/cross-seed:6.13.9@sha256:c310f84e040b82c140424f6377fa36487335261037175ef9cec3aefc92b93076 |  | volsync | onepassword-store, rook-ceph-cluster |  |
| media | jellyseerr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/seerr-team/seerr:v3.5.2@sha256:aadee014b40e28cf9aa4928bc9d1183a6eb08f8c44d543cddc9efdcb16549be2 | envoy-external | cnpg, volsync | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | kometa | app-template | docker.io/kometateam/kometa:v2.5.5@sha256:864cec57d099c71a26a5a5ce2784d34d9b53874c91269c3a12df3949eab96562 |  | volsync | onepassword-store, rook-ceph-cluster, plex, radarr, sonarr, tautulli |  |
| media | plex | app-template | ghcr.io/home-operations/plex:1.43.5.11079@sha256:06ef0fc23e9af9bbaf284c3f27972f94e703d13d6f745edeb6818fcbebf6c673 | envoy-external | volsync | intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | prowlarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/prowlarr:3.0.2.5780@sha256:58fa5dbed20738ce0a72077315e818eeb731cb4b4a5173c4a837d343a9573750 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store |  |
| media | qbittorrent | app-template | ghcr.io/home-operations/qbittorrent:5.3.0@sha256:5a858e61f94cf2712391db32ed03556576c700858f3e62c4c6fcde262443ebd8 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | radarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/radarr:7.0.3.10918@sha256:55d3cf8a4c4c531bb8b5c1ba88eb270d4435e01e228fbdb16cdfc910a17e3b06 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | recyclarr | app-template | ghcr.io/recyclarr/recyclarr:8.8.1@sha256:3e9c41b9ec29bbf65fe846864058730d321a21f7695d8c0d9437b73e34d50ad9 |  | volsync | onepassword-store, rook-ceph-cluster, radarr, sonarr |  |
| media | sabnzbd | app-template | ghcr.io/home-operations/sabnzbd:5.1.3@sha256:07790a7829201d9ea302e8b862078beac4b1a07003fe8359e3f069b6bcd84a95 | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | silo | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/silo-server/silo-server:build-2903@sha256:01025c2505bd5c3e8def8c4cf98d7c54fd95f703634f5487d5c16d8e5ea49fe7 | envoy-internal | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, intel-device-plugin-gpu, onepassword-store, rook-ceph-cluster |  |
| media | sonarr | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/home-operations/sonarr:5.0.0.2997@sha256:05acf764e72fa458b5edf236771d7a08d1f120fce509d4fb8a4e799fae29fda7 | envoy-internal | cnpg | cloudnative-pg-cluster, onepassword-store, rook-ceph-cluster |  |
| media | subs | app-template | ghcr.io/home-operations/postgres-init:18, ghcr.io/mchestr/plex-manager:0.12.0@sha256:f7ccc98e01f3eb1023e4848c4697c011e6b1ec1f6da7f3e82bb4b39aa4342278 | envoy-external | cnpg, dragonfly | cloudnative-pg-cluster, dragonfly, onepassword-store, rook-ceph-cluster | gateway-only ingress + kube-apiserver entity |
| media | tautulli | app-template | ghcr.io/home-operations/tautulli:2.19.1@sha256:602dc59bbc24f3127e086c1b702860b02abb846e7669e2ed53157bc7572c5c9b | envoy-internal | volsync | onepassword-store, rook-ceph-cluster |  |
| media | tqm | app-template | ghcr.io/home-operations/tqm:1.20.0@sha256:c5bdff16ca1107712fd61dc6c39a276488908c702e68e427db889419af042761 |  |  |  |  |
| media | unpackerr | app-template | ghcr.io/unpackerr/unpackerr:v1.0.1 |  |  | onepassword-store |  |
| media | whisper | app-template | onerahmet/openai-whisper-asr-webservice:v1.10.0@sha256:0616c3d5fc6924e9d59aa8a7a3a944fbe8f3a5d701e5fc1fa2ce5b933dfecb73 |  |  | bazarr, rook-ceph-cluster |  |
| networking | cloudflared | app-template | docker.io/cloudflare/cloudflared:2026.11.1@sha256:e613aadbc2d9511785d2e67a86b0c8ac18dd63a3f9af0d06faf04cbfdcb35f2d |  |  | onepassword-store |  |
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
| observability | unpoller | app-template | ghcr.io/unpoller/unpoller:v5.10.0@sha256:6e88aa12d57ebac6798d7e37abd37f31c4584028c22df02a0f8e935ac3afe8ca |  |  | onepassword-store |  |
| observability | victoria-logs | victoria-logs-single |  | envoy-internal |  | rook-ceph-cluster, victoria-metrics-operator |  |
| observability | victoria-metrics-operator | victoria-metrics-operator |  |  |  |  |  |
| openebs-system | openebs | openebs |  |  |  |  |  |
| renovate | renovate-operator | renovate-operator |  | envoy-internal |  |  |  |
| renovate | renovate-operator-jobs |  |  |  |  | renovate-operator, onepassword-store |  |
| rook-ceph | rook-ceph | rook-ceph |  |  |  | onepassword-store |  |
| rook-ceph | rook-ceph-cluster | rook-ceph-cluster |  | envoy-internal |  | rook-ceph, rook-ceph-csi-drivers |  |
| rook-ceph | rook-ceph-csi-drivers | ceph-csi-drivers |  |  |  | rook-ceph |  |
| system-upgrade | etcd-defrag | app-template | ghcr.io/siderolabs/talosctl:v1.14.6@sha256:82c9a9985fc7292a222e680414c65955ac0566db588b84d88f620b05d16b1d5b |  |  |  |  |
| system-upgrade | tuppr | tuppr |  |  |  |  |  |
| system-upgrade | tuppr-upgrades |  |  |  |  | tuppr |  |
| volsync-system | snapshot-controller | snapshot-controller |  |  |  |  |  |
| volsync-system | volsync | volsync |  |  |  | snapshot-controller |  |
| waitlist | waitlist | app-template | ghcr.io/mchestr/waitlist-control:1.0.0@sha256:42c262ee983d32e1db0b49ff2639975b97dd3d4d1d1c78e7d5c4232353c1a159 | envoy-external | cnpg | onepassword-store, cloudnative-pg-cluster | gateway-only ingress + kube-apiserver entity |

Total Kustomizations: 96
