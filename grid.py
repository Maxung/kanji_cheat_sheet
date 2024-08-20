#!/usr/bin/env python3

from reportlab.lib.pagesizes import *
from reportlab.lib.colors import *
from reportlab.lib.units import cm
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

class canvasSpec:
    def __init__ (self,object):
        self.filename=object.filename
        self.size=object.size
        self.width=object.size[0]
        self.height=object.size[1]
        self.xgap=object.xgap
        self.ygap=object.ygap
        self.xlist=[]
        self.ylist=[]
        self.xStart=0
        self.yStart=0

def draw(object,detailTF,canvas,color,lineWidth, filepath):
    def xylist(startPoint,list,max,gap,detailTF):
        i=startPoint*cm
        while i<max-5*gap*cm:
            list.append(i)
            i+=5*gap*cm
            list.append(list[-1]+5*gap*cm)

    def align(max,gap):
        return((converter(max) % (5*gap)) / 2)

    def scale(drawing):
        scaling_factor = object.grid_dist / drawing.width
        drawing.width = drawing.minWidth() * scaling_factor
        drawing.height = drawing.height * scaling_factor
        drawing.scale(scaling_factor, scaling_factor)
        return drawing

    def gridB(object,canvas,color,lineWidth,xlist,ylist):
        canvas.setStrokeColor(color)
        canvas.setLineWidth(lineWidth)
        canvas.grid(xlist,ylist)
        object.xStart=xlist[0]
        object.yStart=ylist[0]
        object.grid_dist = xlist[1] - xlist[0]
        xlist = list(dict.fromkeys(xlist))
        ylist = list(dict.fromkeys(ylist))
        xlist.pop()
        ylist.pop()
        l = 0
        for i, _ in enumerate(xlist):
            for j, _ in enumerate(ylist):
                if (l >= len(filepath)):
                    break
                drawing = scale(svg2rlg(filepath[l]))
                renderPDF.draw(drawing, canvas, xlist[i], ylist[j])
                l = l + 1
        canvas.setStrokeColor(gray, 0.8)
        canvas.setLineWidth(0.5)
        canvas.setDash([6, 3])
        gsl_x = []
        for i, _ in enumerate(xlist):
            if (i < len(xlist)-1):
                gsl_x.append(xlist[i] + ((xlist[i+1]-xlist[i])/2))
        gsl_x.append(gsl_x[-1] + (xlist[1]-xlist[0]))
        gsl_y = []
        for i, _ in enumerate(ylist):
            if (i < len(ylist)-1):
                gsl_y.append(ylist[i] + ((ylist[i+1]-ylist[i])/2))
        gsl_y.append(gsl_y[-1] + (ylist[1]-ylist[0]))

        for i in gsl_x:
            canvas.line(i, ylist[0], i, ylist[-1] + (ylist[1] - ylist[0]))
        for i in gsl_y:
            canvas.line(xlist[0], i, xlist[-1] + (xlist[1] - xlist[0]), i)

    def converter(px):
        return(px * 2.54 / 72)

    xylist(align(object.width,object.xgap),object.xlist,object.width,object.xgap,detailTF)
    xylist(align(object.height,object.ygap),object.ylist,object.height,object.ygap,detailTF)
    gridB(object,canvas,color,lineWidth,object.xlist,object.ylist)
