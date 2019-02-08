import numpy as np
import matplotlib.pyplot as plt
# import imageio as imio
import time
T1 = time.time()
N = 14
ScalFact = 1.25
images = []


for Deg in [1, 5, 10, 15, 16.26, 20, 22.62, 25, 28.07, 30, 35, 36.86, 40, 43.6, 45]:
    RtAng = np.deg2rad(Deg)
    RtMtr = np.array([[np.cos(RtAng), -np.sin(RtAng)], [np.sin(RtAng), np.cos(RtAng)]])
    frame = np.linspace(0, N, N+1)
    SupCell = np.meshgrid(frame, frame)
    CellX = np.reshape(SupCell[0], np.size(SupCell[0]), 1)
    CellY = np.reshape(SupCell[1], np.size(SupCell[1]), 1)
    Cell = np.array([CellX, CellY])
    MovedCell = Cell.transpose()
    CellR = np.dot(RtMtr, Cell)
    Cent = int(np.round(N/2))
    Offset = np.dot(RtMtr,[Cent, Cent])
    Px = CellR[0, :]+(Cent-Offset[0])
    Py = CellR[1, :]-(Offset[1]-Cent)

    CSLx = Px[np.where(np.sqrt(abs(np.round(Px)-Px)**2+abs(np.round(Py)-Py)**2) <= 0.001)]
    CSLy = Py[np.where(np.sqrt(abs(np.round(Px)-Px)**2+abs(np.round(Py)-Py)**2) <= 0.001)]

    plt.rcParams['figure.figsize'] = (6, 6)
    plt.scatter(MovedCell[:, 0], MovedCell[:, 1], label='Original', color='gray', alpha=0.8,marker='s')
    plt.scatter(Px, Py, marker='o', label='Rotated', color='lightblue', alpha=0.8,)
    plt.grid(True, linestyle="--", color="black", linewidth="0.5")
    plt.xticks(np.linspace(-Cent, 3*Cent, 4*Cent+1))
    plt.yticks(np.linspace(-Cent, 3*Cent, 4*Cent+1))
    plt.xlabel('X')
    plt.ylabel('Y')
    Couple = np.intersect1d(CSLx, CSLy)
    vtest = np.array([CSLx, CSLy])
    # plt.scatter(Cent, Cent, color='r', marker='*')

    plt.scatter(CSLx, CSLy, marker='o', color='firebrick', label='CSL')
    plt.xlim(int(-0.6*Cent), int(2.5*Cent))
    plt.ylim(int(-0.6*Cent), int(2.5*Cent))
    sig = (CSLx-Cent)**2+(CSLy-Cent)**2
    if sig.any():
        if int(round(np.min(sig[np.nonzero(np.round(sig))]))):
            Sigma = int(round(np.min(sig[np.nonzero(np.round(sig))])))
            plt.text(-2.5, 1.15*max(frame), r'$ \Sigma=%s$ Rotate %s$^{o}$'%(Sigma, Deg),
                 color='darkblue', bbox=dict(facecolor='white', alpha=0.85, boxstyle="round"))
            plt.text(-2.5, -3.5,'by Mao', color='gray')
            plt.legend(frameon=True,loc=4)
            plt.tight_layout()
            plt.savefig('pic/Deg-%s.png'%Deg, dpi=200)
            plt.show()
            plt.close('all')
            # images.append(imio.imread('pic/Deg-%s.png'%Deg))
            print('Rotate 	%s 	degree	Sigma	%s' % (Deg, Sigma))

    else:
        Sigma = 'None'
        plt.text(-2.5, -3.5, 'by Mao', color='gray')
        plt.text(-2.5, 1.15*max(frame), r'$ \Sigma= None$ Rotate %s$^{o}$ ' % Deg,
                 color='darkblue', bbox=dict(facecolor='white', alpha=0.85, boxstyle="round"))
        p2 = plt.savefig('pic/Deg-%s.png'%Deg)
        plt.legend(frameon=True, loc=4)
        plt.tight_layout()
        plt.savefig('pic/Deg-%s.png' % Deg, dpi=200)
        plt.show()
        plt.close('all')
        # images.append(imio.imread('pic/Deg-%s.png' % Deg))
        print('Rotate	%s	degree	Sigma	%s' %(Deg,Sigma))
# imio.mimsave('pic/CSL.gif', images, duration=2.5)
T2 = time.time()

print('All Done!  %s Seconds'%round(T2-T1))



