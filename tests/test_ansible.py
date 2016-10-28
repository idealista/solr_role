import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_solr_version(File, AnsibleVars):
    version = AnsibleVars["solr_cloud_version"]
    assert File("/opt/solr-" + version).exists
    assert File("/opt/solr").is_symlink
    assert File("/opt/solr").linked_to == "/opt/solr-" + version


def test_solr_service(File, Service, Socket, AnsibleVars):
    port = AnsibleVars["solr_port"]
    assert File("/etc/init.d/solr").exists
    assert Service("solr").is_enabled
    assert Service("solr").is_running
    assert Socket("tcp://:::" + str(port)).is_listening
