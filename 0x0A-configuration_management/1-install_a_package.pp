# install flask 2.1.0 using pip3

exec { 'puppet-lint':
    command => '/usr/local/bin/pip3 install flask==2.1.0',
}
