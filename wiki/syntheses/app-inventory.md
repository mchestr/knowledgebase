---
title: App inventory
type: synthesis
question: Which apps run in the home-cluster, and how is each one exposed and backed up?
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, inventory]
---

# App inventory

## Answer

The [[home-cluster]] runs 98 Flux Kustomizations in 17 namespaces at commit `e36a8c8` ([[home-cluster-app-inventory]]). The table is generated from the manifests. Check the source page for the method limits.

- Gateway: **external** is `envoy-external` (internet through the [[cloudflare-tunnel]]). internal is `envoy-internal` (LAN, behind [[authelia]]). See [[internal-vs-external-gateway]].
- Components: `volsync` ([[volsync]] backup), `cnpg` ([[cloudnative-pg]] database), `dragonfly` (Redis-compatible store).
- Policy: `gateway` means only the external or internal gateway may connect. `apiserver` means the CiliumNetworkPolicy for the `kube-apiserver` entity. `other` means another NetworkPolicy. Empty means none in the app path.

| Namespace | App | Chart / image | Gateway | Components | Policy |
| --- | --- | --- | --- | --- | --- |
| actions-runner-system | actions-runner-controller | gha-runner-scale-set-controller |  |  |  |
| actions-runner-system | actions-runner-controller-runners | gha-runner-scale-set |  |  |  |
| ai | [[claude-code-remote-control\|claude-code]] | node:24-bookworm |  |  | other |
| ai | [[litellm\|litellm]] |  | internal | dragonfly |  |
| ai | litellm-operator | litellm-operator |  |  |  |
| ai | [[memini\|memini]] | memini | internal | volsync |  |
| ai | text-embeddings | text-embeddings-inference:cpu-1.8 |  |  |  |
| cert-manager | cert-manager | cert-manager |  |  |  |
| cert-manager | cert-manager-issuers |  |  |  |  |
| database | [[cloudnative-pg\|cloudnative-pg]] | cloudnative-pg |  |  |  |
| database | cloudnative-pg-cluster |  |  |  |  |
| database | cloudnative-pg-roles |  |  |  |  |
| database | dragonfly | operator:v1.7.1 |  |  |  |
| default | atuin | atuin:18.24.1 | internal | cnpg |  |
| default | [[authelia\|authelia]] | authelia:4.39.28 | **external** | cnpg, dragonfly |  |
| default | esphome | esphome:2026.9.1 | internal | volsync |  |
| default | frigate | frigate:0.18.2 | internal | volsync |  |
| default | govee2mqtt | govee2mqtt:latest | internal | volsync |  |
| default | home-assistant | home-assistant:2026.10.2 | **external** | volsync | gateway |
| default | homepage | homepage:v2.6.0 | internal |  |  |
| default | immich | immich-server:v3.3.3 | **external** | cnpg, dragonfly | gateway + apiserver |
| default | [[lldap\|lldap]] | lldap:v0.6.3-alpine-rootless | internal | cnpg |  |
| default | matter-server | python-matter-server:8.1.0 | internal | volsync |  |
| default | mosquitto | eclipse-mosquitto:2.0.22 |  | volsync |  |
| default | paperless | paperless-ngx:3.3.2 | internal | cnpg, dragonfly, volsync | gateway |
| default | radicale | docker-radicale:3.8.3.0 | **external** | volsync | gateway + apiserver |
| default | smtp-relay | maddy:0.9.6 |  |  | other |
| default | teslamate | teslamate:4.3.0 | internal | cnpg |  |
| default | thelounge | thelounge:4.5.2 | internal | volsync |  |
| default | windmill | windmill | **external** | cnpg |  |
| default | zigbee2mqtt | zigbee2mqtt:2.14.2 | internal | volsync |  |
| default | zwave-js-ui | zwave-js-ui:11.24.3 | internal | volsync |  |
| external-secrets | external-secrets | external-secrets |  |  |  |
| external-secrets | onepassword | connect-api:1.8.3 |  |  |  |
| external-secrets | onepassword-store |  |  |  |  |
| flux-system | flux-instance | flux-instance | **external** |  |  |
| flux-system | flux-operator | flux-operator | internal |  |  |
| kube-system | [[cilium\|cilium]] | cilium | internal |  |  |
| kube-system | cilium-config |  |  |  |  |
| kube-system | coredns | coredns |  |  |  |
| kube-system | descheduler | descheduler |  |  |  |
| kube-system | intel-device-plugin-gpu | intel-device-plugins-gpu |  |  |  |
| kube-system | intel-device-plugin-operator | intel-device-plugins-operator |  |  |  |
| kube-system | irqbalance | irqbalance:1.9.5 |  |  |  |
| kube-system | kubelet-csr-approver | kubelet-csr-approver |  |  |  |
| kube-system | metrics-server | metrics-server |  |  |  |
| kube-system | node-feature-discovery | node-feature-discovery |  |  |  |
| kube-system | node-feature-discovery-rules |  |  |  |  |
| kube-system | reloader | reloader |  |  |  |
| kube-system | spegel | spegel |  |  |  |
| media | autobrr | autobrr:v1.88.0 | internal | cnpg |  |
| media | bazarr | bazarr:1.6.2 | internal | cnpg, volsync |  |
| media | cross-seed | cross-seed:6.13.7 |  | volsync |  |
| media | jellyfin | jellyfin:12.2 | internal | volsync |  |
| media | jellyplex-watched | jellyplex-watched:8.5.3 |  |  |  |
| media | jellyseerr | seerr:v3.5.0 | **external** | cnpg, volsync | gateway + apiserver |
| media | kometa | kometa:v2.5.3 |  | volsync |  |
| media | plex | plex:1.43.4.10903 | **external** | volsync |  |
| media | prowlarr | prowlarr:2.6.5.5623 | internal | cnpg |  |
| media | qbittorrent | qbittorrent:5.2.4 | internal | volsync |  |
| media | radarr | radarr:6.4.4.10685 | internal | cnpg |  |
| media | recyclarr | recyclarr:8.8.0 |  | volsync |  |
| media | sabnzbd | sabnzbd:5.1.3 | internal | volsync |  |
| media | sonarr | sonarr:5.0.0.2668 | internal | cnpg |  |
| media | subs | plex-manager:0.1.0 | **external** | cnpg, dragonfly | gateway + apiserver |
| media | tautulli | tautulli:2.18.2 | internal | volsync |  |
| media | tqm | tqm:1.20.0 |  |  |  |
| media | unpackerr | unpackerr:v0.16.1 |  |  |  |
| media | whisper | openai-whisper-asr-webservice:v1.10.0 |  |  |  |
| networking | cloudflared | cloudflared:2026.10.1 |  |  |  |
| networking | [[envoy-gateway\|envoy]] | gateway-helm | **external**, internal |  |  |
| networking | external-dns-cloudflare | external-dns |  |  |  |
| networking | external-dns-unifi | external-dns; external-dns-unifi-webhook:v0.9.0 |  |  |  |
| networking | multus | cni-plugins:1.9.1 |  |  |  |
| networking | multus-config |  |  |  |  |
| observability | fluent-bit | fluent-bit |  |  |  |
| observability | [[gatus\|gatus]] | gatus-sidecar:0.5.3 | **external** |  |  |
| observability | grafana | grafana-operator |  |  |  |
| observability | grafana-instance |  | internal | cnpg |  |
| observability | kromgo | kromgo:v0.10.0 | **external** |  |  |
| observability | [[kube-prometheus-stack\|kube-prometheus-stack]] | kube-prometheus-stack | internal |  | apiserver |
| observability | silence-operator | silence-operator |  |  |  |
| observability | silence-operator-crds | silence-operator-crds |  |  |  |
| observability | unpoller | unpoller:v5.6.2 |  |  |  |
| observability | victoria-logs | victoria-logs-single | internal |  |  |
| observability | victoria-metrics-operator | victoria-metrics-operator |  |  |  |
| openebs-system | openebs | openebs |  |  |  |
| renovate | renovate-operator | renovate-operator | internal |  |  |
| renovate | renovate-operator-jobs |  |  |  |  |
| rook-ceph | rook-ceph | rook-ceph |  |  |  |
| rook-ceph | rook-ceph-cluster | rook-ceph-cluster | internal |  |  |
| rook-ceph | rook-ceph-csi-drivers | ceph-csi-drivers |  |  |  |
| system-upgrade | etcd-defrag | talosctl:v1.14.3 |  |  |  |
| system-upgrade | [[tuppr\|tuppr]] | tuppr |  |  |  |
| system-upgrade | tuppr-upgrades |  |  |  |  |
| volsync-system | snapshot-controller | snapshot-controller |  |  |  |
| volsync-system | [[volsync\|volsync]] | volsync |  |  |  |
| waitlist | [[waitlist\|waitlist]] | waitlist-control:1.0.0 | **external** | cnpg | gateway + apiserver |

## Analysis

- 13 Kustomizations route to `envoy-external`. Their policy coverage is in [[security-posture]].
- Images pinned with `@sha256` digests in the raw file are shown here without the digest.
- `busybox` and `postgres-init` init images are left out of the "Chart / image" column.

## Sources

- [[home-cluster-app-inventory]]
