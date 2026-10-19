# Index

Catalog of every wiki page. Read this file first. Each entry is `- [[page-name]] — one-line summary`.
Keep entries in alphabetical order inside each section.

## Overview

- [[overview]] — Top-level synthesis of everything in the knowledge base.

## Sources

- [[home-cluster-application-deployment]] — home-cluster docs: Flux app layout, components, HelmRelease rules, gateway choice.
- [[home-cluster-bootstrap]] — home-cluster docs: Talos ISO, MS-01 Secure Boot, bootstrap order before Flux.
- [[home-cluster-disaster-recovery]] — home-cluster docs: backup design, VolSync, node failure, full loss, CNPG recovery and tests.
- [[home-cluster-networking]] — home-cluster docs: subnets, BGP, two gateways, split DNS, Thunderbolt ring.
- [[home-cluster-node-management]] — home-cluster docs: Talos config, reboot, maintenance, add and remove nodes.
- [[home-cluster-observability]] — home-cluster docs: Prometheus, Fluent Bit, VictoriaLogs, alerting, external checks.
- [[home-cluster-readme]] — home-cluster README: components, AI services, cloud costs, hardware table.
- [[home-cluster-secrets-management]] — home-cluster docs: 1Password to External Secrets, add, sync, rotate secrets.
- [[home-cluster-storage-operations]] — home-cluster docs: Rook-Ceph health, OSD removal and repair, disk cleaning.
- [[home-cluster-troubleshooting]] — home-cluster docs: diagnostics for pods, Flux, nodes, network, DNS, certificates.
- [[home-cluster-upgrade-procedures]] — home-cluster docs: tuppr, Renovate automerge, rollback, stuck upgrades.
- [[home-cluster-workstation-setup]] — home-cluster docs: Homebrew tools, kubectl plugins, kubeconfig and talosconfig.

## Entities

- [[authelia]] — SSO and 2FA in front of the internal gateway; fails closed; OIDC provider.
- [[cilium]] — CNI; LB-IPAM pool 10.0.20.0/24 advertised over BGP.
- [[cloudflare-tunnel]] — The only internet entry; sends *.chestr.dev to envoy-external.
- [[cloudnative-pg]] — Postgres operator; postgres17 and immich Clusters; R2 backups and recovery procedure.
- [[envoy-gateway]] — Gateway API with envoy-internal (10.0.20.100) and envoy-external (10.0.20.200).
- [[external-secrets]] — Copies 1Password items into Kubernetes Secrets through 1Password Connect.
- [[flux]] — GitOps controller; entry point, central Helm rollback, reconcile commands.
- [[home-cluster]] — Hub page for the home Kubernetes cluster and its repository.
- [[home-nas]] — NAS for database dumps; README and networking docs disagree on the model.
- [[kube-prometheus-stack]] — Prometheus, Alertmanager and Grafana; 14-day retention; Watchdog to Healthchecks.io.
- [[ms-01]] — Node hardware (m0, m1, m2); IPs and Secure Boot setup.
- [[renovate]] — Dependency bot; automerge after risk assessment and a 2-day minimum age.
- [[rook-ceph]] — Distributed block storage on 3 NVMe OSDs; health and OSD procedures.
- [[talos-linux]] — Node OS (1.14, Kubernetes 1.37); config files, Talos commands, rollback.
- [[tuppr]] — Automated Talos and Kubernetes upgrades gated on Ceph and VolSync.
- [[udm-pro-max]] — Gateway router; BGP peer ASN 64513, internal DNS, IoT firewall.
- [[victorialogs]] — Log store that replaced Loki; Fluent Bit collection; VMRule log alerts.
- [[volsync]] — Daily restic PVC backups to R2; restore task and monthly checks.

## Concepts

- [[app-deployment-pattern]] — Standard files, rules and steps to add an app.
- [[backup-strategy]] — Where each kind of cluster state is backed up and how it comes back.
- [[bgp-load-balancing]] — Cilium LoadBalancer IPs routed to the UDM over BGP.
- [[gitops]] — Git as desired state; what Git does not cover.
- [[internal-vs-external-gateway]] — Security rules for choosing an app's gateway.
- [[split-horizon-dns]] — External-DNS writes hostnames to Cloudflare and the UDM.
- [[thunderbolt-ring-network]] — TB4 mesh between nodes for Ceph; how to check it.

## Syntheses

- [[complete-cluster-loss-runbook]] — Rebuild the cluster from Git, 1Password and R2, including Postgres.
- [[node-failure-runbook]] — Steps when one node is down: assess, move pods, bring it back.
- [[triage-runbook]] — First response: alert path, quick checks, symptom table.
