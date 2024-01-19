# kill proccess killmenow

exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep -f killmenow',
}
