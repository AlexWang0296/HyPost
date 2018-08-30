import os
import ovito
import numpy as np
from ovito.io import import_file
from ovito.modifiers import DislocationAnalysisModifier
from ovito.data import SurfaceMesh, SimulationCell
from ovito.modifiers import ConstructSurfaceModifier
from ovito.data import SimulationCell
import time
print(os.path.abspath(__file__))
time_start = time.time()
# import file
fpath  = input("Path to Source File:\n")
label = fpath.split('/')[1]
#label = slice(fpath)[]
pgap = int(input("Process every N Step:\n"))
# /media/alex/HDD/post/ag/g-ag-300-opt/dump.*.cfg
# 'source/dtest.*.dump'
pipeline = import_file(fpath)
print("%s frame(s) in all \nframe area vol vol_fraction" %pipeline.source.num_frames)
# create list stepstr to save frame output
lenlist = []
denlist = []
#inti = frame+10
for frame in range(0, pipeline.source.num_frames, pgap):
    pipeline.modifiers.append(ConstructSurfaceModifier(radius=2.9))
    pipeline.modifiers.append(ovito.modifiers.DislocationAnalysisModifier())
    data = pipeline.compute(frame)
    vsolid = data.attributes['ConstructSurfaceMesh.solid_volume']
    cell = data.expect(SimulationCell)
    fraction = data.attributes['DislocationAnalysis.total_line_length'] / vsolid
    with open('Dis_den_%s.txt'%label,'a+') as txt1:
        txt1.writelines('%f\n'%data.attributes['DislocationAnalysis.total_line_length'])
    lenlist.append(data.attributes['DislocationAnalysis.total_line_length'])
    with open('Dis_len%s.txt'%label,'a+') as txt2:
        txt2.writelines('%f\n'%fraction)
    denlist.append(fraction)
    print("%s/%s %f  %f" %(frame, pipeline.source.num_frames,data.attributes['DislocationAnalysis.total_line_length'],fraction))
time_end = time.time()
tsp = time_end - time_start
print('OVER in %f ! ^o^ ' %tsp)

# convert list to numpy.array for plot and output
dislength = np.array(lenlist)
disdens = np.array(denlist)
# np.savetxt("Dis_length.txt", dislength, fmt="%2.3f", delimiter=" ")
# np.savetxt("Dis_density.txt", disdens, fmt="%2.3f", delimiter=" ")

#pxx = range(len(dislength))
#plt.plot(pxx, dislength)
#plt.show()
#plt.savefig('CrackSurface.pdf')


