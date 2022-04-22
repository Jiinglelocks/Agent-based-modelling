# -*- coding: utf-8 -*-
"""
@author: Alex Camilleri
"""
"""
---- Agent-based Modelling
---- GEOG5003M Programming for Geographical Information Analysis
---- Model
"""

"""
---- IMPORTS
"""

import random
import operator
import tkinter # interface library
from tkinter import * # imports everything from tkinter module to call tkinter functions without prefixing them
from tkinter import ttk # newer themed widgets, importing just tkk itself means need to prefix anything inside that submodule.
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework # my module to make the model work
import csv
import requests # make http requests
import bs4 # BeautifulSoup

"""
---- MODEL FUNCTIONS
"""

def update(frame_number): # function for all agent and predator "activity" which is passed into the animation function
    fig.clear()
    for j in range(num_of_iterations): # each iteration of the model will do the following
        for i in range(len(agents[:])): # agent activity
            agents[i].move() # these are activities, methods found within the Agent class
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            #agents[i].starve() # doesn't work well, see agentframework
            #agents[i].breed_check(neighbourhood, environment, agents) # doesn't work well, see agentframework docs
            agents[i].breed_test(neighbourhood, environment, agents) # rudimentary reproduction, see agentframework docs
            random.shuffle(agents) # shuffle the list of agents to prevent artifacts

    for j in range(num_of_iterations):
        for i in range(num_of_predators): # predator activity
            predators[i].move() # an agent (Super class) method
            predators[i].hunt_agent(neighbourhood) # a predator (Sub class) method
            #predators[i].starve() # doesn't work well, see agentframework

    matplotlib.pyplot.ylim(0, 300) # the following is to plot the agents each "frame" of the animation
    matplotlib.pyplot.xlim(0, 300) # set graph limits
    matplotlib.pyplot.imshow(environment)
    for i in range(len(agents)): # loop to plot all the agents
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color='yellow') # agents are yellow, default markers
    for i in range(num_of_predators):
        matplotlib.pyplot.scatter(predators[i]._x, predators[i]._y, color='red', marker='x') # predators are red x's

def run():
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    #animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) # attempted gen_function but could not get it working
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.draw()
#matplotlib.pyplot.show() # removed this because the plot will be occurring within the interface frame/canvas

def quit_model(): # to quit the model, accessed from the main menu bar in the model frame/canvas
    root.quit() # exit mainloop but preserve interpreter and widgets, can execute code to further interact with widgets
    root.destroy() # destroy all widgets and exit mainloop
    
def output_env(): # a post-activity report function
    # write post-activity environment as a file at the end
    print("writing post-activity environment to text file")
    file2 = open('out.txt', 'w', newline='')
    writer = csv.writer(file2, delimiter=',')
    for row in environment:
        writer.writerow(row)
    file2.close()
    
def output_energy(): # another post-activity report function
# append a list with each agent's energy value and sum them
    print("writing agents' total energy to text file")
    energy_list = []
    for agent in agents:
        energy_list.append(agent.energy)
    energy_total = str(sum(energy_list))
    
    # append a file with the total of agent's energys each time model is run
    file3 = open('energy.txt', 'a', newline='')
    #appender = csv.writer(file3, delimiter=',')
    file3.write("Total eaten: " + energy_total + "\n")
    file3.close()

"""
---- MODEL PARAMETERS
"""

# define model parameters
num_of_agents = 10
num_of_predators = 2
num_of_iterations = 100 #100 # number of times the model will be run
neighbourhood = 20 # neighbourhood is the distance within which any agent/predator interaction will occur

#random.seed = 5 # set random seed for reproducible results during build/testing

"""
---- SETTING THE FIGURE
"""

fig = matplotlib.pyplot.figure(figsize=(7, 7)) # first part of code for animation sets up the figure
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

"""
---- SETTING ENVIRONMENT
"""

environment_file = 'in.txt' #'test.txt' # the environment should be a 300x300 grid of values as a text file
environment = agentframework.create_env(environment_file) # calling csv read function from agentframework
#print(environment[2]) # testing that the create_env function read the text file correctly

"""
---- INITIALISE AGENTS & PREDATORS
"""
"""
In this series of blocks the initial y and x values for the agents/predators is scraped from a html table hosted on my github
The agents and predators lists are populated
Some feedback is provided on the number of predators
"""

# web scrape initial y and x values using BeautifulSoup
#r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html') # make a http request inside a response variable 'r'
r = requests.get('https://jiinglelocks.github.io/Agent-based-modelling/Model/data2.html') # pulling the initial yx values from a generated html table
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser') # make the soup! passing the text from the http request into a BeautifulSoup object which represents it as a nested data structure
#print(soup.prettify()) # checking out the html in an indented format
td_ys = soup.find_all(attrs={"class" : "y"}) # finds all rows with specified class, energys in a list including tags
td_xs = soup.find_all(attrs={"class" : "x"})
#print(int(td_ys[0].text)) # printing out a value at position [0] to see how it looks

y_values = [] # the following strips out the integer values from the td_ys and td_xs lists and appends them to a blank list
for row in td_ys:
    #print(int(row.text))
    y_values.append(int(row.text)) # for example, now instead of <td class="y">93</td> the value will be 93
x_values = []
for row in td_xs:
    x_values.append(int(row.text))
#print(y_values) # checking how it looks
#print(x_values)

# create blank lists of agents and predators
agents = []
predators = []

for i in range(num_of_agents): # creating agents
    y = y_values[i] # I used provided html generator code to increase the integers generated in the source html to max value 299 (see Appendix 2)
    x = x_values[i]
    name = ("Agent " + str(i)) # creating iterating agent name and number within name variable
    agents.append(agentframework.Agent(environment, name, agents, y, x)) # arguments are passing these variables back into Agent class (making available to inner class functions)
    random.shuffle(y_values) # shuffling the y and x values lists to make pseudo-random starts
    random.shuffle(x_values)
    
for i in range(num_of_predators): # creating predators
    y = y_values[i] 
    x = x_values[i]
    name = ("Predator" + str(i))
    predators.append(agentframework.Predator(environment, name, agents, y, x, predators)) # appending an instance of the Predator subclass to a separate predators list
    random.shuffle(y_values)
    random.shuffle(x_values)
    
if num_of_predators < 0: # some conditional feedback on the initial predator situation
    ("Error: cannot have negative predators")
elif num_of_predators == 1:
    ("There is a predator about, Agents be careful!")
elif num_of_predators > 1:
    print("There are",num_of_predators, "Predators about, Agents be careful!")
else:
    print("No predators, Agents relax...")

"""
---- GUI SETUP
"""
"""
Makes use of tkinter, sets the matplotlib figure (fig) inside a tkinter canvas
"""

root = tkinter.Tk()
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Quit", command=quit_model)

tkinter.mainloop()

# calling post-activity report functions outside the tkinter mainloop
output_env()
output_energy()

"""
---- APPENDIX 1
"""
"""
Below is some legacy code and some concept testing
It is not positioned in a way that it will work with the current model setup 
but here for evidence of some of my exploration/testing

"""

"""
# printing out agent names to test __str__ override, see how name looks
# prints initial location and energy info for each agent  
print("Initial agent info:")
for agent in agents:
    print(agent.agent_status())
"""

"""
# testing the agent status function, not practical as it puts loads of outputs in the console
print("Agent updates:")
for agent in agents:
    print(agent.agent_status())
"""

"""
# testing the check_other_agent function to confirm the agents list is passing into the agent class correctly
agents[0].check_other_agent()
"""

"""
# legacy distance_between function that works with the distance list populating code below
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) + ((agents_row_a.x - agents_row_b.x)**2))**0.5
"""

"""
# testing a way to slice lists to prevent repeating pairs
list = [1,5,4,7]
for i in range(len(list)): # problematic because it still uses the last agent in the list
  list2 = list[i+1:]
  for j in range(len(list2)):
      print(list[i],"-",list2[j])
"""

"""
# another solution with the addition of preventing repeated testing of pairs of agents
# makes use of list slicing to only calculate distances between agents_row_a and everything 
# after it. this also prevents testing agent against itself
distance_list = []
for agents_row_a in range(len(agents)-1): # -1 prevents the last agent in the list from being printed on its own
        #print("distance between", agents[agents_row_a].y,",",agents[agents_row_a].x)
        agents2 = agents[agents_row_a+1:]
        for agents_row_b in range(len(agents2)):
                #print(agents[agents_row_a], "-", agents2[agents_row_b]) # testing to see if pairs are truly not repeated
                distance = distance_between(agents[agents_row_a], agents2[agents_row_b]) # no need to specify .y and .x here because it's specified in the distance_between function
                #print("and", agents2[agents_row_b].y,",", agents2[agents_row_b].x, "=" , distance)
                distance_list.append(distance)
                
# finding max and min distances from the created distance list
max_dist = max(distance_list)
min_dist = min(distance_list)
print("number  of distances:", len(distance_list))           
#print(distance_list)     
print("max distance was:", max_dist)
print("min distance was:", min_dist)

#print(agents[0].environment[agents[0].y][agents[0].x])
"""

"""
---- APPENDIX 2
"""
"""
Also included the altered html generator code which was provided in the course materials
Can be used to generate a new html page of initial values or adapted for something else
I have # commented where I altered the code
"""

"""
#import random

f = open("data2.html", "w")

f.write("<HTML>\n<BODY>\n")
f.write("<STYLE>\n")
f.write("TD {border: 1px solid black; padding: 15px;}\n")
f.write("TH {border: 1px solid black; padding: 15px;}\n")
f.write("</STYLE>\n")
f.write("<TABLE class=\'datatable\' id=\'yxz\'>\n")
f.write("<TR><TH>y</TH><TH>x</TH><TH>z</TH></TR>\n")

for i in range(100):
	y = random.randint(0,299) # I altered
	x = random.randint(0,299) # these bits (changed 99 to 299)
	z = random.randint(0,255)
	f.write("<TR><TD class=\'y\'>" + str(y) + "</TD>")
	f.write("<TD class=\'x\'>" + str(x) + "</TD>")
	f.write("<TD class=\'z\'>" + str(z) + "</TD></TR>\n")

f.write("</TABLE>\n</BODY>\n</HTML>")

f.close()
"""
