import os.path
import sys
import numpy as np
from ovito.io import import_file
from os import listdir
from ovito.modifiers import SliceModifier
from ovito.modifiers import BinAndReduceModifier
from ovito.data import SimulationCell
frame = '0'
offset = '1'
width = '10'
subdir = ['1k','298k','498k','698k','898k','1100k']
#wkdir = os.path.join()
#/media/alex/HDD2/shock-temp/1k
#/media/alex/HDD2/shock-temp/298k
#/media/alex/HDD2/shock-temp/498k
#/media/alex/HDD2/shock-temp/698k
#/media/alex/HDD2/shock-temp/898k
#/media/alex/HDD2/shock-temp/1100k
os.chdir(os.path.dirname(__file__))
os.chdir(os.path.join('..','source'))
print(os.path.dirname(__file__))


ppl = import_file('dtest.*.dump') # 导入文件
cell = ppl.compute().expect(SimulationCell) # 获取cell几何信息

MdfBin = BinAndReduceModifier() # 定义Bin and Reduce Modifier
L = int(cell[2,2])
MdfBin.property = 'c_c'
MdfBin.bin_count_x = L #
MdfBin.direction = BinAndReduceModifier.Direction.Vector_3
MdfBin.reduction_operation = BinAndReduceModifier.Operation.Max
ppl.modifiers.append(MdfBin)
ppl.compute()
prop = MdfBin.bin_data

import matplotlib.pyplot as plt
px = np.linspace(0,L,L)
plt.plot(px,prop)
plt.show()

