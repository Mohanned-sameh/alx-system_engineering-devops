# Install flask

package { 'flask':
    ensure => present,
  provider => 'pip'
}
