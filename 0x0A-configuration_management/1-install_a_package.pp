# Install an especific version of flask (2.1.0) in puppet

exec { 'install_flask':
  command => 'pip install flask==2.1.0',
  path    => '/usr/local/bin',
  creates => '/usr/local/bin/flask',
  require => Package['python3-pip'],
}
