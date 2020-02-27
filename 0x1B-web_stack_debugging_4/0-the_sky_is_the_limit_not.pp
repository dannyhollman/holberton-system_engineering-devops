exec { 'removeLimit':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx; sudo /usr/bin/service nginx restart"
}
