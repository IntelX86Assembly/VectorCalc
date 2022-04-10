#IMPORT STATEMENTS
import math

####################################################################################################
class Vector2D_List:

#PROPERTIES FOR CLASS

    vectorList = []

####################################################################################################
# CONSTRUCTOR 

    def __init__(self):

####################################################################################################
# GETTERS

    def get_vector_list(self):
        return self.vectorList

####################################################################################################
# SETTERS 

#This method takes the elements of another list and adds them to vectorList.
#Used when you already have a list of vectors and you want this class to 
#take on this list as one of its properties.
    def set_vector_list(self, list):
        self.extend(list)

    def add_vector_to_list(self, vector)
        self.append(vector)
####################################################################################################

# METHODS

#TODO ADD METHODS FOR THIS LIST OF VECTORS AS NEEDED


#Gets user input from shell and adds vector2D objects to list
promptForUserInput(self, numVectors):
    #Instantiate objects and append to list
    for num in range(numVectors):
        #Gets the x and y component for one vector
        x_component = float(input("Please enter the x component of vector" + str(num + 1) + ": "))
        y_component = float(input("Please enter the y component of vector" + str(num + 1) + ": "))
        self.append(Vector2D_Components(x_component, y_component))


