#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
def height(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
x=np.linspace(-3,3,300)
y=np.linspace(-3,3,300)
X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,height(X,Y),10,alpha=0.75,cmap=plt.cm.hot)
#为等高线填充颜色 10表示按照高度分成10层 alpha表示透明度 cmap表示渐变标准
C=plt.contour(X,Y,height(X,Y),10,colors='black')
#使用contour绘制等高线
plt.clabel(C,inline=True,fontsize=10)
#在等高线处添加数字
plt.xticks(())
plt.yticks(())
#去掉坐标轴刻度
plt.show()
#显示图片