# -*- coding: utf-8 -*-
"""
Demonstration of some of the shader programs included with pyqtgraph that can be
used to affect the appearance of a surface.
"""



## Add path to library (just for examples; you do not need this)
# import initExample

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GL Shaders')
w.setCameraPosition(distance=500, azimuth=-90)

g = gl.GLGridItem()
g.scale(50,50,1)
w.addItem(g)

import numpy as np

import STLparser


md = gl.MeshData.sphere(rows=10, cols=20)

# m1 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 0.2), shader='balloon', glOptions='additive')
# m1.translate(x[0], 0, 0)
# m1.scale(1, 1, 2)
# w.addItem(m1)
#
# m2 = gl.GLMeshItem(meshdata=md, smooth=True, shader='normalColor', glOptions='opaque')
# m2.translate(x[1], 0, 0)
# m2.scale(1, 1, 2)
# w.addItem(m2)

# m3 = gl.GLMeshItem(meshdata=md, smooth=True, shader='viewNormalColor', glOptions='opaque')
# m3.translate(x[2], 0, 0)
# m3.scale(1, 1, 2)
# w.addItem(m3)

angle1=50
angle2=-45
angle3=90
angle4=30
angle5=50
angle6=-20


baseSTL = STLparser.parseSTL("stl/base.stl")
baseMesh = gl.MeshData(vertexes=baseSTL)
base3D = gl.GLMeshItem(meshdata=baseMesh, smooth=False, shader='shaded', glOptions='opaque')
w.addItem(base3D)

art1STL = STLparser.parseSTL("stl/art1.stl")
art1Mesh = gl.MeshData(vertexes=art1STL)
art13D = gl.GLMeshItem(meshdata=art1Mesh, smooth=False, shader='shaded', glOptions='opaque')

art13D.translate(0, 0, 86)
w.addItem(art13D)

art2STL = STLparser.parseSTL("stl/art2.stl")
art2Mesh = gl.MeshData(vertexes=art2STL)
art23D = gl.GLMeshItem(meshdata=art2Mesh, smooth=False, shader='shaded', glOptions='opaque')
art23D.translate(0, 0, 202)
w.addItem(art23D)

art3STL = STLparser.parseSTL("stl/art3.stl")
art3Mesh = gl.MeshData(vertexes=art3STL)
art33D = gl.GLMeshItem(meshdata=art3Mesh, smooth=False, shader='shaded', glOptions='opaque')
w.addItem(art33D)

art4STL = STLparser.parseSTL("stl/art4.stl")
art4Mesh = gl.MeshData(vertexes=art4STL)
art43D = gl.GLMeshItem(meshdata=art4Mesh, smooth=False, shader='shaded', glOptions='opaque')
w.addItem(art43D)

art5STL = STLparser.parseSTL("stl/art5.stl")
art5Mesh = gl.MeshData(vertexes=art5STL)
art53D = gl.GLMeshItem(meshdata=art5Mesh, smooth=False, shader='shaded', glOptions='opaque')
w.addItem(art53D)

art6STL = STLparser.parseSTL("stl/art6.stl")
art6Mesh = gl.MeshData(vertexes=art6STL)
art63D = gl.GLMeshItem(meshdata=art6Mesh, smooth=False, shader='shaded', glOptions='opaque')
w.addItem(art63D)

# angle1=0
art13D.rotate(angle1, 0, 0, 1, True)
art23D.rotate(angle1, 0, 0, 1, True)
art33D.rotate(angle1, 0, 0, 1, True)
art43D.rotate(angle1, 0, 0, 1, True)
art53D.rotate(angle1, 0, 0, 1, True)
art63D.rotate(angle1, 0, 0, 1, True)


# angle2=0
art3x=160*np.sin(angle2/180.0*np.pi)
art3z=160*np.cos(angle2/180.0*np.pi)+202

art33D.translate(art3x, 0, art3z, True)
art43D.translate(art3x, 0, art3z, True)
art53D.translate(art3x, 0, art3z, True)
art63D.translate(art3x, 0, art3z, True)

art23D.rotate(angle2, 0, 1, 0, True)
art33D.rotate(angle2, 0, 1, 0, True)
art43D.rotate(angle2, 0, 1, 0, True)
art53D.rotate(angle2, 0, 1, 0, True)
art63D.rotate(angle2, 0, 1, 0, True)

# angle3=0
art4x=90.5*np.sin(angle3/180.0*np.pi)
art4z=90.5*np.cos(angle3/180.0*np.pi)

art5x=(90.5+104.5)*np.sin(angle3/180.0*np.pi)
art5z=(90.5+104.5)*np.cos(angle3/180.0*np.pi)

art43D.translate(art4x, 0, art4z, True)
art53D.translate(art5x, 0, art5z, True)
art63D.translate(art5x, 0, art5z, True)

art33D.rotate(angle3, 0, 1, 0, True)
art43D.rotate(angle3, 0, 1, 0, True)
art53D.rotate(angle3, 0, 1, 0, True)
art63D.rotate(angle3, 0, 1, 0, True)

# angle4=0
art43D.rotate(angle4, 0, 0, 1, True)
art53D.rotate(angle4, 0, 0, 1, True)
art63D.rotate(angle4, 0, 0, 1, True)

# angle5=0
art6x=64*np.sin(angle5/180.0*np.pi)
art6z=64*np.cos(angle5/180.0*np.pi)

art63D.translate(art6x, 0, art6z, True)

art53D.rotate(angle5, 0, 1, 0, True)
art63D.rotate(angle5, 0, 1, 0, True)

# angle6=0
art63D.rotate(angle6, 0, 0, 1, True)


# print("X: " + str(art4x) + "    Z: " + str(art4z))






#

#

#


# m4 = gl.GLMeshItem(meshdata=md2, smooth=True, shader='shaded', glOptions='opaque')
# m4.translate(0, 0, 1)
# m4.setParent(m1)
# w.addItem(m4)

# m1.rotate(30,0,0,1,local=True)
# m4.rotate(30,0,0,1,local=True)
# m4.rotate(30,1,0,0,local=True)



# m5 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 1), shader='edgeHilight', glOptions='opaque')
# m5.translate(x[4], 0, 0)
# m5.scale(1, 1, 2)
# w.addItem(m5)
#
# m6 = gl.GLMeshItem(meshdata=md, smooth=True, color=(1, 0, 0, 1), shader='heightColor', glOptions='opaque')
# m6.translate(x[5], 0, 0)
# m6.scale(1, 1, 2)
# w.addItem(m6)




#def psi(i, j, k, offset=(25, 25, 50)):
    #x = i-offset[0]
    #y = j-offset[1]
    #z = k-offset[2]
    #th = np.arctan2(z, (x**2+y**2)**0.5)
    #phi = np.arctan2(y, x)
    #r = (x**2 + y**2 + z **2)**0.5
    #a0 = 1
    ##ps = (1./81.) * (2./np.pi)**0.5 * (1./a0)**(3/2) * (6 - r/a0) * (r/a0) * np.exp(-r/(3*a0)) * np.cos(th)
    #ps = (1./81.) * 1./(6.*np.pi)**0.5 * (1./a0)**(3/2) * (r/a0)**2 * np.exp(-r/(3*a0)) * (3 * np.cos(th)**2 - 1)

    #return ps

    ##return ((1./81.) * (1./np.pi)**0.5 * (1./a0)**(3/2) * (r/a0)**2 * (r/a0) * np.exp(-r/(3*a0)) * np.sin(th) * np.cos(th) * np.exp(2 * 1j * phi))**2


#print("Generating scalar field..")
#data = np.abs(np.fromfunction(psi, (50,50,100)))


##data = np.fromfunction(lambda i,j,k: np.sin(0.2*((i-25)**2+(j-15)**2+k**2)**0.5), (50,50,50));
#print("Generating isosurface..")
#verts = pg.isosurface(data, data.max()/4.)

#md = gl.MeshData.MeshData(vertexes=verts)

#colors = np.ones((md.vertexes(indexed='faces').shape[0], 4), dtype=float)
#colors[:,3] = 0.3
#colors[:,2] = np.linspace(0, 1, colors.shape[0])
#m1 = gl.GLMeshItem(meshdata=md, color=colors, smooth=False)

#w.addItem(m1)
#m1.translate(-25, -25, -20)

#m2 = gl.GLMeshItem(vertexes=verts, color=colors, smooth=True)

#w.addItem(m2)
#m2.translate(-25, -25, -50)



## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
