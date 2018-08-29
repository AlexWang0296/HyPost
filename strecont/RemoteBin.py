import os.path
import sys
import numpy as np
from ovito.io import import_file
from os import listdir
from ovito.modifiers import SliceModifier
from ovito.modifiers import BinAndReduceModifier

pos = sys.argv[2]
size = sys.argv[3]
frame = sys.argv[1]
width = int(eval(sys.argv[4]))

os.chdir(os.path.join('sz','%ssz'%pos,'sz%s'%size))
dirlist = listdir()
framelist = []
for i in dirlist:
    if os.path.splitext(i)[1] == ".cfg":
#        print('%s found' %i)
        framelist.append(i)
print('%s frames in all'%np.size(framelist))
      # .append(os.path.splitext(i)[0])
# print(dirlist)
# frame = input('which frame?\n')
pipeline = import_file(framelist[int(frame)])
stepstr = []
#for frame in range(pipeline.source.num_frames):
# print("Hello, this is OVITO %i.%i.%i" % ovito.
# print("%s %s" %(pos,size))
# yslice = SliceModifier(normal=(0, 1, 0), slab_w
# slice z
zslice = SliceModifier(normal=(0, 0, 1), slab_width = width)
# apply modifiers to pipeline
# pipeline.modifiers.append(yslice)
pipeline.modifiers.append(zslice)
binmdf = BinAndReduceModifier()
binmdf.bin_count_x = 100
binmdf.bin_count_y = 100
binmdf.property = "v_ES"
binmdf.direction = BinAndReduceModifier.Direction.Vectors_1_2
binmdf.reduction_operation = BinAndReduceModifier.Operation.Max
pipeline.modifiers.append(binmdf)
pipeline.compute()
bprop = binmdf.bin_data
gg = bprop.tolist()
stepstr.append(gg)
np.savetxt("cont/cont%s.txt"%frame, bprop, fmt="%2.3f", delimiter=" ")
print('%s %s %s over'%(frame,pos,size))
os.chdir('../../..')



