# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:39 2022

@author: alexa
"""
import random
import operator
import matplotlib.pyplot

# define distance function
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
 
# define model parameters
num_of_agents = 10
num_of_iterations = 2 #100

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
# testing a way to slice lists so that
list = [1,5,4,7]
for i in range(len(list)):
  list2 = list[i+1:]
  for j in range(len(list2)):
      print(list[i],"-",list2[j])
"""

# another solution with the addition of preventing repeated testing of pairs of agents
# makes use of list slicing to only calculate distances between agents_row_a and everything 
# after it this also prevents testing agent against itself
distance_list = []
for agents_row_a in range(len(agents)-1):
        print("distance between", agents[agents_row_a])
        agents2 = agents[agents_row_a+1:]
        for agents_row_b in range(len(agents2)):
                #print(agents[agents_row_a], "-", agents2[agents_row_b])
                distance = distance_between(agents[agents_row_a], agents2[agents_row_b])
                print("and", agents2[agents_row_b], "=" , distance)
                distance_list.append(distance)
                
# finding max and min distances
max_dist = max(distance_list)
min_dist = min(distance_list)
print("number  of distances:", len(distance_list))           
#print(distance_list)     
print("max distance was:", max_dist)
print("min distance was:", min_dist)

# figured out how to prevent testing agents against self. Could
# not figure out how to prevent repeating pairs.

"""
# testing how nested loops access parts of a list
for agents_row_a in agents:
    for agents_row_b in agents:
        for agents_row_c in agents:
            print(agents_row_a[0], agents_row_b[0], agents_row_c[0]) # return only the first element of three agents
            #print(agents_row_a[1], agents_row_b[1], agents_row_c[1]) # return the second element
            #print(agents_row_a[2], agents_row_b[2], agents_row_c[2]) # this should return index out of range because there is no [2] element in the sublist (only [0] and [1])
"""

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


    