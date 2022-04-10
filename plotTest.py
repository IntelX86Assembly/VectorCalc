#THIS PROGRAM PLOTS A USER SPECIFIED NUMBER OF VECTORS WITH USER SPECIFIED 
#COMPONENTS. WANT TO ADD FUNCTIONALLITY TO ADD VECTORS.

#IMPORT STATEMENTS
#import pyplot to plot the vectors in a graph
import matplotlib.pyplot as plotter

#import the vector classes to instantiate vector objects
#and gain access to their properties and methods
from Vector2D import *
#from vector2D_AngleForce import *

####################################################################################################
#CREATE VECTORS

#Ask user for the number of vectors to plot
numberOfVectors = int(input("Please enter the number of vectors to add together: "))

#Create a list to hold vector objects
vectorList = []

#Instantiate objects and append to list
for vectorNumber in range(numberOfVectors):
    #Gets the x and y component for one vector
    x_component = float(input("Please enter the x component of vector" + str(vectorNumber + 1) + ": "))
    y_component = float(input("Please enter the y component of vector" + str(vectorNumber + 1) + ": "))
    vectorList.append(Vector2D(x_component, y_component))

lengthList = len(vectorList)
####################################################################################################
#CREATE AND SHOW GRAPH FOR VECTORS
# Holds origin for graph
origin_points = [0] * lengthList

# Creates empty list. Will later be filled with the x and y components of vector objects
x_components = [0] * lengthList
y_components = [0] * lengthList

#scaleSize var used later to scale the user window properly
scaleSize = 0

#Used to iterate over the arrays of the x_component values and y_component values
vectorCounter = 0

#Used in a part of the for loop below that checks the values of the x_components list and y_components
#list and finds the biggest value in them. 
prevMax = 0

for vectorNum in vectorList:
    # Holds vector components
    x_components[vectorCounter] = vectorNum.get_x_component()
    y_components[vectorCounter] = vectorNum.get_y_component()
    vectorCounter =  vectorCounter + 1
  


    # Gets the max value of the current vector either x component or 
    # y component and checks if it is bigger than the largest vector
    # component. This is done to scale the window automatically.

    biggestComp= max(abs(vectorNum.get_x_component()), abs(vectorNum.get_y_component())) 
    if biggestComp > prevMax:
       prevMax = biggestComp
       scaleSize = prevMax

# Creating plot
plotter.quiver(origin_points, origin_points, x_components, y_components, angles = 'xy', scale_units= 'xy', scale=1)
plotter.title("Graph of Vectors")

# x-limit and the y-limit for the graph that is drawn
plotter.xlim(-2 * scaleSize, 2 * scaleSize)
plotter.ylim(-2 * scaleSize, 2 * scaleSize)

# Draws grid on the graph
plotter.grid()

# Displays the graph
plotter.show()


