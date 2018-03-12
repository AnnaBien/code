#!/usr/bin/env python

import os
import sys
import paramiko


if len(sys.argv) == 2:
    command = 'scp -r abien@pluton.kt.agh.edu.pl:/home/gozdecki/PS_2018/' + sys.argv[1] + ' .'
    os.system(command)
    sys.exit(0)

files = os.listdir('.')
download = []
nothing = True

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect('pluton.kt.agh.edu.pl', port=22, username='abien', password='tajnehaslo')

    stdin, stdout, stderr = client.exec_command('ls /home/gozdecki/PS_2018')
    download = stdout.read().split('\n')
    download.remove('')

    for f in download:
        if f not in files:
            nothing = False
            print('Downloading ' + str(f))
            command = 'scp -r abien@pluton.kt.agh.edu.pl:/home/gozdecki/PS_2018/' + f + ' .'
            os.system(command)
    if(nothing):
        print("Nothing new to download")

finally:
    client.close()
