import pyqtgraph.opengl as gl
import STLparser
import numpy as np

class Robot(object):
    def __init__(self, showCurrent, showNext, colorCurrent, colorNext):
        self.L1=202
        self.L2=160
        self.L3=195
        self.L4=67.15

        self.d1=86
        self.d3=90.5
        self.d4=104.5
        self.d5=64



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

        EOATcenter = gl.MeshData.sphere(rows=10, cols=20)

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

        self.NextEOAT = gl.GLMeshItem(meshdata=EOATcenter, smooth=False, shader='shaded', glOptions='translucent')

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
        self.w.addItem(self.NextEOAT)

    def moveEOAT(self, EOATpos):
        self.NextEOAT.resetTransform()
        self.NextEOAT.scale(5,5,5)
        self.NextEOAT.translate(EOATpos[0], EOATpos[1], EOATpos[2])

    def rotArt1(self, model, angle1):
        model[1].rotate(angle1, 0, 0, 1, True)
        model[2].rotate(angle1, 0, 0, 1, True)
        model[3].rotate(angle1, 0, 0, 1, True)
        model[4].rotate(angle1, 0, 0, 1, True)
        model[5].rotate(angle1, 0, 0, 1, True)
        model[6].rotate(angle1, 0, 0, 1, True)

    def rotArt2(self, model, angle2):
        art3x=self.L2*np.sin(angle2/180.0*np.pi)
        art3z=self.L2*np.cos(angle2/180.0*np.pi)+self.L1

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
        art4x=self.d3*np.sin(angle3/180.0*np.pi)
        art4z=self.d3*np.cos(angle3/180.0*np.pi)

        art5x=(self.d3+self.d4)*np.sin(angle3/180.0*np.pi)
        art5z=(self.d3+self.d4)*np.cos(angle3/180.0*np.pi)

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
        art6x=self.d5*np.sin(angle5/180.0*np.pi)
        art6z=self.d5*np.cos(angle5/180.0*np.pi)

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
        model[1].translate(0, 0, self.d1)
        model[2].translate(0, 0, self.L1)

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

    def calculatenoaMatrix(self, orientationAngles):
        angleX = np.radians(orientationAngles[0])
        angleY = np.radians(orientationAngles[1])
        angleZ = np.radians(orientationAngles[2])

        Sx = np.around(np.sin(angleX),4)
        Sy = np.around(np.sin(angleY),4)
        Sz = np.around(np.sin(angleZ),4)
        Cx = np.around(np.cos(angleX),4)
        Cy = np.around(np.cos(angleY),4)
        Cz = np.around(np.cos(angleZ),4)

        noaMatrix=[
            [Cy*Cz, -Cy*Sz, Sy],
            [Cx*Sz + Cz*Sx*Sy, Cx*Cz - Sx*Sy*Sz, -Cy*Sx],
            [-Cx*Cz*Sy + Sx*Sz, Cx*Sy*Sz + Cz*Sx, Cx*Cy]
        ]

        return noaMatrix

    def IK(self, EOATpos, orientationAngles):

        noaMatrix=self.calculatenoaMatrix(orientationAngles)

        mpos=[EOATpos[0]-noaMatrix[0][2]*self.L4, EOATpos[1]-noaMatrix[1][2]*self.L4, EOATpos[2]-noaMatrix[2][2]*self.L4]
        print("Mpos: " + str(mpos))

        ### Q1 ###
        if mpos[0]!=0:
            q1rad=np.arctan(mpos[1]/mpos[0])
        else:
            q1rad=0
        q1=np.around(np.degrees(q1rad),1)

        # print("Q1: " + str(q1))


        ### Q3 ###
        cosq3=(np.square(mpos[0])+np.square(mpos[1])+np.square(mpos[2]-self.L1)-np.square(self.L2)-np.square(self.L3))/(2*self.L2*self.L3)
        if cosq3!=0:
            q3rad=np.arctan(np.sqrt(1-np.square(cosq3))/cosq3)
        else:
            q3rad=np.pi/2
        q3=np.around(np.degrees(q3rad),1)

        # print("Q3: " + str(q3))

        ### Q2 ###
        q2rad=-np.arctan(mpos[2]/np.sqrt(np.square(mpos[0])+np.square(mpos[1])))+np.arctan((self.L3*np.sin(q3rad))/(self.L2+self.L3+np.cos(q3rad)))+np.pi/2
        q2=np.around(np.degrees(q2rad),1)

        # print("Q2: " + str(q2))

        S1 = np.sin(q1rad)
        C1 = np.cos(q1rad)
        S2 = np.sin(q2rad)
        C2 = np.cos(q2rad)
        S3 = np.sin(q3rad)
        C3 = np.cos(q3rad)
        Nx=noaMatrix[0][0]
        Ny=noaMatrix[1][0]
        Nz=noaMatrix[2][0]
        Ox=noaMatrix[0][1]
        Oy=noaMatrix[1][1]
        Oz=noaMatrix[2][1]
        Ax=noaMatrix[0][2]
        Ay=noaMatrix[1][2]
        Az=noaMatrix[2][2]

        r23=-Ax*S1 + Ay*C1
        r31=Nx*(C1*C2*S3 + C1*C3*S2) + Ny*(C2*S1*S3 + C3*S1*S2) + Nz*(C2*C3 - S2*S3)
        r32=Ox*(C1*C2*S3 + C1*C3*S2) + Oy*(C2*S1*S3 + C3*S1*S2) + Oz*(C2*C3 - S2*S3)
        r33=Ax*(C1*C2*S3 + C1*C3*S2) + Ay*(C2*S1*S3 + C3*S1*S2) + Az*(C2*C3 - S2*S3)

        p=r23/r33

        # q4rad=np.arcsin(r23/r33)
        q4rad=np.arctan(p/np.sqrt(1-np.square(p)))
        q5rad=np.arccos(r33)
        q6rad=np.arctan(-r32/r31)
        q4 = np.around(np.degrees(q4rad),1)
        q5 = np.around(np.degrees(q5rad),1)
        q6 = np.around(np.degrees(q6rad),1)

        # q5rad = np.pi/2 - np.arccos(noaMatrix[0][2]*(C1*S2*S3-C1*C2*C3)+noaMatrix[1][2]*(S1*S2*S3-S1*C2*C3)+noaMatrix[2][2]*(-S2*C3 -C2*S3))
        # q5 = np.around(np.degrees(q5rad),1)
        # S5 = np.sin(q5rad)

        # q6rad = np.arcsin((-noaMatrix[0][0]*(C1*S2*S3-C1*C2*C3)+noaMatrix[1][0]*(S1*S2*S3-S1*C2*C3)+noaMatrix[2][0]*(-S2*C3-C2*S3))/S5)
        # q6 = np.around(np.degrees(q6rad),1)

        # q4rad = np.arccos((noaMatrix[0][1]*(C1*S2*C3-C1*C2*S3)+noaMatrix[1][1]*(S1*S2*C3-S1*C2*S3)+noaMatrix[1][1]*(-S2*S3-C2*C3))/S5)
        # q4 = np.around(np.degrees(q4rad),1)

        print("Q1: " + str(q1))
        print("Q2: " + str(q2))
        print("Q3: " + str(q3))
        print("Q4: " + str(q4))
        print("Q5: " + str(q5))
        print("Q6: " + str(q6))

        self.rotateArm(self.NextPosModel, q1, q2, q3, q4, q5, q6)










    def setColor(self, model, color):
        model[0].setColor(color)
        model[1].setColor(color)
        model[2].setColor(color)
        model[3].setColor(color)
        model[4].setColor(color)
        model[5].setColor(color)
        model[6].setColor(color)
