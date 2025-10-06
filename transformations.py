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
Rsvg=Rh
# Rsvg is because y axis is downwards in svg graphics
# NEED TO BE ADDED AT THE END for all drawings


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

# transformations corresponding to translations to the 14 vertices of TILE(a,b)
def TILE_trans(a,b):
    T=[]
    for i in range(0,14):
        T+=[ttrans(TILE(a,b)[i].x,TILE(a,b)[i].y)]
    return T


# transformations corresponding to the 12 T_base(a,b)[i] translations
def T_trans(a,b):
    T=[]
    for i in range(0,12):
        T+=[ttrans(T_base(a,b)[i].x,T_base(a,b)[i].y)]
    return T

# list of transformation for the C cluster
# code for the six EVEN tiles around the ODD tile in the middle in its reference orientation
def C_cluster_transfo_list(a,b):
    T=[mul(TILE_trans(a,b)[2],trot(-np.pi/6-2*np.pi/3)),
       mul(T_trans(a,b)[2],trot(-np.pi/6-np.pi/3)),
       mul(TILE_trans(a,b)[6],trot(-np.pi/6)),
       mul(TILE_trans(a,b)[8],trot(-np.pi/6+np.pi/3)),
       mul(T_trans(a,b)[4],trot(-np.pi/6-4*np.pi/3)),
# inversion to b,a for T_base only once !!!
       mul(mul(TILE_trans(a,b)[12],T_trans(b,a)[9]),trot(-np.pi/6))] 
    return T


# list of transformation for the full C cluster (12 tiles)
# code for the six EVEN tiles like in C_cluster_transfo_list(a,b)
# plus 6 more EVEN tiles
# three of them are duplicated using: T_trans(b,a)[1], T_trans(b,a)[5] and two times T_trans(b,a)[9] 
# the three others are obtained by inversion operation around the green points
def C_full_cluster_transfo_list(a,b):
    T=[
    mul(TILE_trans(a,b)[2],trot(-np.pi/6-2*np.pi/3)),
# duplicated with inversion operation around green point
    mul(mul(mul(TILE_trans(a,b)[2],T_trans(b,a)[11]),T_trans(b,a)[11]),trot(-np.pi/6-2*np.pi/3+np.pi)),

    mul(T_trans(a,b)[2],trot(-np.pi/6-np.pi/3)),
# duplicated
    mul(mul(T_trans(a,b)[2],T_trans(b,a)[1]),trot(-np.pi/6-np.pi/3)),
 
    mul(TILE_trans(a,b)[6],trot(-np.pi/6)),
# duplicated with inversion operation around green point
    mul(mul(mul(TILE_trans(a,b)[6],T_trans(b,a)[3]),T_trans(b,a)[3]),trot(-np.pi/6+np.pi)),

    mul(TILE_trans(a,b)[8],trot(-np.pi/6+np.pi/3)), 
# duplicated
    mul(mul(TILE_trans(a,b)[8],T_trans(b,a)[5]),trot(-np.pi/6+np.pi/3)), 

    mul(T_trans(a,b)[4],trot(-np.pi/6-4*np.pi/3)),
# duplicated with inversion operation around green point
   mul(mul(mul(T_trans(a,b)[4],T_trans(b,a)[7]),T_trans(b,a)[7]),trot(-np.pi/6-4*np.pi/3+np.pi)),
 
# inversion to b,a for T_base !!!
    mul(mul(TILE_trans(a,b)[12],T_trans(b,a)[9]),trot(-np.pi/6)), 
# duplicated tile
    mul(mul(mul(TILE_trans(a,b)[12],T_trans(b,a)[9]),T_trans(b,a)[9]),trot(-np.pi/6)) 
    ] 
    return T

