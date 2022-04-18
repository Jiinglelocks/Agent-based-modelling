# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:39 2022

@author: alexa
"""
import random
import operator
import matplotlib.pyplot

agents = []

"""
#set up variables (no need, now using randint directly in 2D list)
y0 = random.randint(0, 99)
x0 = random.randint(0, 99)
y1 = random.randint(0, 99)
x1 = random.randint(0, 99)

"""

# create first agent coords within a list
# append that list to the agents list
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
print(agents) # test the append worked, see how it looks

#random_number = random.random()
#print(random_number) # this was to test if random_number variable changes once called in the loop

# to print current coordinates
print("y0 =", agents[0][0], "x0 =", agents[0][1])
print("y1 =", agents[1][0], "x1 =", agents[1][1])

# move agent randomly
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    agents[0][0] += 1
else:
    #print(random_number)
    #print(random.random())
    agents[0][0] -= 1
    
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    agents[0][1] += 1
else:
    #print(random_number)
    #print(random.random())
    agents[0][1] -= 1

# move agent randomly
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    agents[1][0] += 1
else:
    #print(random_number)
    #print(random.random())
    agents[1][0] -= 1
    
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    agents[1][1] += 1
else:
    #print(random_number)
    #print(random.random())
    agents[1][1] -= 1

# to print post-move coordinates
print("y0 =", agents[0][0], "x0 =",  agents[0][1])
print("y1 =", agents[1][0], "x1 =", agents[1][1])

# max function gets each element of agent list, each of which is a list too
# operator.itemgetter(1) gets the second element of each agent in the agent list
# so the following gives us the max in the x direction.

most_east = max(agents, key=operator.itemgetter(1))
print("Furthest east is:", most_east)
print(most_east[0], most_east[1]) # testing access to parts of the most_east variable
    
"""
The Pythagorian/Euclidian distance is calculated as the difference in the y-direction between two points, squared, added to the squared difference in the x-direction, all then square rooted. 
"""
distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print("Distance between =", distance)

# using matplotlib to plot the agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
# when plotted twice, the last imposed colour is used:
matplotlib.pyplot.scatter(most_east[1], most_east[0], color='red')
matplotlib.pyplot.show()


    