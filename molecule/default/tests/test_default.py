import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    assert host.package('nginx').is_installed


def test_service(host):
    service = host.service('nginx')
    assert service.is_running
