import numpy as np
import drawsvg as draw
from points import *
from shapes import *

def drawTileTrifle(drawing, a, b, T, s):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: triangle stroke color
    """

# three lines inside TRIFLE shape
    start=TRIFLE(a,b)[0]
    end1=TRIFLE(a,b)[1]
    end2=TRIFLE(a,b)[2]
    end3=TRIFLE(a,b)[3]
    line1=[start,end1]
    line2=[start,end2]
    line3=[start,end3]

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in line1]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_opacity=0.3,
    stroke_width=0.05))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in line2]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_opacity=0.3,
    stroke_width=0.05))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in line3]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_opacity=0.3,
    stroke_width=0.05))

# contour of HALF BOW-TIE shape
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in HALF_BOW_TIE(a,b)]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.05))

# TILE shape
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TILE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.1))

# TRIANGLE with arrow
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TRIANGLE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in arrow_mid(TRIANGLE(a,b)[2],TRIANGLE(a,b)[1])]),close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))



def drawTileBowTie(drawing, a, b, T, s):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: triangle stroke color
    """

# contour of HALF BOW-TIE shape
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in HALF_BOW_TIE(a,b)]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.05))

# TILE shape
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TILE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.1))

# TRIANGLE with arrow
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TRIANGLE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in arrow_mid(TRIANGLE(a,b)[2],TRIANGLE(a,b)[1])]),close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))



def drawTile(drawing, a, b, T, s):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: triangle stroke color
    """

# TILE shape
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TILE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.1))

# TRIANGLE with arrow
    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TRIANGLE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in arrow_mid(TRIANGLE(a,b)[2],TRIANGLE(a,b)[1])]),close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))



def drawTbaseVector(drawing, a, b, T, s, index):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: arrow stroke color
    """
    origin=pt(0,0)
    extremity=T_base(a,b)[index]
    segment=[origin, extremity]

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in segment]),close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in arrow(origin,extremity)]),close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke=s,
    stroke_width=0.1))

