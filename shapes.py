import numpy as np
from points import *


# The 12 unit vectors for 12-fold symmetry
# e_unit contains 12 points corresponding to the 12 unit vectors
# e_unit[0] to e_unit[11]
e_unit=[]
for i in range(0,12):
    e_unit+=[pt(np.cos(i*np.pi/6),np.sin(i*np.pi/6))]


# the 14 edges vectors of Tile(a,b)
# given for the reference orientation
# long edge of Tile(a,b) is horizontal
def TILE_EDGES(a,b):
    return [scale(e_unit[0],a),
            scale(e_unit[10],a),
            scale(e_unit[1],b),
            scale(e_unit[3],b),
            scale(e_unit[0],a),
            scale(e_unit[2],a),
            scale(e_unit[5],b),
            scale(e_unit[7],b),
            scale(e_unit[4],a),
            scale(e_unit[6],a),
            scale(e_unit[6],a),
            scale(e_unit[8],a),
            scale(e_unit[11],b),
            scale(e_unit[9],b)
  ]


# TILE(a,b) contains the 14 points of the tile
# origin is taken at a pt(0,0)
# origin is located at the reference point of Tile(a,b)
origin=pt(0,0)

def TILE(a,b):
    tile_list=[origin]

    for i in range(0,14):
        p=tile_list[i]
        edge=TILE_EDGES(a,b)[i]
        p=add_pt(p,edge)
        tile_list+=[p]
    
    return tile_list

# regular triangle inside Tile(a,b)
# TRIANGLE(a,b)[0]=TILE(a,b)[0]=origin=pt(0,0)
def TRIANGLE(a,b):
    p1=TILE(a,b)[0]    
    p2=TILE(a,b)[4]    
    p3=TILE(a,b)[10]    
    return [p1,p2,p3]

# half bow-tie inside Tile(a,b)
# three edges
def HALF_BOW_TIE_EDGES(a,b):
    return [scale(e_unit[9],a),
            scale(e_unit[11],b),
            scale(e_unit[8],b)
  ]

# half bow-tie
# three points
# HALF_BOW_TIE(a,b)[0]=TILE(a,b)[10]
def HALF_BOW_TIE(a,b):
    tile_list=[TILE(a,b)[10]]

    for i in range(0,3):
        p=tile_list[i]
        edge=HALF_BOW_TIE_EDGES(a,b)[i]
        p=add_pt(p,edge)
        tile_list+=[p]
    
    return tile_list

# T_base(a,b)
def T_base(a,b):
    base_list=[]
    base=add_pt(TRIANGLE(a,b)[1],scale(TRIANGLE(a,b)[2],-1))
    for i in range(0,12):
        Tbx=np.cos(i*np.pi/6)*base.x-np.sin(i*np.pi/6)*base.y
        Tby=np.sin(i*np.pi/6)*base.x+np.cos(i*np.pi/6)*base.y
        p=pt(Tbx,Tby)
        base_list+=[p]
    
    return base_list
