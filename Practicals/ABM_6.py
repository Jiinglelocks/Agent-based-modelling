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
import matplotlib.pyplot
import agentframework
import csv

# set random seed for reproducible results
#random.seed = 0

#a = agentframework.Agent()
#print(type(a))
#print(isinstance(a, agentframework.Agent))
#a.hi()
# testing the move() function by printing coords pre and post move
#print(a.y, a.x)
#a.move()
#print(a.y, a.x)

"""
# define distance function (pre-agentframework version)
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
"""
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) + ((agents_row_a.x - agents_row_b.x)**2))**0.5

# define model parameters
num_of_agents = 10
num_of_iterations = 10000 #100

"""
# initial code for calling csv read function from agentframework
environment_file = 'in.txt' #'test.txt'
agentframework.create_env(environment_file)
"""
# reader to open the environment file 'in.txt'
# gives data as a list of lists
file_to_open = 'in.txt' #'test.txt'
file1 = open(file_to_open, newline="")
dataset = csv.reader(file1, delimiter=',', quoting=csv.QUOTE_NONNUMERIC) # the last kwarg converts the data to float

# creating the environment by appending input file values to a 2D list
environment = []
for row in dataset:
    rowlist=[]
    #print("new row")
    #print(row)
    for values in row:
        rowlist.append(values)
        #print(values) # test how values are read in
    #print(rowlist) # test how the row list looks
    environment.append(rowlist)
file1.close()
#print(environment[0:2]) # print a small slice of the environment list

"""
---- SECTION B ----
---- Agent Creation and Activity ----
"""
# create blank list of agents
agents = []

# create first agent coords within a list
# append that list to the agents list
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,99),random.randint(0,99)])

for i in range(num_of_agents):
    #agents.append([random.randint(0,100),random.randint(0,100)])
    #agents.append([99,1]) # testing boundary effect with yx values fixed near borders
    #agents.append(agentframework.Agent())
    name = ("Agent " + str(i)) # creating iterating agent name within name variable
    agents.append(agentframework.Agent(environment, name)) # passing environment and name variables back into Agent class (making available to inner class functions)

# printing out agent names to test __str__ override, see how name looks
# prints initial location and store info for each agent  
for agent in agents:
    #print("xy: " + str(agent.x) + "," + str(agent.y) + " store = " + str(agent.store)) alternate way of presenting name and location info (now inside agentframework)
    print(agent)

#random_number = random.random()
#print(random_number) # this was to test if random_number variable changes once called in the loop

# to print current coordinates
#print("y0 =", agents[0][0], "x0 =", agents[0][1])
#print("y1 =", agents[1][0], "x1 =", agents[1][1])

# move each agent randomly
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

"""            
the modulo operator % in the above loop gives the remainder of dividing two numbers.
example: if the random number is less than 0.5, the first element [0] of the
current agent [i] will increase by 1, and the resulting value will be divided by the boundary
limit (100). The modulo operator will leave the remainder, so if the agent[i][0] value reaches
101, the value will be set to 1, creating a torus effect (agent leaves graph/frame to the right 
and enters on the left instead of disappearing).
"""
# testing the modulo operator
#print(99%100)
#print(100%100)
#print(101%100)

# to print post-move coordinates
#print("y0 =", agents[0][0], "x0 =",  agents[0][1])
#print("y1 =", agents[1][0], "x1 =", agents[1][1])
#print(agents)

# print final location and store info for each agent
for agent in agents:
    print(agent)
 

"""
---- SECTION C ----
---- Agent Feedback and Metrics ----
"""

# max function gets each element of agent list, each of which is a list too
# operator.itemgetter(1) gets the second element of each agent in the agent list
# so the following gives us the max in the x direction.

"""
most_east = max(agents, key=operator.itemgetter(1))
print("Furthest east is:", most_east)
print(most_east[0], most_east[1]) # testing access to parts of the most_east variable
""" 

"""
The Pythagorian/Euclidian distance is calculated as the difference in the y-direction between two points, squared, added to the squared difference in the x-direction, all then square rooted. 
"""
#distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#distance = distance_between(agents[0], agents[1])
#print("Distance between =", distance)

"""
# define an empty distances list, then check the distances between each agent
# in the agents list. Prevents checking against itself (if row_a does not equal row_b)
# appends each distance to the distance list.
distances = []
for agents_row_a in agents:
        print("distance between", agents_row_a)
        for agents_row_b in agents:
            if agents_row_a != agents_row_b:
                distance = distance_between(agents_row_a, agents_row_b)
                print("and", agents_row_b, "=" , distance)
                distances.append(distance)   
"""

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
        print("distance between", agents[agents_row_a].y,",",agents[agents_row_a].x)
        agents2 = agents[agents_row_a+1:]
        for agents_row_b in range(len(agents2)):
                #print(agents[agents_row_a], "-", agents2[agents_row_b]) # testing to see if pairs are truly not repeated
                distance = distance_between(agents[agents_row_a], agents2[agents_row_b]) # no need to specify .y and .x here because it's specified in the distance_between function
                print("and", agents2[agents_row_b].y,",", agents2[agents_row_b].x, "=" , distance)
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
# testing how nested loops access parts of a list
for agents_row_a in agents:
    for agents_row_b in agents:
        for agents_row_c in agents:
            print(agents_row_a[0], agents_row_b[0], agents_row_c[0]) # return only the first element of three agents
            #print(agents_row_a[1], agents_row_b[1], agents_row_c[1]) # return the second element
            #print(agents_row_a[2], agents_row_b[2], agents_row_c[2]) # this should return index out of range because there is no [2] element in the sublist (only [0] and [1])
"""

"""
---- SECTION D ----
---- Plotting and Visualisation ----
"""
# set graph limits
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment)
# loop to plot all the agents
for i in range(num_of_agents):
    #matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
    # when plotted twice, the last imposed colour is used:
    # matplotlib.pyplot.scatter(most_east[1], most_east[0], color='red')
    #matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

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

    