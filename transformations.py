import numpy as np
from points import *
from shapes import *

# transformations coded with 6 parameters
# 4 for rotations
# 2 for translation

# Matrix * point
def transPt(M, P):
    return pt(M[0]*P.x + M[1]*P.y + M[2], M[3]*P.x + M[4]*P.y + M[5])


IDENTITY = [1, 0, 0, 0, 1, 0]

#vertical mirror
R = [-1, 0, 0, 0, 1, 0]

Rv=R

#horizontal mirror
Rh=[1, 0, 0, 0, -1, 0]
# used because y axis is downwards in svg graphics
Rsvg=Rh

# Translation matrix
def ttrans(tx, ty):
    return [1, 0, tx, 0, 1, ty]


def transTo(p, q):
    return ttrans(q.x - p.x, q.y - p.y)


# Rotation matrix
def trot(ang):
    c = np.cos(ang)
    s = np.sin(ang)
    return [c, -s, 0, s, c, 0]


# Affine matrix multiply
# combination of two transformations
def mul(A, B):
    return [
        A[0]*B[0] + A[1]*B[3],
        A[0]*B[1] + A[1]*B[4],
        A[0]*B[2] + A[1]*B[5] + A[2],

        A[3]*B[0] + A[4]*B[3],
        A[3]*B[1] + A[4]*B[4],
        A[3]*B[2] + A[4]*B[5] + A[5]
    ]


# transformations corresponding to the 12 T_base(a,b)[i] translations
def T_trans(a,b):
    T=[]
    for i in range(0,12):
        T+=[ttrans(T_base(a,b)[i].x,T_base(a,b)[i].y)]
    return T

