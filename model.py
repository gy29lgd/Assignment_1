# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:09:56 2021

@author: laura
"""

"""Code to generate agents, which move, eat and interact with other agents,
 within an environment. A figure window is produced containing an animation of
 the agents movements in the environment"""

import requests
import bs4
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv
import tkinter
import matplotlib.animation
from multiprocessing import Process
import time

#Code starting statement
print("Start")
start = time.time() #start the run timer
print("Timer started")

# Set a seed to get a reproducable result
#random.seed(0)
random.seed(4)




"""Create the environment"""
#Read in csv file by: reading in the in.text file and convert it into a 
#csv file, this generates raster data by creating a list of lists
environment = []                #make empty list called 'environment'
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                #make second empty list called 'rowlist'				
    environment.append(rowlist) #append rowlist to environment list	
    for value in row:
        rowlist.append(value)   #append values to row list			




"""Downloading x and y data from the web: data.html"""
td_ys = []  #empty list for y co-ordinate data
td_xs = []  #empty list for x co-ordinate data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/'\
                 'practicals/python/agent-framework/part9/data.html')
print("Data obtained from:", 'http://www.geog.leeds.ac.uk/courses/\
      computing/practicals/python/agent-framework/part9/data.html')
content = r.text                                #contents of table into text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})    #finds y co-ords in table
td_xs = soup.find_all(attrs={"class" : "x"})    #finds x co-ords in table
print("td_ys values")
print(td_ys)                                    #prints y co-ordinates
print("td_xs values")
print("\n", td_xs)                              #prints x co-ordinates                          




"""Create a figure for animating the agents"""
fig = matplotlib.pyplot.figure(figsize=(5, 5))  #empty figure
ax = fig.add_axes([0, 0, 1, 1]) #figure axes
print(fig)  #print figure size
print(ax)   #print figure axes




"""Setup the agents"""
#Number of agents
num_of_agents = 100

#Number of repeats the agents will go through within the For-Loop
num_of_iterations = 10

#Agents object
agents = []

#Create a neighbourhood for each agent, this is 20 units distance
neighbourhood = 20




"""Create the agents"""
#For-Loop to append the agents to move randomly within the environment
#ranging from 0 to 99
print("Create Agents")
#Print the co-ordinates for the agents with co-ordinates from data.html
for i in range(num_of_agents):
    y = int(td_ys[i].text)  #make td_ys into integer data
    x = int(td_xs[i].text)  #make td_xs into integer data
    agents.append(agentframework.Agent(i, environment, agents, x, y))
print(i)                    #prints number of agents from data.html minus 1
i = i + 1

#Below prints co-ordinates for an agent with known co-ordinates
agents.append(agentframework.Agent(i, environment, agents, 50, 50))
i = i + 1
#Below prints co-ordinates for another agent with known co-ordinates
agents.append(agentframework.Agent(i, environment, agents, 51, 51))
print("num_of_agents", num_of_agents)   #prints agents with co-ordinates from data.html

num_of_agents = len(agents)
print("num_of_agents", num_of_agents)   #prints total number of agents
for i in range(num_of_agents):
    print("Agent Starting co-ordinates, and store value")
    print(agents[i])                    #prints the agents number, x and 
                                        #y co-ords and store number

print("\n", "Create plot")


#continue to run the code
carry_on = True




#create the animation figure
def update(frame_number):
    """
    The frames for the iterations of the agents.

    Parameters
    ----------
    frame_number : TYPE Number
        The number of frames needed to produce the number of iterations of the 
        agents.

    Returns
    -------
    None.

    """
    
    fig.clear()
    global carry_on
    
    print("")
    print("Do iterations")
    for j in range (num_of_iterations):
        print("Iteration", j)   #The iteration number
    for i in range (num_of_agents):
        random.shuffle(agents)          #Randomises order agents are processed 
        agents[i].move()                #moves agents within environment
        agents[i].eat()                 #agents eat their environment
        agents[i].share(neighbourhood)  #agents share their neighbourhoods
        agents[i].store
        print()                         #Prints the move, eat and neighbourhood 
        break

    #Plot the agents locations, within the 99x99 unit environment
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)




def gen_function(b = [0]):
    """
    Ensures the agents have 'eaten' at least a set amount of environment

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    TYPE
        DESCRIPTION.

    """
    a = 10
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 25) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        print("a is equal to", a)
        print("Agents store is", agents[i].store) #store value




def runAnimation():
    """
    Shows the agents moving and eating their environment in an animation.

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    wait_fig()
    return




def wait_fig(): 
    """
    A control function to wait until the figure is closed before, the next 
    set of code is run.

    Returns
    -------
    None.

    """
    # Block the execution of the code until the figure is closed.
    # This works even with multiprocessing.
    if matplotlib.pyplot.isinteractive():
        matplotlib.pyplot.ioff() # this is necessary in mutliprocessing
        matplotlib.pyplot.show(block=False)
    else:      
        matplotlib.pyplot.show(block=False)
    matplotlib.pyplot.close()
    return    




def main():
    """
    The final stage of running the code, which prints the final agent 
    co-ordinates and store values.

    Returns
    -------
    None.

    """

    if __name__ != '__main__': return                      
    
    
    p = Process(target=runAnimation())
    p.start()
    print('hello', flush = True) #tests the main function is running

    for i in range(3): #prints world three times
        print('world', flush = True)    
        time.sleep(1)
        
    matplotlib.pyplot.close()   #close the figure
    
    #The final agent co-ordinates
    for i in range (num_of_agents):
        agents[i].x, agents[i].y
        print("\n", "Agent final co-ordinates and store value:", agents[i]) 
    
    
    end = time.time() # stop the run timer
    print("Stop timing")
    print("Run time in seconds", end - start)   #calculate the run time
    #Code end statement
    print("End")




def run():
    """
    Enables the animation to be drawn and run

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, 
               frames=gen_function, repeat=False)
    canvas.draw()




"""Create a GUI showing the environment figure with the agents in a window"""
root = tkinter.Tk()
root.wm_title("Model")  #Title of the window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)                           #Add a menu bar
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)                     
menu_bar.add_cascade(label="Model", menu=model_menu)    #Add Model tab in menu 
                                                        #bar
model_menu.add_command(label="Run model", command=run)  #Add run model option 
                                                        #in Model tab




def exiting(): 
    """
    When the model window is closed, it causes the code to continue 

    Returns
    -------
    None.

    """
    root.quit()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exiting)

tkinter.mainloop()	#wait for interaction




main()  #run the main() function











