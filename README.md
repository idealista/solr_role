![Logo](https://raw.githubusercontent.com/idealista/solr_role/master/logo.gif)

[![Build Status](https://api.travis-ci.com/idealista/solr_role.png)](https://app.travis-ci.com/github/idealista/solr_role)

# Solr Ansible role

This ansible role installs a Solr server in a debian environment.

- [Solr Ansible role](#solr-ansible-role)
  - [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
  - [Usage](#usage)
    - [Add JVM Agent to your installation](#add-jvm-agent-to-your-installation)
  - [Set up collections](#set-up-collections)
  - [Set up cores](#set-up-cores)
  - [Prometheus Exporter](#prometheus-exporter)
  - [Testing](#testing)
  - [Built With](#built-with)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Solr](https://cwiki.apache.org/confluence/display/solr/SolrCloud) server in a Debian system.

This role is tested on:
- Debian
  - stretch (java 8 and 11)
  - buster (java 11)
- Ubuntu
  - focal (java 8 and 14)

### Prerequisities

Ansible 2.8.8 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.solr_role
  version: x.x.x
  name: solr
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: solr }
```

Playbook example below showing how to provision from scratch a SolrCloud cluster with two nodes plus create an example (and empty) collection called `sample_techproducts_configs`, using idealista [java](https://github.com/idealista/java-role), [zookeeper](https://github.com/idealista/zookeeper_role) and [solr](https://github.com/idealista/solr_role) roles:

**Note:** Assuming that 'solrcloud' group has two nodes (`solrcloud1` and `solrcloud2`) as is declared in [molecule.yml](https://github.com/idealista/solr_role/tree/master/molecule/default/molecule.yml),
collection will have two shards, one replica and one shard per node as is declared in group vars file called [solrcloud.yml](https://github.com/idealista/solr_role/tree/master/molecule/default/group_vars/solrcloud.yml)
and configuration files are stored under directory called `sample_techproducts_configs` under template directory.

> :warning: Use the example below just as a reference, requires inventory host groups `solr` and `zookeeper` to be correctly defined

```
---

- hosts: zookeeper
  roles:
    - role: zookeeper
  pre_tasks:
    - name: installing required libs
      apt:
        pkg: "{{ item }}"
        state: present
      with_items:
        - net-tools
        - netcat

- hosts: solrcloud
  roles:
    - role: solr_role
```

## Usage

Look to the defaults properties file to see the possible configuration properties.

### Add JVM Agent to your installation

This role supports JVM agents (such as [Newrelic](https://newrelic.com/), [Datadog](https://www.datadoghq.com/), etc.) to be used inside your installation.
You can view an example with JVM Agents in the molecule tests section --> [example_setup_with_agent](molecule/setup_with_agent).

Its very simple, must follow this steps (in this case we will add config for [Newrelic's agent](https://newrelic.com/)):
- Just add the config in your group_vars.
  ```yml
  solr_agents_required_libs:
    - unzip
    - apt-transport-https
  solr_agents_config:
    - name: "newrelic"
      download_url: "http://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip"
      vm_opts:
        - '-javaagent:{{ solr_installation_dir }}/newrelic/newrelic.jar'
      configuration_files:
        - "newrelic.yml"
      params: {
        application_name: "application_sample_name",
        license_key: "your_license_key"
      }
  ```
- __Optional__: Place the configuration files in the templates folder using this order "templates/{{ agent_name }}/{{ file names specified in solr_agents_config.configuration_files }}.j2. In this case we have the newrelic.yml.j2 in [templates/agents/newrelic/newrelic.yml.j2](molecule/setup_with_agent/templates/agents/newrelic/newrelic.yml.j2).

## Set up collections

In order to configure collections just put this config in yml like this example:

```yaml
solr_mode: cloud
solr_collections:
  # Extracted from https://github.com/apache/lucene-solr/tree/master/solr/server/solr/configsets/sample_techproducts_configs/conf
  # Should have configuration files under "templates/collections/[collection_name]" directory
  sample_techproducts_configs:
    shards: 2
    replicas: 1
    shards_per_node: 1
    auto_add_replicas: false
  sample_techproducts_configs_2:
    shards: 2
    replicas: 1
    shards_per_node: 1
```

## Set up cores

In order to configure cores just put this config in yml like this example:

```yaml
solr_mode: standalone
solr_cores:
  # Extracted from https://github.com/apache/lucene-solr/tree/master/solr/server/solr/configsets/sample_techproducts_configs/conf
  # Should have configuration files under "templates/collections/[collection_name]" directory
  - mail
```

## Prometheus Exporter

If you want to scrape metrics from Solr using [Prometheus](https://github.com/idealista/prometheus_server-role), you will need to [configure a exporter](https://lucene.apache.org/solr/guide/7_7/monitoring-solr-with-prometheus-and-grafana.html). We have a [Prometheus Solr Exporter role](https://github.com/idealista/prometheus_solr_exporter_role) that will make configuration easier for you, just keep in mind that the variables `solr_version` and `prometheus_solr_exporter_version` must have the same value.

## Testing

```
$ pipenv sync
$ pipenv shell

# This will execute tests but doesn't destroy created environment (because of --destroy=never)
$ molecule test --destroy=never -s setup_with_collections
```

Solr Admin UI should be accessible from docker container host at URL:

http://localhost:8983/solr/#/ (node: `solrcloud1`)

or

http://localhost:8984/solr/#/ (node: `solrcloud2`)

<img src="https://raw.githubusercontent.com/idealista/solr_role/master/assets/solr_admin_ui.png" alt="Solr Admin UI example" style="width: 600px;"/>

See [molecule.yml](https://github.com/idealista/solr_role/blob/master/molecule/default/molecule.yml) to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.8-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.0.4-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.11-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/solr_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](https://github.com/idealista/solr_role/blob/master/CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/solr_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/idealista/solr_role/blob/master/.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
