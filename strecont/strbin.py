import ovito
from ovito.io import export_file
from numpy import array

import numpy as np
from ovito.io import import_file
import os.path
import matplotlib.pyplot as plt

WDIR = os.path.dirname(__file__)
source = os.path.join(WDIR,'..','source')

pipeline = import_file(os.path.join(source,'dtest.1.dump'))
stepstr = [];
for frame in range(pipeline.source.num_frames):
    # print("Hello, this is OVITO %i.%i.%i" % ovito.version)
    from ovito.modifiers import SliceModifier
    from ovito.modifiers import BinAndReduceModifier

    # slice y
    # yslice = SliceModifier(normal=(0, 1, 0), slab_width=10)

    # slice z
    zslice = SliceModifier(normal=(0, 0, 1), slab_width=15)

    # apply modifiers to pipeline
    # pipeline.modifiers.append(yslice)
    pipeline.modifiers.append(zslice)

    binmdf = BinAndReduceModifier()
    binmdf.bin_count_x = 100
    binmdf.bin_count_y = 100
    binmdf.property = "c_c"
    binmdf.direction = BinAndReduceModifier.Direction.Vectors_1_2
    binmdf.reduction_operation = BinAndReduceModifier.Operation.Mean
    pipeline.modifiers.append(binmdf)
    pipeline.compute(frame)
    mean_stre_x = binmdf.bin_data
    gg = mean_stre_x.tolist()
    # print(gg[50])
    # print(mean_stre_x[50])
    stepstr.append(gg)
    print(frame)
    #stepstr.append(mean_stre_x)
    #print(pipeline.source.num_frames)
    #plt.savefig("examples.jpg")
    plt.savefig('%s.png' %frame)
plx = np.linspace(0,100,100)
ply = np.linspace(0,100,100)
px, py = np.meshgrid(plx,ply)
plt.contourf(px,py,mean_stre_x,10,alpha=1,cmap=plt.cm.jet)
plt.colorbar()
plt.show()
# '%s.csv' % name, 'wb'
# print(stepstr)
# stepstrline = array(stepstr)
# export_file(pipeline, "outputfile.dump","lammps/dump", columns = ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z"],multiple_frames = True)
# print(pipeline.source.num_frames)
# ub = array(stepstr)
# for fig in range(0,len(ub)):
    # pxx = np.linspace(0, 10, 100)
    # pxx = np.linspace(binmdf.axis_range_x[0], binmdf.axis_range_x[1], np.size(mean_stre_x))
    # plt.plot(pxx, ub[fig])
    # plt.savefig('%s.png' %fig)




