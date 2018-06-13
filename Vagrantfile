Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.define "master" do |master|
    master.vm.hostname = "master.local" 
    master.vm.network "private_network", type: "dhcp"
  end 

  config.vm.define "node1" do |node1|
     node1.vm.hostname = "node1.local" 
     node1.vm.network "private_network", type: "dhcp" 
  end 

  config.vm.define "node2" do |node2|
    node2.vm.hostname = "node2.local" 
    node2.vm.network "private_network", type: "dhcp" 
  end  
  config.vm.provision "ansible" do |ansible|
    ansible.inventory_path = "hosts.yml"
    ansible.verbose = "true"
    ansible.playbook = "CreateKeys.yml"
  end
  
  
    
  
end 
