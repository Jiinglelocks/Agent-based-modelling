# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:39 2022

@author: alexa
"""
import random

#set up variables
y0 = random.randint(0, 99)
x0 = random.randint(0, 99)
y1 = random.randint(0, 99)
x1 = random.randint(0, 99)

#random_number = random.random()
#print(random_number) # this was to test if random_number variable changes once called in the loop

# to print current coordinates
print("y0 =", y0, "x0 =", x0)
print("y1 =", y1, "x1 =", x1)

# move agent randomly
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    y0 += 1
else:
    #print(random_number)
    #print(random.random())
    y0 -= 1
    
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    x0 += 1
else:
    #print(random_number)
    #print(random.random())
    x0 -= 1


# move agent randomly
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    y1 += 1
else:
    #print(random_number)
    #print(random.random())
    y1 -= 1
    
if random.random() < 0.5:
    #print(random_number)
    #print(random.random())
    x1 += 1
else:
    #print(random_number)
    #print(random.random())
    x1 -= 1

# to print post-code coordinates
print("y0 =", y0, "x0 =", x0)
print("y1 =", y1, "x1 =", x1)
    
""" # hardcoded values to check answer equation works
y0 = 0
x0 = 0
y1 = 4
x1 = 3
"""

"""
The Pythagorian/Euclidian distance is calculated as the difference in the y-direction between two points, squared, added to the squared difference in the x-direction, all then square rooted. 
"""

distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print("Distance between =", distance) 
    