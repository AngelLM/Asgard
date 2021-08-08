from sympy import *

Q1 = Symbol('Q1')
Q2 = Symbol('Q2')
Q3 = Symbol('Q3')
Q4 = Symbol('Q4')
Q5 = Symbol('Q5')
Q6 = Symbol('Q6')
r11 = Symbol('r11')
r12 = Symbol('r12')
r13 = Symbol('r13')
r21 = Symbol('r21')
r22 = Symbol('r22')
r23 = Symbol('r23')
r31 = Symbol('r31')
r32 = Symbol('r32')
r33 = Symbol('r33')
R3=Matrix([[cos(Q1)*cos(Q2)*sin(Q3)+cos(Q1)*sin(Q2)*cos(Q3),sin(Q1),-
cos(Q1)*cos(Q2)*cos(Q3)+cos(Q1)*sin(Q2)*sin(Q3)],[sin(Q1)*cos(Q2)*sin(Q3)+sin(Q1)
*sin(Q2)*cos(Q3),-cos(Q1),-sin(Q1)*cos(Q2)*cos(Q3)+sin(Q1)*sin(Q2)*sin(Q3)],[-
cos(Q2)*cos(Q3)+sin(Q2)*sin(Q3),0,-cos(Q2)*sin(Q3)-sin(Q2)*cos(Q3)]])
NOAtcp=Matrix([[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]])
print(R3.T*NOAtcp)
