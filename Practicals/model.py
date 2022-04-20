# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:39 2022

@author: alexa
"""
"""
---- Agent-based Modelling ----

---- SECTION A ----
---- Model Setup ----
"""
import random
import operator
import tkinter
from tkinter import * # imports everything from tkinter module to call tkinter functions without prefixing them
from tkinter import ttk # newer themed widgets, importing just tkk itself means need to prefix anything inside that submodule.
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

# set random seed for reproducible results
random.seed = 5

# define model parameters
num_of_agents = 10
num_of_iterations = 10 #100
neighbourhood = 20
num_of_predators = 2

# first part of code for animation
# setting the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)


# code for calling csv read function from agentframework
environment_file = 'in.txt' #'test.txt'
environment = agentframework.create_env(environment_file)
#print(environment[2]) # testing that the create_env function read the text file correctly

"""
---- SECTION B ----
---- Agent Creation and Activity ----
"""
# create blank lists of agents and predators
agents = []
predators = []

for i in range(num_of_agents):
    name = ("Agent " + str(i)) # creating iterating agent name within name variable
    agents.append(agentframework.Agent(environment, name, agents)) # passing environment and name variables back into Agent class (making available to inner class functions)

# creating predators
for i in range(num_of_predators):
    name = ("Predator" + str(i))
    predators.append(agentframework.Predator(environment, name, agents, predators))

if num_of_predators > 0:
    print("There are",num_of_predators, "Predators about, Agents be careful!")

# printing out agent names to test __str__ override, see how name looks
# prints initial location and store info for each agent  
print("Initial agent info:")
for agent in agents:
    print(agent.agent_status())

# another part of animation code
def update(frame_number):
    fig.clear()

# move each agent randomly
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            random.shuffle(agents) # shuffle the list of agents to prevent artifacts

    
    for j in range(num_of_iterations):
        for i in range(num_of_predators):
            predators[i].move()
            #predators[i].hunt_agent(neighbourhood)

    """
    ---- SECTION C ----
    ---- Plotting and Visualisation ----
    """
    # set graph limits
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment)
    
    # loop to plot all the agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color='yellow')
        
    for i in range(num_of_predators):
        matplotlib.pyplot.scatter(predators[i]._x, predators[i]._y, color='red', marker='x')

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    canvas.draw()
#matplotlib.pyplot.show()

def quit_model():
    root.quit()
    root.destroy()

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



print("Agent updates:")
for agent in agents:
    print(agent.agent_status())
 
# testing the check_other_agent function to confirm the agents list is passing into the agent class correctly
#agents[0].check_other_agent()

"""
---- SECTION D ----
---- Agent Feedback and Metrics ----
"""

# legacy distance_between function that works with the distance list populating code below
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) + ((agents_row_a.x - agents_row_b.x)**2))**0.5
"""
# testing a way to slice lists to prevent repeating pairs
list = [1,5,4,7]
for i in range(len(list)):
  list2 = list[i+1:]
  for j in range(len(list2)):
      print(list[i],"-",list2[j])
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
---- SECTION E ----
---- Output files ----
"""
# write post-activity environment as a file at the end
file2 = open('out.txt', 'w', newline='')
writer = csv.writer(file2, delimiter=',')
for row in environment:
    writer.writerow(row)
file2.close()

# append a list with each agent's store value and sum them
stores_list = []
for agent in agents: 
    stores_list.append(agent.store)
stores_total = str(sum(stores_list))

# append a file with the total of agent's stores each time model is run
file3 = open('stores.txt', 'a', newline='')
appender = csv.writer(file3, delimiter=',')
file3.write("Total eaten: " + stores_total + "\n")
file3.close()

tkinter.mainloop()