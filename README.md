<!-- GitHub Shields -->
[![Github (license)](https://img.shields.io/github/license/kirikae/ansible-role-install_foreman.svg)](https://github.com/kirikae/ansible-role-install_foreman/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/kirikae/ansible-role-install_foreman.svg)](https://github.com/kirikae/ansible-role-install_foreman/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/kirikae/ansible-role-install_foreman.svg)](https://github.com/kirikae/ansible-role-install_foreman/pulls)
<!-- Ansible Shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fkirikae%2Fansible-role-install_foreman%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/install_foreman)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fkirikae%2Fansible-role-install_foreman%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/install_foreman)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fkirikae%2Fansible-role-install_foreman%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/install_foreman)

# Ansible Role: install_foreman

Install and configure The Foreman or Red Hat Satellite 6.

## Description

This role is designed to install The Foreman, or Red Hat Satellite 6 with an extremely basic configuration.

The intent is to have this role be compatible with either The Foreman, or Satellite 6. Installing both in a way that they should function the same. This role will not do any configuration of either application beyond the initial setup of an Organization with DNS and DHCP. This should place the application in a state that is almost ready to start provisioning hosts.

## Requirements

To utilise this role to install Red Hat Satellite 6, you will need the required subscriptions for RHEL and Satellite 6.

To utilise this role for either The Foreman or Satellite 6, you will need to ensure the [Foreman Ansible Modules](https://github.com/theforeman/foreman-ansible-modules) are present and usable by Ansible. This will only be required until these modules are pushed into mainline Ansible.

Modules used:

* [module](link)

## Installation

<!-- TODO: Installation process to use this repository -->

Install from [Ansible Galaxy](https://galaxy.ansible.com/kirikae/install_foreman)
```bash
ansible-galaxy install kirikae.install_foreman
```

Install from [GitHub](https://github.com/kirikae/ansible-role-install_foreman)
```bash
git clone https://github.com/kirikae/ansible-role-install_foreman.git kirikae.install_foreman
```

Dependencies:
```bash
ansible-galaxy install -r requirements.yml
```

## Usage

<!-- TODO: How to use this repository -->

### Variables

| Variable      | Default     | Comments (type)         |
| :---          | :---        | :---                    |
| `key`         | `value`     | Key and default value.  |

### Example Playbook

Running Ansible [Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html) can be done in a [playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Defaults

```yaml
- hosts: all
  roles:
    - role: kirikae.install_foreman
```

#### Customised

```yaml
- hosts: all
  roles:
    - role: kirikae.install_foreman
      variable: value
      also_a_variable:
        - foo
        - bar
```

## Known Issues

<!-- TODO: List any known issues -->

## Testing

Ansible specific testing is done with [Molecule](https://molecule.readthedocs.io/en/stable/).

## Contribute

If you would like to contribute to further development of this role, Thanks!

Submit some [Bugs, Feature Requests, Suggestions](https://github.com/kirikae/ansible-role-install_foreman/issues)
Submit a [Pull Requests](https://github.com/kirikae/ansible-role-install_foreman/pulls)

## License

[MIT](https://spdx.org/licenses/MIT.html)

All modules and module_utils provided by the [Foreman Ansible Modules](https://github.com/theforeman/foreman-ansible-modules) are licensed under [GPL-3.0](http://www.gnu.org/licenses/) these are distributed here as dependencies of the role to allow ease of use. All of these modules can be found in the [library](./library) and the [module_utils](./module_utils) directories.

## Author

* Kirikae <kirikae@cs-network.org>
