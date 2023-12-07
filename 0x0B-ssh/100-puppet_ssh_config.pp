# configure to use a specific private key and signin without password
file ('/home/was/.ssh/ssh_config'):
    ensure => 'file',
    owner => 'ubuntu',
    group => 'ubuntu',
    mode => '0600',
    content =>"
    Host 54.174.27.176,
    IdentityFile ~/.ssh/school/
    PasswordAuthetication no
    ",
}
