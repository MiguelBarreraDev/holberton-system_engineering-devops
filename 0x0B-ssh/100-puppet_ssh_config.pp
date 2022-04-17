# Script - Modify config file
# Update the path of the private key to identify us
file_line { 'config_IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/school',
}
# Update mode of authentication
file_line { 'config_PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no',
}
