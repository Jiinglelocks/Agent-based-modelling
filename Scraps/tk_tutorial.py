# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:36:25 2022

@author: Alex
"""
import tkinter
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk() # sets up the main application window
root.title("Feet to Meters") # gives title


mainframe = ttk.Frame(root, padding="3 3 12 12") # creating a frame widget to hold the contents of the UI
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # grid places it directly inside the main app window to match the newer themed widget
root.columnconfigure(0, weight=1) # these bits tell Tk that the frame should expand to fill any extra space if the window is resized
root.rowconfigure(0, weight=1)

# first widget is the entry to input the number of feet to convert
# need to create the widget itself, then place it onscreen
feet = StringVar() # StringVar class to be associated as the textvariable for the entry widget
# when creating widget, optionally provide configuration options (how wide for example)
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # Entry widget with configs: (parentwidget, width of entry, textvariable)
feet_entry.grid(column=2, row=1, sticky=(W, E)) # widgets don't auto appear on screen, Tk doesn't know where you want them, grid tells it, placing the widget in the appropriate column
# the sticky option to grid describes how widget should line up within the grid cell

# then do the same thing for the rest of the widgets
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# finishing touches
for child in mainframe.winfo_children(): # this bit walks through all widgets in the content frame and adds padding so they aren't scrunched together
    child.grid_configure(padx=5, pady=5)

feet_entry.focus() # this bit tells Tk to focus on our entry widget so the cursor will start in that field
root.bind("<Return>", calculate) # pressing Enter will run the calculate function

root.mainloop() # tell Tk to enter its event loop, necessary for everything to appear on screen