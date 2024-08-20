#!/usr/bin/env python

from reportlab.pdfgen import canvas
from grid import *
from settings import Settings
import sys

filepath = []

if (len(sys.argv) > 1):
	kanji_list = sys.argv[1]
	kanji_list = kanji_list.replace(" ", "")
	for i in kanji_list:
		filepath.append("/home/max/Downloads/kanji/" + hex(ord(i)).replace("x", "") + ".svg")

pages = 1
for i in range(0, len(filepath), 88):
	#Create a canvas
	setting=Settings()
	cSpec=canvasSpec(setting)
	c = canvas.Canvas("kanji-"+str(pages)+".pdf",cSpec.size)
	#Footer
	c.setFont("Times-Roman", 6)
	c.drawString(539, 7, "Created by Maxung")
	if setting.majorLine==True:
		draw(cSpec,0,c,setting.colorMajor,setting.lineWidthMajor, filepath[i:i+88])

	pages = pages + 1
	c.showPage()
	c.save()
