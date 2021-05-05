# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 08:35:43 2021

@author: laura
"""

"""Creates an Agent class which generates the agents, and subsequently 
moves them, enables them to eat the environment, and share their 
co-ordinates with other agents within the agent class"""

import random




#Create the Agent Class
class Agent():
    #Create an object inside the function
    def __init__ (self, i, environment, agents, x, y):
        """
       Sets up the agents. 

        Parameters
        ----------
        i : TYPE Name
            This gives the agents names.
        environment : TYPE
            The environment that the agents are within.
        agents : TYPE
            The co-ordinates of the agents.
        x : TYPE
            The x co-ordinate of the agents.
        y : TYPE
            The y co-ordinate of the agents.

        Returns
        -------
        The agents name, x and y co-ordinates, and the store value.

        """
        self.i = i
        self.x = x
        self.y = y
        self.environment = environment  #get the envionrment into each agent
        self.agents = agents
        self.store = 0
        return


 
     
    def __str__(self):
        """
        Converting a number into a string variable.

        Returns
        -------
        TYPE String
            The name, x co-ord, y co-ord and store value as a string.

        """
        return "I am agent " + str(self.i) + " x=" + str(self.x) +\
        " y=" + str(self.y) + " store=" + str(self.store)  




    def share(self, neighbourhood):
        """
        Agents share their average distance between each other.

        Parameters
        ----------
        neighbourhood : TYPE Number
            The whether other agents, which are not itself, are within its 
            neighbourhood. Based on the two agents stores.

        Returns
        -------
        States whether or not agents are within the neighbourhood of another 
        agent using the print statements.

        """
        for i in range(len(self.agents)):
            agent = self.agents[i]
            if (agent.i != self.i):
                d = self.distance_between(agent)
                print("distance", d)
                
                if (d < neighbourhood):
                    ave = (self.store + agent.store) / 2
                    print(self, agent, "share ave", ave)
                    self.store = ave
                    agent.store = ave                
                else:
                    print("\n", "not share")
     
        
 
        
    def move(self):
        """
        Generates random co-ordinates for the agents, that lie within the
        environment.

        Returns
        -------
        Agent co-ordinates which are within the environment.

        """
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            #self.y = (self.y + 1) % 100
            self.y = (self.y - 1) % 100
            
        if random.random()  < 0.5:
            self.x = (self.x + 1) % 100
        else:
            #self.x = (self.x + 1) % 100
            self.x = (self.x - 1) % 100
 


   
    def eat(self):
        """
        Decides how much of the environment the agent will eat, if the 
        agent is greater than 10, or less than or equal to 10.

        Returns
        -------
        The amount of environment consumed by an agent.

        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10   
        return




    def distance_between(self, agent):
        """
        This calculates the distance between self and agent.

        Parameters
        ----------
        agent : TYPE Agent
            An agent to find the distance to/from.

        Returns
        -------
        TYPE Number
            Distance between self and agent.

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5  
 
    
 
