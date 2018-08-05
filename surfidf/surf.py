import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from ovito.io import import_file
from ovito.data import SurfaceMesh, SimulationCell
from ovito.modifiers import ConstructSurfaceModifier
import time

time_start=time.time()
# import file
pipeline = import_file("source/dtest.*.dump")
print("%s frame(s) in all" %pipeline.source.num_frames)
# create list stepstr to save frame output
cdt= [];
#inti = frame+10
for frame in range(0,pipeline.source.num_frames,1):
    pipeline.modifiers.append(ConstructSurfaceModifier(radius=2.9))
    data = pipeline.compute(frame)
    data.expect(SurfaceMesh)
    cell = data.expect(SimulationCell)
    print("Surface area: %f" % data.attributes['ConstructSurfaceMesh.surface_area'])
    print("Solid volume: %f" % data.attributes['ConstructSurfaceMesh.solid_volume'])
    fraction = data.attributes['ConstructSurfaceMesh.solid_volume'] / cell.volume
    print("Solid volume fraction: %f" % fraction)
    cmp = frame+1;
    print('frame %s of %s complete' %(cmp,pipeline.source.num_frames))
# convert list to numpy.array for plot and output
    cdt.append(data.attributes['ConstructSurfaceMesh.surface_area'])
surfid = array(cdt)

np.savetxt("surface.txt", surfid, fmt="%2.3f", delimiter=" ")
print('OVER ! └(^o^)┘ ')
time_end=time.time()
print('totally cost',time_end-time_start)
pxx = range(np.size(surfid))
plt.plot(pxx, surfid)
plt.savefig('surface.pdf')


