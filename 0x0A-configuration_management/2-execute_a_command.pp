# executes the pkill command

exec {'perocesskiller':
    command => '/usr/bin/pkill killmenow',
}
