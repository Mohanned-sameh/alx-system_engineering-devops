# changes to config file 

file { '/home/mohanned/.ssh/config':
  ensure => present,
  content => "
    Host server
    HostName <server_hostname>
    User <username>
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
