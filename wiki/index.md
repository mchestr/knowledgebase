# Index

Catalog of every wiki page. Read this file first. Each entry is `- [[page-name]] — one-line summary`.
Keep entries in alphabetical order inside each section.

## Overview

- [[overview]] — Top-level synthesis of everything in the knowledge base.

## Sources

- [[home-cluster-add-app-skill]] — home-cluster agent skill: add an app, build like Flux, open a PR.
- [[home-cluster-agents-md]] — home-cluster AGENTS.md: repo conventions, components, AI stack, Renovate in-cluster.
- [[home-cluster-app-inventory]] — Generated table of 98 Flux Kustomizations with gateway and policy coverage.
- [[home-cluster-application-deployment]] — home-cluster docs: Flux app layout, components, HelmRelease rules, gateway choice.
- [[home-cluster-authelia-readme]] — home-cluster: make an Authelia OIDC client and store it in 1Password.
- [[home-cluster-bootstrap]] — home-cluster docs: Talos ISO, MS-01 Secure Boot, bootstrap order before Flux.
- [[home-cluster-cilium-config-readme]] — home-cluster: UniFi BGP config that peers with Cilium.
- [[home-cluster-claude-code-agent-instructions]] — home-cluster: STE writing rules for the in-cluster Claude Code.
- [[home-cluster-claude-code-readme]] — home-cluster: in-cluster Claude Code Remote Control setup and limits.
- [[home-cluster-cnpg-component-readme]] — home-cluster: make CNPG database credentials in 1Password.
- [[home-cluster-disaster-recovery]] — home-cluster docs: backup design, VolSync, node failure, full loss, CNPG recovery and tests.
- [[home-cluster-networking]] — home-cluster docs: subnets, BGP, two gateways, split DNS, Thunderbolt ring.
- [[home-cluster-node-management]] — home-cluster docs: Talos config, reboot, maintenance, add and remove nodes.
- [[home-cluster-observability]] — home-cluster docs: Prometheus, Fluent Bit, VictoriaLogs, alerting, external checks.
- [[home-cluster-ops-agent]] — home-cluster: Claude ops subagent with kubernetes and flux-operator MCP tools.
- [[home-cluster-readme]] — home-cluster README: components, AI services, cloud costs, hardware table.
- [[home-cluster-renovate-review-skill]] — home-cluster: AI prompt that rates Renovate PR risk.
- [[home-cluster-renovate-risk-prompt]] — home-cluster: extra risk-review prompt for hand-written PRs.
- [[home-cluster-rook-ceph-readme]] — home-cluster: Rook-Ceph procedures next to the manifests.
- [[home-cluster-secrets-management]] — home-cluster docs: 1Password to External Secrets, add, sync, rotate secrets.
- [[home-cluster-storage-operations]] — home-cluster docs: Rook-Ceph health, OSD removal and repair, disk cleaning.
- [[home-cluster-terraform-readme]] — home-cluster: Cloudflare Terraform workspace in Terraform Cloud.
- [[home-cluster-troubleshooting]] — home-cluster docs: diagnostics for pods, Flux, nodes, network, DNS, certificates.
- [[home-cluster-upgrade-procedures]] — home-cluster docs: tuppr, Renovate automerge, rollback, stuck upgrades.
- [[home-cluster-volsync-restore-skill]] — home-cluster agent skill: safe VolSync restore and data check.
- [[home-cluster-waitlist-readme]] — home-cluster: Waitlist parts, guard rails, runbooks (removed upstream in 470f9f8).
- [[home-cluster-workstation-setup]] — home-cluster docs: Homebrew tools, kubectl plugins, kubeconfig and talosconfig.
- [[incident-2026-10-22-seerr-plex-signin]] — Incident: a shared Plex user could not sign in to Seerr; wrong share email.

## Entities

- [[authelia]] — SSO and 2FA in front of the internal gateway; fails closed; OIDC provider.
- [[cilium]] — CNI; LB-IPAM pool 10.0.20.0/24 advertised over BGP.
- [[claude-code-remote-control]] — In-cluster Claude Code server with cluster-admin; allowlist is the guard.
- [[cloudflare-terraform]] — Terraform for the Cloudflare tunnel, rulesets and zone settings.
- [[cloudflare-tunnel]] — The only internet entry; sends *.chestr.dev to envoy-external.
- [[cloudnative-pg]] — Postgres operator; postgres17 and immich Clusters; R2 backups and recovery procedure.
- [[envoy-gateway]] — Gateway API with envoy-internal (10.0.20.100) and envoy-external (10.0.20.200).
- [[external-secrets]] — Copies 1Password items into Kubernetes Secrets through 1Password Connect.
- [[flux]] — GitOps controller; entry point, central Helm rollback, reconcile commands.
- [[gatus]] — Status page at status.chestr.dev built from every HTTPRoute.
- [[home-cluster]] — Hub page for the home Kubernetes cluster and its repository.
- [[home-nas]] — UNAS Pro 8 (4x28TB) at 10.0.40.13; receives 4-hourly database dumps.
- [[kube-prometheus-stack]] — Prometheus, Alertmanager and Grafana; 14-day retention; Watchdog to Healthchecks.io.
- [[litellm]] — OpenAI-compatible proxy to OpenRouter in the ai namespace.
- [[lldap]] — User directory for Authelia; groups decide access.
- [[memini]] — Agent memory service; /v1 and /mcp bypass Authelia.
- [[ms-01]] — Node hardware (m0, m1, m2); IPs and Secure Boot setup.
- [[plex-manager]] — Owner's Plex companion app (subs); source of truth for Plex user details.
- [[renovate]] — Dependency bot; automerge after risk assessment and a 2-day minimum age.
- [[rook-ceph]] — Distributed block storage on 3 NVMe OSDs; health and OSD procedures.
- [[seerr]] — Media request app at requests.chestr.dev; Plex sign-in checks the share list.
- [[talos-linux]] — Node OS (1.14, Kubernetes 1.37); config files, Talos commands, rollback.
- [[tuppr]] — Automated Talos and Kubernetes upgrades gated on Ceph and VolSync.
- [[udm-pro-max]] — Gateway router; BGP peer ASN 64513, internal DNS, IoT firewall.
- [[victorialogs]] — Log store that replaced Loki; Fluent Bit collection; VMRule log alerts.
- [[volsync]] — Daily restic PVC backups to R2; restore task and monthly checks.
- [[waitlist]] — Owner's reservation-watcher app; most locked-down app in the cluster.

## Concepts

- [[app-deployment-pattern]] — Standard files, rules and steps to add an app.
- [[backup-strategy]] — Where each kind of cluster state is backed up and how it comes back.
- [[bgp-load-balancing]] — Cilium LoadBalancer IPs routed to the UDM over BGP.
- [[gitops]] — Git as desired state; what Git does not cover.
- [[in-cluster-ai-stack]] — LiteLLM, TEI embeddings, memini and Claude Code in the ai namespace.
- [[internal-vs-external-gateway]] — Security rules for choosing an app's gateway.
- [[renovate-risk-review]] — AI agent rates each PR's risk before Renovate automerge.
- [[split-horizon-dns]] — External-DNS writes hostnames to Cloudflare and the UDM.
- [[thunderbolt-ring-network]] — TB4 mesh between nodes for Ceph; how to check it.

## Syntheses

- [[app-inventory]] — All 98 Kustomizations: namespace, image, gateway, components, policy.
- [[complete-cluster-loss-runbook]] — Rebuild the cluster from Git, 1Password and R2, including Postgres.
- [[node-failure-runbook]] — Steps when one node is down: assess, move pods, bring it back.
- [[security-posture]] — External exposure, NetworkPolicy gaps, OIDC gaps, privileged automation.
- [[triage-runbook]] — First response: alert path, quick checks, symptom table.

## Issues

- [[seerr-plex-user-cannot-sign-in]] — Seerr refuses a Plex user who is not on the Plex share list with the same email.

## SOPs

- [[look-up-a-plex-user]] — Find a Plex user's email, Plex username and server access in plex-manager.
