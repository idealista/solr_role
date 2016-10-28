import pytest

@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]

@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]

@pytest.fixture()
def AnsibleDistribution(Ansible):
    return Ansible("setup")["ansible_facts"]["ansible_distribution"]

def test_java_resources(File, AnsibleDefaults, AnsibleDistribution):
    if AnsibleDistribution == "Debian":
        java_resources = File("/etc/apt/sources.list.d/ppa_launchpad_net_webupd8team_java_ubuntu.list")
        assert java_resources.contains(AnsibleDefaults["java_repo"])
    elif AnsibleDistribution == "Ubuntu":
        java_resources = File("/etc/apt/sources.list.d/ppa_webupd8team_java_xenial.list")
        assert java_resources.contains("deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main")
    else:
        raise ValueError("Unsupported distribution: " + AnsibleDistribution)

def test_java_package(Package, AnsibleVars):
    for version in AnsibleVars["java_version"]:
        assert Package("oracle-java" + version + "-installer").is_installed

def test_java_default(File, Package, Command, AnsibleVars):
    assert Package("oracle-java" + AnsibleVars["java_set_version"] + "-set-default").is_installed
    assert AnsibleVars["java_set_version"] in Command("java -version").stderr
    assert File("/usr/lib/jvm/default-java").is_symlink
    assert File("/usr/lib/jvm/default-java").linked_to == "/usr/lib/jvm/java-" + (AnsibleVars["java_set_version"]) + "-oracle"
