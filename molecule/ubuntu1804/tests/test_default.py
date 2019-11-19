import os
# import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    assert host.package('nginx').is_installed


def test_service(host):
    service = host.service('nginx')
    assert service.is_running


def test_configuration(host):
    c = host.file('/etc/nginx/sites-enabled/default')
    assert not c.exists


def test_logrotate(host):
    log = host.file("/etc/logrotate.d/nginx")
    assert log.contains("daily")
    assert log.contains("rotate 366")


def test_version(host):
    r = host.run('nginx -v')
    assert r.rc == 0
    ver = r.stderr.strip()
    assert ver.startswith('nginx version: nginx/1.14.')
