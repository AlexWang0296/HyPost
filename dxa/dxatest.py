import os
import numpy as np
import ovito
import matplotlib.pyplot as plt
#from numpy import array
from ovito.io import import_file
from ovito.modifiers import DislocationAnalysisModifier
from ovito.data import SurfaceMesh, SimulationCellimport time
print(os.path.abspath(__file__))
time_start = time.time()
# import file
fpath  = '/media/alex/HDD/post/ag/g-ag-300-opt/dump.*.cfg'
pgap = 100
# /media/alex/HDD/post/ag/g-ag-300-opt/dump.*.cfg
# 'source/dtest.*.dump'
pipeline = import_file(fpath)
print("%s frame(s) in all \nframe area vol vol_fraction" %pipeline.source.num_frames)
# create list stepstr to save frame output
lenlist = []
denlist = []
#inti = frame+10
frame = 1
pipeline.modifiers.append(ovito.modifiers.DislocationAnalysisModifier())
data = pipeline.compute(frame)
cell = data.expect(SimulationCell)
disdens = data.attributes['DislocationAnalysis.total_line_length'] / cell.volume
lenlist.append(data.attributes['DislocationAnalysis.total_line_length'])
denlist.append(disdens)
print("%s/%s %f %f" %(frame, pipeline.source.num_frames,data.attributes['DislocationAnalysis.total_line_length'], disdens))


