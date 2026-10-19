---
title: Security posture
type: synthesis
question: How exposed is the home-cluster, and where are the gaps?
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, security]
---

# Security posture

## Answer

The [[home-cluster]] has two layers in front of apps: the gateway choice and the NetworkPolicy of each app. Internal apps are behind [[authelia]], which fails closed. External apps rely on their own login ([[internal-vs-external-gateway]]). At commit `e36a8c8`, the main gaps are external apps without a NetworkPolicy, OIDC clients without group limits, and a powerful in-cluster agent.

### External exposure

13 Kustomizations route to `envoy-external`. One of them is the `envoy` gateway itself. The rule says each external app needs two policies: ingress only from the external gateway's Envoy pods, and a CiliumNetworkPolicy for the `kube-apiserver` entity, because cross-node gateway traffic is SNATed to a control-plane node ([[home-cluster-agents-md]], [[home-cluster-networking]]).

| Coverage | Apps |
| --- | --- |
| Both policies | `immich`, `jellyseerr`, `radicale`, `subs`, [[waitlist]] |
| Gateway policy only | `home-assistant` |
| No policy in the app path | [[authelia]], `windmill`, `plex`, [[gatus]], `kromgo`, `flux-instance` |

Source: [[home-cluster-app-inventory]]. `AGENTS.md` says "not every app has one yet" ([[home-cluster-agents-md]]).

The reference implementations are `default/radicale` and `waitlist` ([[home-cluster-agents-md]], [[home-cluster-networking]]). `home-assistant` has no `kube-apiserver` rule, so it is not a complete example ([[home-cluster-app-inventory]]).

> [!question] Unverified
> The sources do not say whether `home-assistant` loses cross-node gateway traffic without the `kube-apiserver` rule.

Other paths into pods:
- Home Assistant, Frigate, ESPHome, matter-server and govee2mqtt have a Multus leg on the IoT VLAN with no gateway and no NetworkPolicy. A UDM firewall rule is the only control ([[home-cluster-networking]]).
- [[memini]] `/v1` and `/mcp` bypass Authelia and rely on memini's API key ([[home-cluster-agents-md]]).

### Identity

- [[lldap]] is the user directory. Groups decide access: two-factor for `admin`, one-factor for `media` on the *arr apps, deny by default ([[home-cluster-networking]]).

WARNING: Before you add a second user to lldap, give Autobrr, Grafana, Immich, Paperless and Windmill their own `authorization_policies`. Any lldap account can use every OIDC client without one, and can enrol its own second factor ([[home-cluster-waitlist-readme]]).

- OIDC client secrets go from the Authelia CLI straight into 1Password and never reach the screen ([[home-cluster-authelia-readme]]).

### Automation with write access

- [[claude-code-remote-control]] has `cluster-admin`, talosctl and push access to the repository. Its only guard is the permission allowlist and approval in the Claude app. It has an outbound-only NetworkPolicy and no route ([[home-cluster-claude-code-readme]]).
- The `ops` subagent can delete pods and resources and apply manifests through MCP servers ([[home-cluster-ops-agent]]).
- [[renovate]] automerges minor, patch and digest updates, and its own majors, after the [[renovate-risk-review]]. The review agent can edit config on a high rating and treats release notes as untrusted data ([[home-cluster-agents-md]], [[home-cluster-renovate-review-skill]]).

### Hardened example

[[waitlist]] is the most restricted app. It has three ValidatingAdmissionPolicies for its browser pods, and a fetcher with no credentials whose egress allows only one FQDN, with an `egressDeny` for private ranges ([[home-cluster-waitlist-readme]]).

## Analysis

The highest-value fixes in the sources are: add policies to the six external apps that have none; add the `kube-apiserver` rule to `home-assistant`; add group limits to the five OIDC clients before any second user exists.

## Sources

- [[home-cluster-app-inventory]]
- [[home-cluster-agents-md]]
- [[home-cluster-networking]]
- [[home-cluster-waitlist-readme]]
- [[home-cluster-claude-code-readme]]
