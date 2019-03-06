import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
LW = np.loadtxt('LenCra.txt')
px = np.linspace(0, 1, len(LW))
Lfit = np.poly1d(np.polyfit(px, LW[:, 1], 4))
# def func_powerlaw(x,)
# ydata = fit.(func_powerlaw, x, y)
py = Lfit(px)
plt.plot(px, py)
plt.scatter(px, LW[:, 1], marker ='o', color='firebrick')
plt.show()