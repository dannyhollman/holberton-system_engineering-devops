exec { 'removeLimit':
  command => "/bin/sed -i 's/5/20000/g' /etc/default/nginx; sudo service nginx restart"
}
