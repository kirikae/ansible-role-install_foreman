# TODO: Modify below tests with actual ones.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_foreman_package(host):
    pkg = host.package('foreman-installer')

    assert pkg.is_installed

def test_firewalld_service(host):
    srv = host.service('firewalld')

    assert srv.is_running
    assert srv.is_enabled
