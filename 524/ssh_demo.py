#!/usr/bin/env python

import paramiko
import sys
cmd = sys.argv[1]

HOST = '192.168.1.170'

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#s.connect('192.168.1.170',22,'root','root',timeout=5)

key_file = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(key_file)
s.connect('192.168.1.170',22,'root',timeout=5)
stdin,stdout,stderr = s.exec_command(cmd)

cmd_result = stdout.read(),stderr.read()

for line in cmd_result:
    print line
s.close()

t = paramiko.Transport((HOST,22))
t.connect(username='root',password='root')
sftp =paramiko.SFTPClient.from_transport(t)
#stftp.get('ll','')
sftp.put('/tmp/kel.txt','/tmp/kel.txt')
t.close()
