# 输出为LAMMPS建模格式

import numpy as np


def rotcell(rotang):
    cellvect = [[1, 0], [0, 1]]
    rotang = np.deg2rad(rotang)
    rotmat = np.array([[np.cos(rotang), -np.sin(rotang)], [np.sin(rotang), np.cos(rotang)]])  # 二维旋转矩阵
    cellr = np.dot(rotmat, cellvect)  # 对初始晶胞进行旋转
    return(cellr)


for u in [1, 5, 10, 15, 16.26, 20, 22.62, 25, 28.07, 30, 35, 36.86, 40, 43.6, 45]:
    print(u)
    print(rotcell(u/2))
    print(rotcell(-u/2))

