# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:46:22 2022

@author: alexa
"""

import random

f = open("data2.html", "w")

f.write("<HTML>\n<BODY>\n")
f.write("<STYLE>\n")
f.write("TD {border: 1px solid black; padding: 15px;}\n")
f.write("TH {border: 1px solid black; padding: 15px;}\n")
f.write("</STYLE>\n")
f.write("<TABLE class=\'datatable\' id=\'yxz\'>\n")
f.write("<TR><TH>y</TH><TH>x</TH><TH>z</TH></TR>\n")

for i in range(100):
	y = random.randint(0,299)
	x = random.randint(0,299)
	z = random.randint(0,255)
	f.write("<TR><TD class=\'y\'>" + str(y) + "</TD>")
	f.write("<TD class=\'x\'>" + str(x) + "</TD>")
	f.write("<TD class=\'z\'>" + str(z) + "</TD></TR>\n")

f.write("</TABLE>\n</BODY>\n</HTML>")

f.close()