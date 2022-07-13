import os
import paramiko
import numpy as np
from scipy import signal
from scipy import ndimage as nmg
from PIL import ImageFilter
import matplotlib.pyplot as plt
os.chdir(os.path.dirname(__file__))
# setup SSH


# setup SFTP
transport = paramiko.Transport(('00000', 0000))
transport.connect(username='0000', password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='124.152.228.80', port=10000, username='LUTRuizy', password='123456')
sftp.put('RemoteBin.py', '/public1/home/LUTRuizy/RemoteBin.py')

framlist = [2,100,150,160,170,180]
for frame in framlist:
     # process parameters
    pos = 'ia'
    size = '15'
    width = 5
    ssh_client.exec_command('ovitos RemoteBin.py %s %s %s %d'%(frame,pos,size,width))
    # optional: stdin,stdout,stderr=ssh_client.exec_command('ls')
    sftp.get('/public1/home/LUTRuizy/sz/%ssz/sz%s/cont/cont%s.txt'%(pos,size,frame),'pltdata/data/cont%s.txt'%frame)
    # full path: /home/alex/Documents/HyPost/strecont/pltdata/data/pdata125.txt
    # close SSH/SFTP

    # load data
    u = np.loadtxt('pltdata/data/cont%s.txt'%frame)
    #domain = np.identity(9)
    #v = signal.spline_filter(u,15)
    v = nmg.filters.gaussian_filter(u,1)/10e5
    # w = u.filter(ImageFilter.BLUR)

    # full path: /pltda/home/alex/Documents/HyPost/strecont/pltdata/data/cont125.txtta/data/cont125.txt
    plx = 2*np.linspace(0,v.shape[0],v.shape[0])
    ply = 2*np.linspace(0,v.shape[1],v.shape[1])
    ply = 2*np.linspace(0,v.shape[1],v.shape[1])
    px, py = np.meshgrid(ply,plx)
    lineplot = plt.contour(px,py,v,5,linewidths=2,colors='w')
    fillplot = plt.contourf(px,py,v,5,alpha=1,cmap="coolwarm")
    plt.axis('equal')

    # RdBu_r
    rg = np.linspace(0,5,10)
    # plt.set_zlim(zmax=5e6)

    # cmap=plt.cm.jet
    # plt.linewidth=1.5 alpha=1,
    # plt.title('frame:%s  position:%s  size:%s'%(frame,pos,size))
    # plt.colorbar(ticks=rg, orientation='vertical')# lorbar()
    plt.savefig('pltdata/fig/%s-%s-%s.pdf'%(pos,size,frame))
    plt.show()

transport.close()
ssh_client.close()
#plt.savefig('pltdata/fig/%s-%s-%s.pdf'%(pos,size,frame))

