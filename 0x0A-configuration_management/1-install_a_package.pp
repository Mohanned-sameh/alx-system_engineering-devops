# Install an especific version of flask (2.1.0) in puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
