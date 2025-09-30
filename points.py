import numpy as np

# ancillary function for collasping a list to a 1D array
def flatten(lst):
    return [item for sublist in lst for item in sublist]

# points in the plane are coded using class pt(x,y)

# class pt
class pt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = [x, y]

# operations on pt
# addition of two points
def add_pt(pta,ptb):
    px=pta.x+ptb.x
    py=pta.y+ptb.y
    return pt(px,py)

# mid point
def mid_pt(pta,ptb):
    px=(pta.x+ptb.x)/2
    py=(pta.y+ptb.y)/2
    return pt(px,py)

# scaling factor
def scale(point,scale=1):
    return pt(scale*point.x,scale*point.y)

# distance between two points
def distance(pta,ptb):
    deltax=ptb.x-pta.x
    deltay=ptb.y-pta.y
    dist=np.sqrt(deltax**2+deltay**2)
    return dist

# ancillary function for drawing an arrow 
# arrow is oriented from point pta to point ptb
# size is scaled to the length of the segment between pta and ptb
# arrow retruns three points p2, p1, p3
# p1 is located at the apex of the arrow located on the segment
# p2 and p3 are the two other extremities of the arrow
# internal angle of the arrow is fixed to 60°
def arrow(pta,ptb,size=0.15): 
    pmid=mid_pt(pta,ptb) # middle point of the segment
    deltax=ptb.x-pta.x # length of the segment along x
    deltay=ptb.y-pta.y # length of the segment along y
    p1x=pmid.x+size*deltax 
    p1y=pmid.y+size*deltay
    p1=pt(p1x,p1y) # arrow point on the segment 
    p1cx=pmid.x-size*deltax/2 
    p1cy=pmid.y-size*deltay/2
    p1c=pt(p1cx,p1cy) # intermediate point on the segment
    p2x=p1c.x+size*np.sqrt(3)*(-deltay)/2
    p2y=p1c.y+size*np.sqrt(3)*(deltax)/2
    p2=pt(p2x,p2y) # second arrow point
    p3x=p1c.x+size*np.sqrt(3)*(deltay)/2
    p3y=p1c.y+size*np.sqrt(3)*(-deltax)/2
    p3=pt(p3x,p3y) # third arrow point

    return [p2,p1,p3]
