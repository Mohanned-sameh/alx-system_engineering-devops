# creates a file with the content "I Love Puppet"
# in /tmp/school

file { '/tmp/school':
  content => 'I Love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
