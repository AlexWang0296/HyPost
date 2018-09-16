import os.path
import numpy as np
import matplotlib.pyplot as plt
from ovito.io import import_file
from os import listdir
from ovito.modifiers import SliceModifier
from ovito.modifiers import BinAndReduceModifier
from ovito.data import SimulationCell
pos = 'ia'
size = '2'
frame = 1
#os.chdir(os.path.join('sz','%ssz'%pos,'sz%s'%size))
dirlist = listdir()
#print('Scaning dir: %s' %dirlist)
pipeline = import_file('/home/alex/Documents/HyPost/source/dtest.*.dump')
stepstr = []
#for frame in range(pipeline.source.num_frames):
# print("Hello, this is OVITO %i.%i.%i" % ovito.
print("%s %s" %(pos,size))
# yslice = SliceModifier(normal=(0, 1, 0), slab_w
# slice z
zslice = SliceModifier(normal=(0, 0, 1), slab_width=15)
# apply modifiers to pipeline
# pipeline.modifiers.append(yslice)
pipeline.modifiers.append(zslice)
binmdf = BinAndReduceModifier()
cell = pipeline.compute().expect(SimulationCell)
binmdf.bin_count_x = 100
binmdf.bin_count_y = 100
binmdf.property = "c_c"
binmdf.direction = BinAndReduceModifier.Direction.Vectors_1_2
binmdf.reduction_operation = BinAndReduceModifier.Operation.Mean
pipeline.modifiers.append(binmdf)
pipeline.compute()
mean_stre_x = binmdf.bin_data
gg = mean_stre_x.tolist()
stepstr.append(gg)
np.savetxt("%d.txt"%frame, mean_stre_x, fmt="%2.3f", delimiter=" ")
plx = np.linspace(0,100,100)
ply = np.linspace(0,100,100)
px, py = np.meshgrid(plx,ply)
plt.contourf(px,py,mean_stre_x,5,alpha=1,cmap="RdBu_r")
print('over')
os.chdir('../../..')

#




