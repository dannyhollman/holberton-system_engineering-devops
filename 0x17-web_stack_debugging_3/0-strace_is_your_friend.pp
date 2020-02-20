# fix typo with puppet

exec { 'typo':
  command => "/bin/sed -i \'s/phpp/php/\' /var/www/html/wp-settings.php"
}
