# install puppet-lint -v 2.5.0

exec { 'puppet-lint':
    command => '/usr/bin/apt install -y puppet-lint -v 2.5.0',
}
