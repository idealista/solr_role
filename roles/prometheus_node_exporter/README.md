# Prometheus node exporter role

Ansible role to install and manage node exporter

To launch tests

```bash
molecule test
```

You can add country, env and service roles to help identify machines on prometheus/grafana.

```yaml
node_exporter_country_role: es
node_exporter_env_role: local
node_exporter_service_roles:
  - vagrant
  - test
```
