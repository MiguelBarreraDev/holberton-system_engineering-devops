-> exec { 'typo':
  command => 'sed -i "s/phpp/php" /var/www/html/wp-settings.php'
}
-> exec { 'Reload Service':
  command => 'service apache2 reload'
}
