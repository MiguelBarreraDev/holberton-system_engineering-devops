# Add a custom HTTP header with Puppet
exec {'upgrade_package':
  provider => shell,
  command  => 'sudo apt-get -y upgrade',
  before   => Exec['update_packages'],
}

exec {'update_packages':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install_nginx'],
}

exec {'install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header']
}

exec {'add_header':
  provider    => 'shell',
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/^server\s{/server {\n\tadd_header X-Served-By $HOSTNAME;/1" /etc/nginx/sites-available/default',
  before      => Exec['restart_nginx_service']
}

exec {'restart_nginx_service':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
