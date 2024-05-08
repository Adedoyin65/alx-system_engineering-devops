# This puppet file automates to reset apache to return a webpage

# Define an exec resource to run strace on the Apache process
exec { 'strace_apache':
  command     => 'strace -o /tmp/apache_strace.txt -f -s 1000 -p $(pgrep apache2)',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

# Define an exec resource to fix the issue based on the strace output
exec { 'fix_apache_issue':
  command     => 'sed -i "s/display_errors = Off/display_errors = On/" /etc/php/5.5/apache2/php.ini',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  notify      => Exec['restart_apache'],
}

# Define an exec resource to restart Apache after fixing the issue
exec { 'restart_apache':
  command     => 'service apache2 restart',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

# Notify the restart_apache exec resource when the fix_apache_issue exec resource is executed
Exec['fix_apache_issue'] -> Exec['restart_apache']
