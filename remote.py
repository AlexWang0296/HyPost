import paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='202.201.35.13', username='root', password='1')
stdin,stdout,stderr=ssh_client.exec_command('ls')
print(stdout.readlines())
