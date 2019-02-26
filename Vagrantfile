SALT_VERSION="2018.3"

SHELL_SCRIPT = <<SCRIPT
OSCODENAME=$(lsb_release -cs)
DISTRO=$(lsb_release -is);
DISTRO=${DISTRO,,}
VARIANT=$(lsb_release -rs)

apt-get install apt-transport-https
APT_URL="https://repo.saltstack.com/apt/${DISTRO}/${VARIANT}/amd64/#{SALT_VERSION}"
mkdir -p /etc/salt/pki
cp /vagrant/salt/{minion,master} /etc/salt/.
cp -r /vagrant/salt/pki/* /etc/salt/pki/.
chown root: -R /etc/salt/pki
apt-key adv --fetch-keys ${APT_URL}/SALTSTACK-GPG-KEY.pub
echo "deb ${APT_URL} ${OSCODENAME} main" > /etc/apt/sources.list.d/saltstack.list
apt-get update
apt-get -o Dpkg::Options::="--force-confold" -y install salt-minion salt-master
SCRIPT

Vagrant.configure("2") do |config|

  # UBUNTU
  ## trusty
  config.vm.define "trusty", autostart: false do |distro|
    distro.vm.box = "ubuntu/trusty64"
    distro.vm.box_url = "https://app.vagrantup.com/ubuntu/boxes/trusty64"
  end

  ## xenial
  config.vm.define "xenial", autostart: false do |distro|
    distro.vm.box = "ubuntu/xenial64"
    distro.vm.box_url = "https://app.vagrantup.com/ubuntu/boxes/xenail64"
  end

  ## bionic
  config.vm.define "bionic", autostart: false do |distro|
    distro.vm.box = "ubuntu/bionic64"
    distro.vm.box_url = "https://app.vagrantup.com/ubuntu/boxes/bionic64"
  end
  # END UBUNTU

  # DEBIAN
  ## stretch
  config.vm.define "jessie", autostart: false do |distro|
    distro.vm.box = "debian/contrib-jessie64"
    distro.vm.box_url = "https://app.vagrantup.com/debian/boxes/contrib-jessie64"
  end

  ## stretch
  config.vm.define "stretch", autostart: false do |distro|
    distro.vm.box = "debian/contrib-stretch64"
    distro.vm.box_url = "https://app.vagrantup.com/debian/boxes/contrib-stretch64"
  end
  # END DEBIAN

  config.vm.synced_folder "salt", "/srv/salt"

  config.vm.provision "shell",
    run: "once",
    inline: SHELL_SCRIPT

end
