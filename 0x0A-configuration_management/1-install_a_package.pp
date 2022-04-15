# Using Puppet, install puppet-lint
package { 'puppet-lint':
  name   => 'puppet-lint',
  ensure => '2.5.0',
}
