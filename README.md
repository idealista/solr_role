SolrCloud playbook
==================

TODO
====

- set vars per environment (like zookeeper hosts, etc.)
- Set solr_cloud vars for prometheus in group vars (actually hardcoded)
- not try to reinstall if a previous installation was found
- zhcli.sh should be executed once in each installation (is not a per host task)
- set interfaces per environment (eth1 in vagrant, default in other cases (see http://opengrok.int.sys.idealista:8080/search?q=consul_interface&defs=&refs=&path=&hist=&type=&project=as))
