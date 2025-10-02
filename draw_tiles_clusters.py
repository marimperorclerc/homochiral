import numpy as np
import drawsvg as draw
from points import *
from shapes import *

def drawTileBowTie(drawing, a, b, T, s):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: triangle stroke color
    """

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in HALF_BOW_TIE(a,b)]), close=False),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.05))

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

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TILE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
    stroke_width=0.1))


def drawTile(drawing, a, b, T, s):
    """
    drawing: drawing to draw on
    T: transformation matrix
    s: triangle stroke color
    """

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

    drawing.append(draw.Use(
    draw.Lines(*flatten([p.xy for p in TILE(a,b)]), close=True),
    0, 0,
    transform=f"matrix({T[0]} {T[3]} {T[1]} {T[4]} {T[2]} {T[5]})",
    fill="none",
    stroke="black",
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

