import numpy as np
import wxgl

r = 1 # 地球半径
gv, gu = np.mgrid[np.pi/2:-np.pi/2:91j, 0:2*np.pi:361j] # 纬度和经度网格
xs = r * np.cos(gv)*np.cos(gu)
ys = r * np.cos(gv)*np.sin(gu)
zs = r * np.sin(gv)

light = wxgl.SunLight(direction=(-1,1,0), ambient=(0.1,0.1,0.1)) # 太阳光照向左前方，暗环境光
tf = lambda t : ((0, 0, 1, (0.02*t)%360), ) # 以20°/s的角速度绕y逆时针轴旋转

app = wxgl.App(haxis='z') # 以z轴为高度轴
app.title('自转的地球')
app.mesh(xs, ys, zs, texture='res/earth.jpg', light=light, transform=tf)
app.show()