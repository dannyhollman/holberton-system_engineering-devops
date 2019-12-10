# kills process named killmenow
exec { 'kill process' :
  command  => 'pkill killmenow',
  provider => 'shell',
}
