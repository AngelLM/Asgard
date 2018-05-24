import pyqtgraph.opengl as gl
import STLparser
import numpy as np

class Robot(object):
    def __init__(self, showCurrent, showNext, colorCurrent, colorNext):
        self.L1=86
        self.L2=202
        self.L3=160
        self.L4=90.5
        self.L5=104.5
        self.L6=64

        self.w = gl.GLViewWidget()
        self.w.setCameraPosition(distance=1500, azimuth=-90)

        self.g = gl.GLGridItem()
        self.g.scale(50,50,1)
        self.w.addItem(self.g)


        baseSTL = STLparser.parseSTL("stl/base.stl")
        baseMesh = gl.MeshData(vertexes=baseSTL)

        art1STL = STLparser.parseSTL("stl/art1.stl")
        art1Mesh = gl.MeshData(vertexes=art1STL)

        art2STL = STLparser.parseSTL("stl/art2.stl")
        art2Mesh = gl.MeshData(vertexes=art2STL)

        art3STL = STLparser.parseSTL("stl/art3.stl")
        art3Mesh = gl.MeshData(vertexes=art3STL)

        art4STL = STLparser.parseSTL("stl/art4.stl")
        art4Mesh = gl.MeshData(vertexes=art4STL)

        art5STL = STLparser.parseSTL("stl/art5.stl")
        art5Mesh = gl.MeshData(vertexes=art5STL)

        art6STL = STLparser.parseSTL("stl/art6.stl")
        art6Mesh = gl.MeshData(vertexes=art6STL)

        self.base3D = gl.GLMeshItem(meshdata=baseMesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art13D = gl.GLMeshItem(meshdata=art1Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art23D = gl.GLMeshItem(meshdata=art2Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art33D = gl.GLMeshItem(meshdata=art3Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art43D = gl.GLMeshItem(meshdata=art4Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art53D = gl.GLMeshItem(meshdata=art5Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.art63D = gl.GLMeshItem(meshdata=art6Mesh, smooth=False, shader='shaded', glOptions='translucent')

        self.CurrentPosModel=[self.base3D, self.art13D, self.art23D, self.art33D, self.art43D, self.art53D, self.art63D]

        self.NextBase3D = gl.GLMeshItem(meshdata=baseMesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt13D = gl.GLMeshItem(meshdata=art1Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt23D = gl.GLMeshItem(meshdata=art2Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt33D = gl.GLMeshItem(meshdata=art3Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt43D = gl.GLMeshItem(meshdata=art4Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt53D = gl.GLMeshItem(meshdata=art5Mesh, smooth=False, shader='shaded', glOptions='translucent')
        self.NextArt63D = gl.GLMeshItem(meshdata=art6Mesh, smooth=False, shader='shaded', glOptions='translucent')

        self.NextPosModel=[self.NextBase3D, self.NextArt13D, self.NextArt23D, self.NextArt33D, self.NextArt43D, self.NextArt53D, self.NextArt63D]

        self.showModels(showCurrent, showNext)

        self.rotateArm(self.CurrentPosModel, 0,0,0,0,0,0)
        self.rotateArm(self.NextPosModel, 0,0,0,0,0,0)

        self.setColorCurrent(colorCurrent)
        self.setColorNext(colorNext)

    def clearWindow(self):
        for part in self.CurrentPosModel:
            try:
                self.w.removeItem(part)
            except:
                pass
        for part in self.NextPosModel:
            try:
                self.w.removeItem(part)
            except:
                pass

    def showModels(self, showCurrent, showNext):
        self.clearWindow()
        if showCurrent:
            for part in self.CurrentPosModel:
                self.w.addItem(part)
        if showNext:
            for part in self.NextPosModel:
                self.w.addItem(part)



    def rotArt1(self, model, angle1):
        model[1].rotate(angle1, 0, 0, 1, True)
        model[2].rotate(angle1, 0, 0, 1, True)
        model[3].rotate(angle1, 0, 0, 1, True)
        model[4].rotate(angle1, 0, 0, 1, True)
        model[5].rotate(angle1, 0, 0, 1, True)
        model[6].rotate(angle1, 0, 0, 1, True)

    def rotArt2(self, model, angle2):
        art3x=self.L3*np.sin(angle2/180.0*np.pi)
        art3z=self.L3*np.cos(angle2/180.0*np.pi)+self.L2

        model[3].translate(art3x, 0, art3z, True)
        model[4].translate(art3x, 0, art3z, True)
        model[5].translate(art3x, 0, art3z, True)
        model[6].translate(art3x, 0, art3z, True)

        model[2].rotate(angle2, 0, 1, 0, True)
        model[3].rotate(angle2, 0, 1, 0, True)
        model[4].rotate(angle2, 0, 1, 0, True)
        model[5].rotate(angle2, 0, 1, 0, True)
        model[6].rotate(angle2, 0, 1, 0, True)

    def rotArt3(self, model, angle3):
        art4x=self.L4*np.sin(angle3/180.0*np.pi)
        art4z=self.L4*np.cos(angle3/180.0*np.pi)

        art5x=(self.L4+self.L5)*np.sin(angle3/180.0*np.pi)
        art5z=(self.L4+self.L5)*np.cos(angle3/180.0*np.pi)

        model[4].translate(art4x, 0, art4z, True)
        model[5].translate(art5x, 0, art5z, True)
        model[6].translate(art5x, 0, art5z, True)

        model[3].rotate(angle3, 0, 1, 0, True)
        model[4].rotate(angle3, 0, 1, 0, True)
        model[5].rotate(angle3, 0, 1, 0, True)
        model[6].rotate(angle3, 0, 1, 0, True)

    def rotArt4(self, model, angle4):
        model[4].rotate(angle4, 0, 0, 1, True)
        model[5].rotate(angle4, 0, 0, 1, True)
        model[6].rotate(angle4, 0, 0, 1, True)

    def rotArt5(self, model, angle5):
        art6x=self.L6*np.sin(angle5/180.0*np.pi)
        art6z=self.L6*np.cos(angle5/180.0*np.pi)

        model[6].translate(art6x, 0, art6z, True)

        model[5].rotate(angle5, 0, 1, 0, True)
        model[6].rotate(angle5, 0, 1, 0, True)

    def rotArt6(self, model, angle6):
        model[6].rotate(angle6, 0, 0, 1, True)

    def rotateCurrentArm(self, a1, a2, a3, a4, a5, a6):
        self.rotateArm(self.CurrentPosModel, a1, a2, a3, a4, a5, a6)

    def rotateNextArm(self, a1, a2, a3, a4, a5, a6):
        self.rotateArm(self.NextPosModel, a1, a2, a3, a4, a5, a6)

    def rotateArm(self, model, a1, a2, a3, a4, a5, a6):
        # self.base3D.resetTransform()
        model[1].resetTransform()
        model[2].resetTransform()
        model[3].resetTransform()
        model[4].resetTransform()
        model[5].resetTransform()
        model[6].resetTransform()
        model[1].translate(0, 0, self.L1)
        model[2].translate(0, 0, self.L2)

        self.rotArt1(model,a1)
        self.rotArt2(model,a2)
        self.rotArt3(model,a3)
        self.rotArt4(model,a4)
        self.rotArt5(model,a5)
        self.rotArt6(model,a6)

    def setColorCurrent(self, color):
        self.setColor(self.CurrentPosModel, color)
    def setColorNext(self, color):
        self.setColor(self.NextPosModel, color)

    def setColor(self, model, color):
        model[0].setColor(color)
        model[1].setColor(color)
        model[2].setColor(color)
        model[3].setColor(color)
        model[4].setColor(color)
        model[5].setColor(color)
        model[6].setColor(color)
