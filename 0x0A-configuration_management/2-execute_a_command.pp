# Create a manifest that kills a process named killmenow
exec {'execute command':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
