import paramiko
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
# setup SSH
transport = paramiko.Transport(('124.152.228.80', 10000))
transport.connect(username='LUTRuizy', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)

# setup SFTP
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='124.152.228.80', port=10000, username='LUTRuizy', password='123456')
# process parameters
frame = 2
pos = 'ag'
size = '15'
width = 5
sftp.put('RemoteBin.py','/public1/home/LUTRuizy/RemoteBin.py')
ssh_client.exec_command('ovitos RemoteBin.py %s %s %s %d'%(frame,pos,size,width))
# optional: stdin,stdout,stderr=ssh_client.exec_command('ls')
sftp.get('/public1/home/LUTRuizy/sz/%ssz/sz%s/cont/cont%s.txt'%(pos,size,frame),'pltdata/data/cont%s.txt'%frame)
# full path: /home/alex/Documents/HyPost/strecont/pltdata/data/pdata125.txt
# close SSH/SFTP
transport.close()
ssh_client.close()
# load data
u = np.loadtxt('pltdata/data/cont%s.txt'%frame)
v = signal.spline_filter(u,lmbda=1.5)
# full path: /pltda/home/alex/Documents/HyPost/strecont/pltdata/data/cont125.txtta/data/cont125.txt
plx = np.linspace(0,100,100)
ply = np.linspace(0,100,100)
px, py = np.meshgrid(plx,ply)
plt.contourf(px,py,v,5,alpha=0.8,cmap="RdBu_r")
# cmap=plt.cm.je
# plt.linewidth=1.5 alpha=1,
plt.title('frame:%s position:%s size:%s'%(frame,pos,size))
plt.colorbar()# lorbar()
plt.savefig('pltdata/fig/%s-%s-%s.png'%(pos,size,frame))
plt.show()
