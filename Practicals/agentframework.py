# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:45:52 2022

@author: alexa
"""

import random
import csv
import requests
import bs4

#random.seed = 5

"""
# to get the below create_env function working, I first tested it in this format outside of agentframework:
def csv_func_test(input_file):
    file1 = input_file
    dataset = file1 
    list1 = []
    for row in dataset:
        rowlist=[]
        #print("new row")
        #print(row)
        for values in row:
            rowlist.append(values)
            #print(values) # test how values are read in
        #print(rowlist) # test how the row list looks
        list1.append(rowlist)
    return list1

input_file = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
environment = csv_func_test(input_file)
print(environment)
"""

def create_env(environment_file):
    #pass
    file1 = open(environment_file, newline="")
    dataset = csv.reader(file1, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
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
    return environment

class Agent():
# Special methods like the __init__ constructor and other class properties go here
    def __init__ (self, environment, name, agents, y=None, x=None): # self is a variable representing the object is injected into the call, traditionally called self (not a keyword)
        #pass
        if (y == None):
            self._y = random.randint(0,299)
        else:
            self._y = y #random.randint(0,299)
        if (x == None):
            self._y = random.randint(0,299)
        else:
            self._x = x #random.randint(0,299)
        self.environment = environment # the environment file read in through the create_env function
        self.energy = random.randint(250,2000) # starting off with random energy level
        self.name = name
        self.agents = agents # this is the list of agents
        self.movement = 1 # the movement speed
        
    # practising making a function inside the class        
    #def randomise(self):
        #self.y = random.randint(0,99)
        #self.x = random.randint(0,99)
    #def hi(self):
        #print("hello world")
    
    def check_other_agent(self):
        """
        function to check if the agents list is being passed into the agent class

        Returns
        -------
        None.

        """
        other_agent = self.agents[4]._x
        print(other_agent)  
    
    def __str__(self):
        """
        str method, overriding the default __str__ by returning the name variable which has been passed into the __init__ constructor above

        Returns
        -------
        String
            Name of agent

        """
        return str(self.name)
        
    def agent_status(self):
        """
        Returns the name, coordinates and energy value of an agent

        Returns
        -------
        String
            name
            x
            y
            energy

        """
        return str(self.name) + ", x=" + str(self._x) + ", y=" + str(self._y) + ", energy=" + str(self.energy)

# protecting the y and x variables behind get/set methods
    def get_y(self):
        """
        Get_y method. Returns the current value of self._y variable

        Returns
        -------
        Int
            the y value retrieved

        """
        return self._y
        
    def set_y(self, value):
        """
        Sets the self._y value

        Parameters
        ----------
        value : Int
            The y value to be set

        Returns
        -------
        None.

        """
        self._y = value
        
    def del_y(self):
        del self._y
# any code that retrieves the value of y will call get_y()
# any that assigns a value to y will call set_y()
    y = property(get_y, set_y, del_y, "y property")
        
    def get_x(self):
        return self._x
        
    def set_x(self, value):
        self._x = value
        
    def del_x(self):
        del self._x
    
    x = property(get_x, set_x, del_x, "x property")

    def move(self):
        #if self.energy > 0:
            if random.random() < 0.5:
                self._y = (self._y + self.movement) % 300
                #self.energy -= 1 # energy cost associated with movement (removed feature, could implement if more time but results were too chaotic)
            else:
                self._y = (self._y - self.movement) % 300
                #self.energy -= 1
            if random.random() < 0.5:
                self._x = (self._x + self.movement) % 300   
                #self.energy -= 1
            else:
                self._x = (self._x - self.movement) % 300
                #self.energy -= 1
        #else:
            #pass
            
    def eat(self):
        #pass
        if self.environment[self._y][self._x] > 10: # if the environment value is greater than 10
            self.environment[self._y][self._x] -= 10 # 10 is removed from the value
            self.energy += 10 # 10 is added to the agent's energy (Agent eats 10 units of environment)
        elif self.environment[self._y][self._x] > 0 < 10: # if the value is greater than 0 but less than 10
            self.energy += self.environment[self._y][self._x] # energy that value first, before it is changed by the next line (agent eats the value)
            self.environment[self._y][self._x] -= self.environment[self._y][self._x] # reducing the value to 0 by subtracting it from itself (agent has eaten the remainder)
        if self.energy > 500: # if agent's energy exceeds 500
            self.environment[self._y][self._x] += self.energy # the environment receives the energy value at current location
            self.energy -= (self.energy + 25) # the agent's energy loses the value (Agent was sick!)
    
    def distance_between(self, agent):
        return (((self._y - agent.y)**2) + ((self._x - agent.x)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        #print(neighbourhood)
        randint = random.random()
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent)
                if distance <= neighbourhood and randint > 0.5:
                    sum = self.energy + agent.energy
                    resource_share = sum / 2
                    #print(self, "and", agent, "are close enough to share resources, they share", resource_share, "units.")
                    self.energy = resource_share
                    agent.energy = resource_share
                    
    def breed_test(self, neighbourhood, environment, agents):
        """
        This was a function to test the breeding concept in the model. Quite unrealistic.

        Parameters
        ----------
        neighbourhood : int
            the neighbourhood parameter given at model initialisation
        environment : list
            the environment file read in at initialisation containing 300x300 grid of numeric values
        agents : list
            list of agents that have been created

        Returns
        -------
        None.

        """
        randint = random.randint(0,1000)
        if randint == 489 and self.environment[self._y][self._x] > 255: # the last condition is to reduce the frequency of reproduction, can be thought of as habitat quality (or a pile of puke)
            #print(randint) # testing how often the randint comes up, surprisingly often
            name = ("Agent " + str(len(agents)))
            print(name, "has been born")
            y = self._y
            x = self._x
            agents.append(Agent(environment, name, agents, y, x))
            
    """
    # this doesn't work well, creates agents too often but is part of me testing a more "realistic" interaction
    def breed_check(self, neighbourhood, environment, agents):
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent)
                breeding_ground = self.environment[self._y][self._x]
                if distance <= neighbourhood and self.energy > 150 and agent.energy > 150 and breeding_ground > 200:
                    print(distance, self.energy, agent.energy)
                    self.energy -= 25
                    agent.energy -= 25
                    name = ("Agent " + str(len(agents)))
                    y = self._y
                    x = self._x
                    #print("name")
                    #agents.append(Agent(environment, name, agents, y, x))
    """
    
    """
    # failed concept, kept to implement later
    def starve(self):
            if self.energy == 0:
                print(self, "has starved and died")
                self.agents.remove(self)
            else:
                pass
    """

# taking advantage of inheritence
class Predator(Agent): # creating a subclass of Agent to transfer attributes and methods
    def __init__ (self, environment, name, agents, y, x, predators): # self is a variable representing the object injected into the call, traditionally called self (not a keyword)
        #pass
        self.predators = predators
        super().__init__(environment, name, agents, y, x) # this pulls attributes and methods from the superclass (Agent)
        self.movement = 1.5 # re-defining a superclass attribute, predators should move faster
        """
        # no need for these, since they have been inherited from the Agent class
        self._y = random.randint(0,299) #None
        self._x = random.randint(0,299) #None
        self.environment = environment
        self.energy = 0
        self.name = name
        self.agents = agents
        self.predators = predators
        """
    def hunt_agent(self, neighbourhood):
        for agent in self.agents[:]: # traversing every object in a copy of the list, because the original list may be changed by this function (removal of agents)
            distance = self.distance_between(agent) # injecting self/predator into distance between function with agent as argument
            if distance <= neighbourhood: # if the distance is within the neighbourhood
                for i in range(int(agent.energy)): # predator will "drag down" its prey by draining energy
                    self._y = agent._y
                    self._x = agent._x
                    agent.movement = 0.1
                    agent.energy -= 1
                    self.energy += 1
                #print("Growl") # this was to test if the predators were created successfully and receiving arguments/parameters correctly
                print(agent, "has been eaten")
                self.agents.remove(agent)
                
                
        