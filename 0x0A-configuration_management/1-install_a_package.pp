# install flask 2.1.0 using pip3

exec { 'install_flask':
	command => '/usr/local/bin/pip3 install flask==2.1.0',
}
