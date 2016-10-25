import pytest

@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]

@pytest.fixture()
def AnsibleVarBinDir(Ansible):
    return Ansible("debug", "msg={{ node_exporter_bin_dir }}")["msg"]

def test_node_exporter_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["node_exporter_user"]).exists
    assert Group(AnsibleDefaults["node_exporter_group"]).exists
    assert User(AnsibleDefaults["node_exporter_user"]).group == AnsibleDefaults["node_exporter_group"]

def test_node_exporter_conf(File, User, Group, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["node_exporter_root_dir"])
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["node_exporter_user"]
    assert conf_dir.group == AnsibleDefaults["node_exporter_group"]

def test_node_exporter_executable(File, Command, AnsibleDefaults, AnsibleVarBinDir):
    node_exporter = File(AnsibleDefaults["node_exporter_bin_dir"] + "/node_exporter")
    assert node_exporter.exists
    assert node_exporter.is_file
    assert node_exporter.user == AnsibleDefaults["node_exporter_user"]
    assert node_exporter.group == AnsibleDefaults["node_exporter_group"]
    assert File("/usr/bin/node_exporter").exists
    assert File("/usr/bin/node_exporter").is_symlink
    assert File("/usr/bin/node_exporter").linked_to == AnsibleVarBinDir + "/node_exporter"
    node_exporter_version = Command("node_exporter --version")
    assert node_exporter_version.rc is 0
    assert "version " + AnsibleDefaults["node_exporter_version"] in node_exporter_version.stdout

def test_node_exporter_service(File, Service, Socket, AnsibleDefaults):
    assert File("/etc/init.d/node_exporter").exists
    assert Service("node_exporter").is_enabled
    assert Service("node_exporter").is_running
    assert Socket("tcp://:::9100").is_listening

def test_node_exporter_roles(File, AnsibleDefaults):
    roles = File(AnsibleDefaults["node_exporter_textfile_collector"] + "/roles.prom")
    assert roles.exists
    assert roles.user == AnsibleDefaults["node_exporter_user"]
    assert roles.group == AnsibleDefaults["node_exporter_group"]
    assert roles.contains("machine_country{role=\"es\"} 1")
    assert roles.contains("machine_env{role=\"pre\"} 1")
    assert roles.contains("machine_role{role=\"vagrant\"} 1")
