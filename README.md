![Logo](https://raw.githubusercontent.com/idealista/solrcloud-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/solrcloud-role.png)](https://travis-ci.org/idealista/solrcloud-role)

# SolrCloud Ansible role

This ansible role installs a SolrCloud server in a debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [SolrCloud](https://cwiki.apache.org/confluence/display/solr/SolrCloud) server in a Debian system.

### Prerequisities

Ansible 2.2.1.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (using [hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.solrcloud-role
  version: 1.8.0
  name: solrcloud
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
    - { role: solrcloud }
```

Playbook example showing how to provision from scratch a solrcloud cluster plus create a collection called `mycollection`, using idealista [java](https://github.com/idealista/java-role), [zookeeper](https://github.com/idealista/zookeeper-role) and [solrcloud](https://github.com/idealista/solrcloud-role) roles.

> :warning: Use the example below just as a reference, requires inventory host groups `solr` and `zookeeper` to be correctly defined
```
- hosts: solr:zookeeper
  roles:
    - role: idealista.java-role
      become: yes
      vars:
        java_open_jdk_set_version: 8   

- hosts: zookeeper
  roles:
    - role: idealista.zookeeper-role
      become: yes
      vars:
        zookeeper_hosts: "
          {%- set ips = [] %}
          {%- for host in groups['zookeeper'] %}
          {{- ips.append(dict(id=loop.index, host=host, ip=hostvars[host]['ansible_default_ipv4'].address)) }}
          {%- endfor %}
          {{- ips -}}"

- hosts: solr
  serial:
    - 1
    - "100%"
  roles:
    - role: idealista.solrcloud-role
      become: yes
      vars:
        solr_cloud_version: 6.5.1
        solr_heap: "10G"
        solr_zookeeper_hosts: "
          {%- set ips = [] %}
          {%- for host in groups['zookeeper'] %}
          {{- ips.append(hostvars[host]['ansible_default_ipv4'].address) }}
          {%- endfor %}
          {{- ips | zip_longest([], fillvalue=':2181') | map('join') | join(',') -}}
        "
        solr_host: "{{ ansible_hostname }}"

- hosts: solr
  vars:
    solr_replicas: "{{ 1 if groups['solr'] | length == 1 else 2 }}"
    solr_shards: "{{ groups['solr'] | length }}"
    solr_collection_home: /var/solr
    solr_collection_name: mycollection
    solr_collection_ok_file: "{{ solr_collection_home }}/create_collection.ok"

  tasks:
  - name: Upload collection
    become: yes
    when: "inventory_hostname == groups['solr'][0]"
    copy:
      src: "{{ playbook_dir }}/{{ solr_collection_name }}"
      dest: "{{ solr_collection_home }}"
      owner: solr
      group: solr
      mode: 0644

  - name: Create mycollection collection
    become: yes
    when: "inventory_hostname == groups['solr'][0]"
    become_user: solr
    shell: |
      /opt/solr/bin/solr create_collection \
        -c {{solr_collection_name}} \
        -n {{solr_collection_name}} \
        -d {{solr_collection_home}}/{{solr_collection_name}} \
        -shards {{solr_shards}} \
        -replicationFactor {{solr_replicas}} \
        && touch {{solr_collection_ok_file}}

    register: command_output
    args:
      executable: /bin/bash
      creates: "{{solr_collection_ok_file}}"

  - name: Collection creation print
    debug: msg="{{ command_output }}"
```

## Usage

Look to the defaults properties file to see the possible configuration properties.

## Testing

```
molecule test --platform=Debian9
```

See molecule.yml to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.1.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/solrcloud-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/solrcloud-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
