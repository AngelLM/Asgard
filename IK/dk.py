from sympy import *
import numpy as np

C1=Symbol("C1")
C2=Symbol("C2")
C3=Symbol("C3")
C4=Symbol("C4")
C5=Symbol("C5")
C6=Symbol("C6")

S1=Symbol("S1")
S2=Symbol("S2")
S3=Symbol("S3")
S4=Symbol("S4")
S5=Symbol("S5")
S6=Symbol("S6")

L1=Symbol("L1")
L2=Symbol("L2")
L3=Symbol("L3")
L4=Symbol("L4")


Nx = Symbol('Nx')
Ny = Symbol('Ny')
Nz = Symbol('Nz')
Ox = Symbol('Ox')
Oy = Symbol('Oy')
Oz = Symbol('Oz')
Ax = Symbol('Ax')
Ay = Symbol('Ay')
Az = Symbol('Az')

# A1=Matrix([
#     [C1,0,-S1,0],
#     [S1,0,C1,0],
#     [0,-1,0,L1],
#     [0,0,0,1]
#     ])
#
# A2=Matrix([
#     [S2,C2,0,L2*S2],
#     [-C2,S2,0,-L2*C2],
#     [0,0,1,0],
#     [0,0,0,1]
#     ])
#
# A3=Matrix([
#     [-S3,0,C3,0],
#     [C3,0,S3,0],
#     [0,1,0,0],
#     [0,0,0,1]
#     ])
#
# A4=Matrix([
#     [C4,0,-S4,0],
#     [S4,0,C4,0],
#     [0,-1,0,L3],
#     [0,0,0,1]
#     ])
#
# A5=Matrix([
#     [C5,0,S5,0],
#     [S5,0,-C5,0],
#     [0,1,0,0],
#     [0,0,0,1]
#     ])
#
# A6=Matrix([
#     [C6,-S6,0,0],
#     [S6,C6,0,0],
#     [0,0,1,L4],
#     [0,0,0,1]
#     ])


R1=Matrix([
    [C1,0,-S1],
    [S1,0,C1],
    [0,-1,0]
    ])

R2=Matrix([
    [S2,C2,0],
    [-C2,S2,0],
    [0,0,1]
    ])

R3=Matrix([
    [-S3,0,C3],
    [C3,0,S3],
    [0,1,0]
    ])

R13=R1*R2*R3

R4=Matrix([
    [C4,0,-S4],
    [S4,0,C4],
    [0,-1,0]
    ])

R5=Matrix([
    [C5,0,S5],
    [S5,0,-C5],
    [0,1,0]
    ])

R6=Matrix([
    [C6,-S6,0],
    [S6,C6,0],
    [0,0,1]
    ])

R46=R4*R5*R6

NOAtcp=Matrix([[Nx,Ox,Ax],[Ny,Oy,Ay],[Nz,Oz,Az]])

print("R13t")
print(R13.T)
print()
print()


print("R46")
print(R46)

print()
print("R13*NOAtcp")
print(R13.T*NOAtcp)
# print(R)
# A=A1*A2*A3*A4*A5*A6
# print(A)
# print()
# print()
#
# A=A4*A5*A6
# print(A)
#
# print()
# print()
# A=A1*A2*A3
# print(A)

# Q1 = Symbol('Q1')
# Q2 = Symbol('Q2')
# Q3 = Symbol('Q3')
# Q4 = Symbol('Q4')
# Q5 = Symbol('Q5')
# Q6 = Symbol('Q6')

# R3=Matrix([[cos(Q1)*cos(Q2)*sin(Q3)+cos(Q1)*sin(Q2)*cos(Q3),sin(Q1),-
# cos(Q1)*cos(Q2)*cos(Q3)+cos(Q1)*sin(Q2)*sin(Q3)],[sin(Q1)*cos(Q2)*sin(Q3)+sin(Q1)
# *sin(Q2)*cos(Q3),-cos(Q1),-sin(Q1)*cos(Q2)*cos(Q3)+sin(Q1)*sin(Q2)*sin(Q3)],[-
# cos(Q2)*cos(Q3)+sin(Q2)*sin(Q3),0,-cos(Q2)*sin(Q3)-sin(Q2)*cos(Q3)]])
