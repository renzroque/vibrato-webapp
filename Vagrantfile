# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.define "vibrato-app" do |h|
    h.vm.network "private_network", ip: "192.168.135.20"
    h.vm.provision :shell, inline: <<-SHELL
    
    wget -qO- https://get.docker.com/ | sh
    sudo apt-get -y install python-pip
    sudo pip install docker-compose

    chmod u+x /vagrant/start-webapp.sh
    cd /vagrant
    sudo ./start-webapp.sh

    SHELL
  end
end