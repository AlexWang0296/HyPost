import paramiko

transport = paramiko.Transport(('202.201.35.13',22))
transport.connect(username='root',password='1')
sftp = paramiko.SFTPClient.from_transport(transport)
#将resutl.txt 上传至服务器 /tmp/result.txt
#sftp.put('~/resutl.txt','/tmp/result.txt')
#将result.txt 下载到本地
sftp.get('/root/home/nohup.out','get.txt')
transport.close()