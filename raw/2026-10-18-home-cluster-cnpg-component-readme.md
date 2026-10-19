https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/components/cnpg/README.md

# CloudNative PG

[CloudNative PG](https://cloudnative-pg.io/) is a Kubernetes operator that manages PostgreSQL workloads. This document provides instructions for managing application database secrets.

## Creating Database Credentials

### Populate Secrets for a New Application

Use the following script to generate and store PostgreSQL credentials for a new application in 1Password:

```bash
# Set the application name
export APP=sonarr

# Generate a secure password
PASSWORD=$(op item create --category password --generate-password=letters,digits,20 --dry-run --format json | jq -r '.fields[0].value')

# Store credentials in 1Password
op item edit cloudnative-pg "${APP}_postgres_username[text]=${APP}"
op item edit cloudnative-pg "${APP}_postgres_password[password]=${PASSWORD}"
```
