#!/usr/bin/python2.7

Usage:
./FreeCADconverter

export PATH="$PATH:$PWD" find . -type f -name '*.step' -exec FreeCADconverter {} {}.fcstd \;

forum.freecadweb.org/viewtopic.php?t=3332







import sys
sys.path.insert(0, '/usr/lib/freecad/')
from FreeCAD import Base
from math import *

import os

import Part

import FreeCADGui

doc = FreeCAD.newDocument()
doc.addObject("Part::Feature","Part").Shape = Part.read(sys.argv[1])
doc.recompute()

#FreeCADGui.getDocument("Unnamed").getObject("Part").Visibility = True

App.getDocument("Unnamed").saveAs(str(sys.argv[2]))
exit()


