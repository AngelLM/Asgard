import sys
import struct
import numpy

class STLVec3:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

class STLTriangle:
    def __init__(self, normal, v0, v1, v2, attributes):
        self.normal = normal
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.attributes = attributes

class STLData:
    def __init__(self, header, tris):
        self.header = header
        self.tris = tris

def readFloat(f):
    float_bytes = f.read(4)
    return struct.unpack('f', float_bytes)[0]

def readVec3(f):
    x = readFloat(f)
    y = readFloat(f)
    z = readFloat(f)

    return STLVec3(x, y, z)

def readUnsignedInt(f):
    uint_bytes = f.read(4)
    return struct.unpack('I', uint_bytes)[0]

def readUINT16(f):
    uint16_bytes = f.read(2)
    return struct.unpack('H', uint16_bytes)[0]

def readTriangle(f):
    norm = readVec3(f)
    v0 = readVec3(f)
    v1 = readVec3(f)
    v2 = readVec3(f)
    attributes = readUINT16(f)

    return STLTriangle(norm, v0, v1, v2, attributes)

def parseSTL(file_name):
    f = open(file_name, "rb")

    header = f.read(80)

    # print ("STL HEADER = ", header)

    num_tris = readUnsignedInt(f)

    tris = []

    for i in range(num_tris):
        tris.append(readTriangle(f))

    stlData = STLData(header, tris)

    vertex = []

    for triangle in stlData.tris:

        v0=[]
        v0.append(triangle.v0.x)
        v0.append(triangle.v0.y)
        v0.append(triangle.v0.z)

        v1=[]
        v1.append(triangle.v1.x)
        v1.append(triangle.v1.y)
        v1.append(triangle.v1.z)

        v2=[]
        v2.append(triangle.v2.x)
        v2.append(triangle.v2.y)
        v2.append(triangle.v2.z)

        tver = [v0,v1,v2]

        vertex.append(tver)

    return numpy.asarray(vertex)
