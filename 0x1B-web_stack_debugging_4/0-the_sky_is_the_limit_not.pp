exec { 'removeLimit':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sudo sed -i 's/15/20000/g' /etc/default/nginx; sudo service nginx restart",
}
