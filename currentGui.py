#IMPORT STATEMENTS

#imports the tkinter library for drawing gui
from tkinter import *

#Gives modern ttk framework widgets for gui
from tkinter import ttk

#Lets us draw message box pop up 
from tkinter import messagebox

#import the vector classes to instantiate vector objects
#and gain access to their properties and methods
from Vector2D import *

#This imports the class to handle graphing 2D vectors
from Vector2D_Graph import *
######################################################################

#Refreshes the frame and adds widgets back for plotting single vectors
def plotSingle2DVector(refreshFrame):

    def plotVector(vector_x, vector_y):
            #convert data from text boxes to float and store
            x_component = float(vector_x)
            y_component = float(vector_y)
            
            #Instantiate a vector with an x and y component from the 
            #Vector2D_Components class
            vector1 = Vector2D(x_component, y_component)

            #This creates a graph object and plots a single vector
            graph = Vector2D_Graph()
            graph.graphSingleVector(vector1)
   

    #clears the frame first before we add widgets back
    for widget in refreshFrame.winfo_children():
        widget.destroy()
    

    #Top Label widget
    ttk.Label(refreshFrame, text="Enter Vector Components", font="bold").grid(column=1, row=1, padx=(20,20), pady=(20,20))

    ##Label and input box for x component
    ttk.Label(refreshFrame, text="X-Component").grid(column=1, row=2)
    vector_x_entry = ttk.Entry(refreshFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3)
    
    #Label and input box for y component
    ttk.Label(refreshFrame, text="Y-Component").grid(column=1, row=4)
    vector_y_entry = ttk.Entry(refreshFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5)
 
    #Plots the vector on a graph
    button1 = ttk.Button(refreshFrame, text="Plot Vector", width = 20, command=lambda: plotVector(vector_x_entry.get(), vector_y_entry.get()))
    button1.grid(pady=(30,0), column=1, row=8)




#Refreshes the frame and adds widgets back for plotting multiple vectors
def plotMultiple2DVectors(refreshFrame):

    #When the user clicks the "Add Vector" button this method is called.
    #It takes a list and creates a new Vector2D object before adding it to
    #this list. In addition it displays the user entered values to the right
    #to keep track of what they are entering.
    vectorList = []
    def addVectorToList(vector_x, vector_y, vectorList, Frame):
        #Create a Vector2D object and add it to our list
        vectorList.append(Vector2D(float(vector_x), float(vector_y)))
        #The "vectors" variable holds the string displayed in the right column
        vectors = "" 
        counter = 1
        #For every vector in the list we are adding them to do the following
        for vector in vectorList:
            #Create a string that displays user entered values
            vectors = vectors + "\n" + "Vector " + str(counter) +  ":   X = " + str(vector.get_x_component()) + "   Y = " + str(vector.get_y_component()) 
            counter = counter + 1
        #Displays "vectors" string in gui
        listOfVectors = ttk.Label(Frame, text=vectors)
        listOfVectors.grid(padx=(40, 40), column=1, row=2)


    #Creates a graph object and calls method to graph the vectors
    #when the user clicks "Plot Vectors"
    def multiGraph(vectorList):
        graph = Vector2D_Graph()
        graph.graphMultipleVectors(vectorList)

    

    #clears the frame first before we add widgets back
    for widget in refreshFrame.winfo_children():
        widget.destroy()
    
    leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
    leftFrame.grid(column=0, row=0, sticky="nwes")

    rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
    rightFrame.grid(column=1, row=0, sticky = "nwes")

    ttk.Label(leftFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(leftFrame, text="X-Component").grid(column=1, row=2)
    vector_x_entry = ttk.Entry(leftFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3)
    
    #Label and input box for y component
    ttk.Label(leftFrame, text="Y-Component").grid(column=1, row=4)
    vector_y_entry = ttk.Entry(leftFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5)
 
    #TODO create list of vectors holding multiple 2D vector components so user can keep track of what they entered
    vectorLabel = ttk.Label(rightFrame, text="Current Vectors:")
    vectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
  
    #Add vector to list of vectors to graph
    button2 = ttk.Button(leftFrame, text="Add Vector", width = 20, command=lambda: addVectorToList(vector_x_entry.get(), vector_y_entry.get(), vectorList, rightFrame))

    button2.grid(column=1, row=6)

    #Plots the vectors on a graph.
    button3 = ttk.Button(leftFrame, text="Plot Vectors", width = 20, command=lambda: multiGraph(vectorList))
    button3.grid(pady=(30,0), column=1, row=7)
    
    


#Refreshes the frame and adds widgets back for plotting the resultant of vectors 
def resultant2DVector(refreshFrame):

    vectorList = []
    def addVectorToList(vector_x, vector_y, vectorList, Frame):
        #Create a Vector2D object and add it to our list
        vectorList.append(Vector2D(float(vector_x), float(vector_y)))
        #The "vectors" variable holds the string displayed in the right column
        vectors = "" 
        counter = 1
        #For every vector in the list we are adding them to do the following
        for vector in vectorList:
            #Create a string that displays user entered values
            vectors = vectors + "\n" + "Vector " + str(counter) +  ":   X = " + str(vector.get_x_component()) + "   Y = " + str(vector.get_y_component()) 
            counter = counter + 1
        #Displays "vectors" string in gui
        listOfVectors = ttk.Label(Frame, text=vectors)
        listOfVectors.grid(padx=(40, 40), column=1, row=2)

    def resultantGraph(vectorList):
        graph = Vector2D_Graph()
        graph.graphResultant(vectorList)
    

    #clears the frame first before we add widgets back
    for widget in refreshFrame.winfo_children():
        widget.destroy()

    leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
    leftFrame.grid(column=0, row=0, sticky="nwes")

    rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
    rightFrame.grid(column=1, row=0, sticky = "nwes")

    ttk.Label(leftFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(leftFrame, text="X-Component").grid(column=1, row=2)
    vector_x_entry = ttk.Entry(leftFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3)
    
    #Label and input box for y component
    ttk.Label(leftFrame, text="Y-Component").grid(column=1, row=4)
    vector_y_entry = ttk.Entry(leftFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5)
 
    #TODO create list of vectors holding multiple 2D vector components so user can keep track of what they entered
    vectorLabel = ttk.Label(rightFrame, text="Current Vectors:")
    vectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
  
    #Add vector to list of vectors to graph
    button2 = ttk.Button(leftFrame, text="Add Vector", width = 20, command=lambda: addVectorToList(vector_x_entry.get(), vector_y_entry.get(), vectorList, rightFrame))

    button2.grid(column=1, row=6)

    #Plots the vectors on a graph.
    button3 = ttk.Button(leftFrame, text="Find Resultant", width = 20, command=lambda: resultantGraph(vectorList))
    button3.grid(pady=(30,0), column=1, row=7)

#Refreshes the frame and adds widgets back for plotting the equilibrium vector to the resultant of vectors 
def equilibrium2DVector(refreshFrame):

    vectorList = []
    def addVectorToList(vector_x, vector_y, vectorList, Frame):
        #Create a Vector2D object and add it to our list
        vectorList.append(Vector2D(float(vector_x), float(vector_y)))
        #The "vectors" variable holds the string displayed in the right column
        vectors = "" 
        counter = 1
        #For every vector in the list we are adding them to do the following
        for vector in vectorList:
            #Create a string that displays user entered values
            vectors = vectors + "\n" + "Vector " + str(counter) +  ":   X = " + str(vector.get_x_component()) + "   Y = " + str(vector.get_y_component()) 
            counter = counter + 1
        #Displays "vectors" string in gui
        listOfVectors = ttk.Label(Frame, text=vectors)
        listOfVectors.grid(padx=(40, 40), column=1, row=2)

    def resultantGraph(vectorList):
        graph = Vector2D_Graph()
        graph.graphResultant(vectorList)
    

    #clears the frame first before we add widgets back
    for widget in refreshFrame.winfo_children():
        widget.destroy()

    leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
    leftFrame.grid(column=0, row=0, sticky="nwes")

    rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
    rightFrame.grid(column=1, row=0, sticky = "nwes")

    ttk.Label(leftFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(leftFrame, text="X-Component").grid(column=1, row=2)
    vector_x_entry = ttk.Entry(leftFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3)
    
    #Label and input box for y component
    ttk.Label(leftFrame, text="Y-Component").grid(column=1, row=4)
    vector_y_entry = ttk.Entry(leftFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5)
 
    #TODO create list of vectors holding multiple 2D vector components so user can keep track of what they entered
    vectorLabel = ttk.Label(rightFrame, text="Current Vectors:")
    vectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)
  
    #Add vector to list of vectors to graph
    button2 = ttk.Button(leftFrame, text="Add Vector", width = 20, command=lambda: addVectorToList(vector_x_entry.get(), vector_y_entry.get(), vectorList, rightFrame))

    button2.grid(column=1, row=6)

    #Plots the vectors on a graph.
    button3 = ttk.Button(leftFrame, text="Find Equilibrium Vector", width = 20, command=lambda: resultantGraph(vectorList))
    button3.grid(pady=(30,0), column=1, row=7)

def showHelp():
    response = '''Hello welcome to vector calc this program aids in the visualization of vectors as well as their calculations.

    Click on the Graph menu item and select an option to begin graphing vectors.

    The Calculations menu item is for performing calculations with vectors like adding or subtracting them.

    - To get started select a menu item and click on an option. You will be presented with input boxes for entering data.

    - Enter the vectors components i.e. their x, y, or z values as a number

    - Click on the button in the menu when finished to perform an action.

    - The program will then preform an action based on what menu option you have selected.
    '''

    #Creates popup to show user how to get started.  takes title and a message as parameters
    messagebox.showinfo("help", response)


####################################################################################################

#Creates main/root window by calling constructor.
root = Tk()

#Sets size and title of window
root.geometry("720x720")
root.title("VectorCalc")

#Creates a frame to put in window. This container is used to when selecting a menu option. When
#the user clicks on an option like "Plot 2D vector" the frame is deleted and a new one is created.
#Wigets are placed in this frame depending on the option selected.
refreshFrame = Frame(root, width=720, height=720)
refreshFrame.grid(column=0, row=0)


#Create the menu bar to act as container for menu buttons  
menuBar = Menu(root)

#We have to tell the root window to use menuBar as our menu
root.config(menu=menuBar)

#Instantiating Menu items to act as our buttons in the menu bar
graphButton = Menu(menuBar, tearoff = 0)
calcButton = Menu(menuBar, tearoff = 0)
helpButton = Menu(menuBar, tearoff = 0)

#Calls the add_cascade method to cause these buttons to show up in the menu.
#We instantiated them but we need to display them 
#This is similar to the grid() or pack() methods)
menuBar.add_cascade(label="Graph", menu=graphButton)
menuBar.add_cascade(label="Calculations", menu=calcButton)
menuBar.add_cascade(label="Help", menu=helpButton)

#Adds commands to the "Graph" menu button
graphButton.add_command(label="Plot single 2D vector", command=lambda: plotSingle2DVector(refreshFrame))
graphButton.add_command(label="Plot multiple 2D vectors", command=lambda: plotMultiple2DVectors(refreshFrame))

#Adds commands to the "Calculations" menu button
calcButton.add_command(label="Resultant 2D vector", command=lambda: resultant2DVector(refreshFrame))
calcButton.add_command(label="Find equlibrium 2D vector", command=lambda: equilibrium2DVector(refreshFrame))

#Adds command to the Help menu for getting help
helpButton.add_command(label="Get help", command=showHelp)

#Runs main window in a loop to make the gui interactive. (like moving the mouse and allowing actions to occur)
root.mainloop()
