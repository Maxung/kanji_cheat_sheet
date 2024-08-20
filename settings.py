#!/usr/bin/env python3

from reportlab.lib.pagesizes import *
from reportlab.lib.colors import *

class Settings():

    def __init__(self):
        self.filename="MyGraphPaper" #no need to assign a file extention
        self.size=A4 #check the default setting below
        self.xgap=0.5 #in cm
        self.ygap=0.5 #in cm

        #Minor line setting:
        self.colorMinor=black #check the default setting below
        self.lineWidthMinor=0.5

        #Major line setting: if u dont want the major grid, set the majorLine=False
        self.majorLine=True
        self.colorMajor=black #check the default setting below
        self.lineWidthMajor=1
