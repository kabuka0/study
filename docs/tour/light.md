---
sort: 3
---

# 光照和材质

WxGL提供了BaseLight（基础光照模式）、SunLight（太阳光照模式）、LampLight（点光源光照模式）、SkyLight（户外光照模式）、SphereLight（球谐光照模式）等多种光照方案。即使不设置light参数，WxGL的模型也都使用了默认的光照模式。下面的代码使用light参数演示了不同光照模式下的球环模型。

```python
import wxgl

app = wxgl.App()
app.text('太阳光', (-5,7.5,0), align='center')
app.torus((-5,4,0), 1, 3, vec=(0,1,1), light=wxgl.SunLight())
app.text('灯光', (5,7.5,0), align='center')
app.torus((5,4,0), 1, 3, vec=(0,1,1), light=wxgl.LampLight())
app.text('户外光', (-5,-0.5,0), align='center')
app.torus((-5,-4,0), 1, 3, vec=(0,1,1), light=wxgl.SkyLight())
app.text('球谐光', (5,-0.5,0), align='center')
app.torus((5,-4,0), 1, 3, vec=(0,1,1), light=wxgl.SphereLight(5))
app.show()
```

![tour_light.png](https://raw.githubusercontent.com/xufive/wxgl/master/example/res/md/tour_light.png)


光照模式配合漫反射系数、镜面反射系数、高光系数、透光系数等参数，可模拟出不同的材质。这几个参数的默认值和值域范围请参考本文档的API部分。下面的代码绘制了塑料质感的分子3D模型。


```python
import wxgl

c1, c2, c3, c4, c5 = '#d8d8d8', '#00d0d0', '#6060f0', '#903030', '#90C090'
light = wxgl.SunLight(direction=(0.5,-0.5,-1.0), diffuse=0.7, specular=0.98, shiny=100, pellucid=0.9)

app = wxgl.App(bg='#f0f0f0', azim=-30, elev=20, fovy=40)

app.sphere((-2,0,0), 0.35, color=c1, light=light)
app.sphere((0,0,0), 0.35, color=c1, light=light)
app.sphere((2,0,0), 0.35, color=c1, light=light)
app.sphere((-1,-1,0), 0.35, color=c1, light=light)
app.sphere((1,-1,0), 0.35, color=c1, light=light)

app.cylinder((-2,0,0), (-1,-1,0), 0.17, color=c2, light=light)
app.cylinder((0,0,0), (-1,-1,0), 0.17, color=c2, light=light)
app.cylinder((0,0,0), (1,-1,0), 0.17, color=c2, light=light)
app.cylinder((2,0,0), (1,-1,0), 0.17, color=c2, light=light)

app.sphere((-2,1.2,-0.6), 0.35, color=c3, light=light)
app.sphere((-3,-0.6,0.6), 0.35, color=c3, light=light)
app.sphere((2.6,0.5,1), 0.35, color=c3, light=light)
app.sphere((2.6,0.5,-1), 0.35, color=c3, light=light)
app.sphere((1,-1.5,1), 0.35, color=c5, light=light)

app.cylinder((-2,0,0), (-2,1.2,-0.6), 0.17, color=c4, light=light)
app.cylinder((-2,0,0), (-3,-0.6,0.6), 0.17, color=c2, light=light)
app.cylinder((2,0,0), (2.6,0.5,1), 0.17, color=c4, light=light)
app.cylinder((2,0,0), (2.6,0.5,-1), 0.17, color=c2, light=light)
app.cylinder((1,-1,0), (1,-1.5,1), 0.17, color=c2, light=light)

app.sphere((0,0.7,-0.8), 0.15, color=c2, light=light)
app.sphere((0,0.7,0.8), 0.15, color=c2, light=light)
app.sphere((-1,-1.7,-0.8), 0.15, color=c2, light=light)
app.sphere((-1,-1.7,0.8), 0.15, color=c2, light=light)

app.cylinder((0,0,0), (0,0.7,-0.8), 0.08, color=c2, light=light)
app.cylinder((0,0,0), (0,0.7,0.8), 0.08, color=c2, light=light)
app.cylinder((-1,-1,0), (-1,-1.7,-0.8), 0.08, color=c2, light=light)
app.cylinder((-1,-1,0), (-1,-1.7,0.8), 0.08, color=c2, light=light)

app.show()
```

![tour_material.png](https://raw.githubusercontent.com/xufive/wxgl/master/example/res/md/tour_material.png)

