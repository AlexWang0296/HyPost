import os
import numpy as np
import matplotlib.pyplot as plt
#from numpy import array
from ovito.io import import_file
from ovito.data import SurfaceMesh, SimulationCell
from ovito.modifiers import ConstructSurfaceModifier
import time
print(os.path.abspath(__file__))
time_start = time.time()
# import file
pipeline = import_file('source/dtest.*.dump')
print("%s frame(s) in all \nframe area vol vol_fraction" %pipeline.source.num_frames)
# create list stepstr to save frame output
cdt = []
#inti = frame+10
for frame in range(0, pipeline.source.num_frames, 1):
    pipeline.modifiers.append(ConstructSurfaceModifier(radius=2.9))
    data = pipeline.compute(frame)
    data.expect(SurfaceMesh)
    cell = data.expect(SimulationCell)
    fraction = data.attributes['ConstructSurfaceMesh.solid_volume'] / cell.volume
    cdt.append(data.attributes['ConstructSurfaceMesh.surface_area'])

    print("%s/%s %f %f %f" %(frame, pipeline.source.num_frames, \
                             data.attributes['ConstructSurfaceMesh.surface_area'], \
                             data.attributes['ConstructSurfaceMesh.solid_volume'], \
                             fraction))
time_end = time.time()
tsp = time_end - time_start
print('OVER in %f ! ^o^ ' %tsp)

# convert list to numpy.array for plot and output
surfid = np.array(cdt)
np.savetxt("surface.txt", surfid, fmt="%2.3f", delimiter=" ")
pxx = range(len(surfid))
plt.plot(pxx, surfid)
plt.show()

plt.savefig('cracksurface.pdf')


