# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:39 2022

@author: alexa
"""
import random
import operator
import matplotlib.pyplot

# define model parameters
num_of_agents = 10
num_of_iterations = 2

# create blank list of agents
agents = []

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    #agents.append([99,1]) # testing boundary effect with yx values fixed near borders

# create first agent coords within a list
# append that list to the agents list
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,99),random.randint(0,99)])

print(agents) # test the append worked, see how it looks

#random_number = random.random()
#print(random_number) # this was to test if random_number variable changes once called in the loop

# to print current coordinates
print("y0 =", agents[0][0], "x0 =", agents[0][1])
print("y1 =", agents[1][0], "x1 =", agents[1][1])

# move each agent randomly
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            #agents[i][0] += 1
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            #agents[i][0] -= 1
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            #agents[i][1] += 1
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            #agents[i][1] -= 1
            agents[i][1] = (agents[i][1] - 1) % 100
"""            
the modulo operator % in the above loop gives the remainder of dividing two numbers.
example: if the random number is less than 0.5, the first element [0] of the
current agent [i] will increase by 1, and the resulting value will be divided by the boundary
limit (100). The modulo operator will leave the remainder, so if the agent[i][0] value reaches
101, the value will be set to 1, creating a torus effect.
print(99%100)
print(100%100)
print(101%100)
"""

# to print post-move coordinates
print("y0 =", agents[0][0], "x0 =",  agents[0][1])
print("y1 =", agents[1][0], "x1 =", agents[1][1])
print(agents)

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
distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print("Distance between =", distance)

# using matplotlib to plot the agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# loop to plot all the agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    #matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
    # when plotted twice, the last imposed colour is used:
    # matplotlib.pyplot.scatter(most_east[1], most_east[0], color='red')

matplotlib.pyplot.show()


    