# TODO: Modify below tests with actual ones.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    pkg = host.package("foreman-installer")

    assert pkg.is_installed
    # assert pkg.version.startswith(version)


# @pytest.mark.parametrize("port", "proto", [
#     ("53", "tcp"),
#     ("53", "udp"),
#     ("67", "udp"),
#     ("68", "udp"),
#     ("69", "udp"),
#     ("80", "tcp"),
#     ("443", "tcp"),
#     ("3000", "tcp"),
#     ("3306", "tcp"),
#     ("5432", "tcp"),
#     ("8140", "tcp"),
#     ("8443", "tcp"),
# ])
# def test_firewall(host, port, proto):
#     svc = host.service('firewalld')
#     socket = host.socket("{0}://{1}".format((proto, port)))
#
#     assert svc.is_running
#     assert svc.is_enabled
#     assert(socket.is_listening)


# def test_foreman(host, File):
#     f = host.File("/etc/ansible/facts.d/install_foreman.fact")
#
#     assert f.exists
#     assert f.is_file
