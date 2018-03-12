#!/usr/bin/env python

import os
import sys
import paramiko


if len(sys.argv) == 2:
    command = 'scp -r login@server:path' + sys.argv[1] + ' .'
    os.system(command)
    sys.exit(0)

files = os.listdir('.')
download = []
nothing = True

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect('server', port=22, username='login', password='password')

    stdin, stdout, stderr = client.exec_command('ls path')
    download = stdout.read().split('\n')
    download.remove('')

    for f in download:
        if f not in files:
            nothing = False
            print('Downloading ' + str(f))
            command = 'scp -r login@server:path' + f + ' .'
            os.system(command)
    if(nothing):
        print("Nothing new to download")

finally:
    client.close()
