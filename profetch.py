import numpy as np
from numpy import array
from ovito.io import import_file
from ovito.modifiers import SliceModifier
from ovito.modifiers import BinAndReduceModifier
# import file
pipeline = import_file("/PATH/TO/File")
# create list stepstr to save frame output
# file name format: "100.*.lammpstrj"/"100.*.gin"
stepstr = [];
for frame in range(pipeline.source.num_frames):
    # slice y
    yslice = SliceModifier(normal=(0, 1, 0), slab_width=10)

    # slice z
    zslice = SliceModifier(normal=(0, 0, 1), slab_width=10)

    # apply modifiers to pipeline
    pipeline.modifiers.append(yslice)
    pipeline.modifiers.append(zslice)
    # config BinAndReduceModifier
    binmdf = BinAndReduceModifier()
    binmdf.bin_count_x = 100
    binmdf.bin_count_y = 100
    binmdf.property = "c_s_1"
    binmdf.direction = BinAndReduceModifier.Direction.Vector_1
    binmdf.reduction_operation = BinAndReduceModifier.Operation.Mean
    pipeline.modifiers.append(binmdf)
    pipeline.compute(frame)
    # save frame data to temp list gg
    gg = binmdf.bin_data.tolist()
    # save all data to list gg
    stepstr.append(gg)
    print('frame %s of %s complete' %(frame,pipeline.source.num_frames))
# convert list to numpy.array for plot and output
output = array(stepstr)
np.savetxt("processed.txt", output, fmt="%2.3f", delimiter=" ")
print('OVER ! ')
