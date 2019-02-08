# 重合位置点阵CSL计算总结

## Packages and Function
### Numpy

1. 角度/弧度转换
```
    rad = np.deg2rad(degree)
    degree = np.rad2deg(rad)
```
2. 矩阵的调整?
```
    CellX = np.reshape(SupCell[0], np.size(SupCell[0]), 1)
```
### imageio
可以用于生成gif动态图片, 读取写入图片

Q: 是否有替代的包???


