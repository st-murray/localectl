[![Build Status](https://travis-ci.org/oasis-roles/localectl.svg?branch=master)](https://travis-ci.org/oasis-roles/localectl)

localectl
===========

Set system LANG locale and keyboard layout settings using localectl

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `localectl_locale` - Set this value to the desired language System locale designation for your system.
At this time only the LANG or language designation is supported. (required)                

* `localectl_keymap` - Set this value to desired VC Keymap designation for your system. (required)

* `localectl_x11_keymap` Set this value to the desired X11 Layout designation for your system. (required)

* `localectl_become` - Defaults to 'true'.  Whether or not to use the `become` feature of Ansible to gain admin privileges.`

* `localectl_become_user` - Defaults to 'root'.  The user to sudo/become


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: localectl-servers
  roles:
    - role: oasis-roles.localectl
      localectl_locale: en_US.UTF-8
      localectl_keymap: us
      localectl_x11_keymap: us
```

License
-------

GPLv3

Author Information
------------------

Steve Murray <stmurray@redhat.com>
