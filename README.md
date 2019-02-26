Vagrantfile and salt-module to illustrate [saltstack/salt#51578](https://github.com/saltstack/salt/issues/51578) on various distibutions.

Steps to reproduce:
  * clone this repository
  * `vagrant up bionic` (replace bionic with desired distro: trusty, xeniail, bionic, jessie or stretch)
  * `vagrant ssh bionic`
  * `systemctl restart salt-master` (restart to ensure not already poisoned)
  * execute `salt-call pillar.items` (will output external pillar provider data)
  * execute `salt-call pillar.items` (second invocation will omit extneral pillars)
