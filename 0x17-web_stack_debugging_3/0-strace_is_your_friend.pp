# fix to why Apache is returning a 500 error
exec { 'fix typo':
  onlyif  => 'test -e /var/www/html/wp-settings.php',
  command => 'sed -i "s/phpp/php" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin',
}
