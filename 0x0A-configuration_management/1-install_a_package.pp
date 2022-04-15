# Using Puppet, install puppet-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  name     => 'puppet-lint',
  provider => 'gem',
  source   => 'https://rubygems.org',
}
