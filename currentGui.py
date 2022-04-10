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
            x_component = float(vector_x)
            y_component = float(vector_y)
            #Instantiate a vector with an x and y component from the 
            #Vector2D_Components class
            vector1 = Vector2D(x_component, y_component)

            #This creates a graph object and plots a single vector
            graph = Vector2D_Graph()
            graph.graphSingleVector(vector1)

    for widget in refreshFrame.winfo_children():
        widget.destroy()
    
    #Top Label
    ttk.Label(refreshFrame, text="Enter Vector Components", font="bold").grid(column=1, row=1, pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(refreshFrame, text="X-Component").grid(column=1, row=2, sticky=(W))
    vector_x_entry = ttk.Entry(refreshFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3, sticky=(W, E))
    
    #Label and input box for y component
    ttk.Label(refreshFrame, text="Y-Component").grid(column=1, row=4, sticky=(W))
    vector_y_entry = ttk.Entry(refreshFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5, sticky=(W, E))
 
    #Plots the vector on a graph
    button1 = ttk.Button(refreshFrame, text="Plot Vector", command=lambda: plotVector(vector_x_entry.get(), vector_y_entry.get()))
    button1.grid(pady=(30,0), column=1, row=8, sticky=(W,E))


 
    

#Refreshes the frame and adds widgets back for plotting multiple vectors
def plotMultiple2DVectors(refreshFrame):

    def addVectorToList(vector_x, vector_y, vectorList):
        vectorList.append(Vector2D(float(vector_x), float(vector_y)))
        for vector in vectorList:
                print(vector.printComponents())

    def multiGraph(vectorList):
        graph = Vector2D_Graph()
        graph.graphMultipleVectors(vectorList)

    
    vectorList = []

    for widget in refreshFrame.winfo_children():
        widget.destroy()

    ttk.Label(refreshFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(refreshFrame, text="X-Component").grid(column=1, row=2, sticky=(W))
    vector_x_entry = ttk.Entry(refreshFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3, sticky=(W, E))
    
    #Label and input box for y component
    ttk.Label(refreshFrame, text="Y-Component").grid(column=1, row=4, sticky=(W))
    vector_y_entry = ttk.Entry(refreshFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5, sticky=(W, E))
   
    #Add vector to list of vectors to graph
    button2 = ttk.Button(refreshFrame, text="Add Vector", command=lambda: addVectorToList(vector_x_entry.get(), vector_y_entry.get(), vectorList))

    button2.grid(column=1, row=6, sticky=(W,E))

    #Plots the vectors on a graph.
    button3 = ttk.Button(refreshFrame, text="Plot Vectors", command=lambda: multiGraph(vectorList))
    button3.grid(pady=(30,0), column=1, row=7, sticky=(W,E))
    
    



#Refreshes the frame and adds widgets back for plotting the resultant of vectors 
def resultant2DVector(refreshFrame):
    for widget in refreshFrame.winfo_children():
        widget.destroy()

    ttk.Label(refreshFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(refreshFrame, text="X-Component").grid(column=1, row=2, sticky=(W))
    vector_x_entry = ttk.Entry(refreshFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3, sticky=(W, E))
    
    #Label and input box for y component
    ttk.Label(refreshFrame, text="Y-Component").grid(column=1, row=4, sticky=(W))
    vector_y_entry = ttk.Entry(refreshFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5, sticky=(W, E))

    #Add vector to list of vectors to graph
    ttk.Button(refreshFrame, text="Add Vector").grid(pady=(30,0), column=1, row=8, sticky=(W,E))
   
    #Plots the vectors on a graph.
    ttk.Button(refreshFrame, text="Find Resultant").grid(pady=(30,0), column=1, row=8, sticky=(W,E))

#Refreshes the frame and adds widgets back for plotting the equilibrium vector to the resultant of vectors 




def equilibrium2DVector(refreshFrame):
    for widget in refreshFrame.winfo_children():
        widget.destroy()

    ttk.Label(refreshFrame, text="Enter Multiple Vector Components", font="bold").grid(column=1, row=1, pady=(20,20), sticky=(W))

    ##Label and input box for x component
    ttk.Label(refreshFrame, text="X-Component").grid(column=1, row=2, sticky=(W))
    vector_x_entry = ttk.Entry(refreshFrame, width=20)
    vector_x_entry.grid(pady=(10,10), column=1, row=3, sticky=(W, E))
    
    #Label and input box for y component
    ttk.Label(refreshFrame, text="Y-Component").grid(column=1, row=4, sticky=(W))
    vector_y_entry = ttk.Entry(refreshFrame, width=20)
    vector_y_entry.grid(pady=(10,10), column=1, row=5, sticky=(W, E))
    
    #Add vector to list of vectors to graph
    ttk.Button(refreshFrame, text="Add Vector").grid(pady=(30,0), column=1, row=8, sticky=(W,E))
   
    #Plots the vectors on a graph.
    ttk.Button(refreshFrame, text="Find Equilibrium Vector").grid(pady=(30,0), column=1, row=8, sticky=(W,E))




def showHelp():
    response = '''Hello welcome to vector calc this program aids in the visualization of vectors as well as their calculations.

    Click on the Graph menu item and select an option to begin graphing vectors.

    The Calculations menu item is for performing calculations with vectors like adding or subtracting them.

    - To get started select a menu item and click on an option. You will be presented with input boxes for entering data.

    - Enter the vectors components i.e. their x, y, or z values as a number

    - Click on the button in the menu when finised to perform an action.

    - The program will then preform an action based on what menu option you have selected.
    '''

    #Creates popup to show user how to get started.  takes title and a message as parameters
    messagebox.showinfo("help", response)


####################################################################################################



#Creates main/root window by calling constructor.
root = Tk()

#Sets size and title of window
root.geometry("420x720")
root.title("VectorCalc")

#Creates a frame to put in window. This container is used to when selecting a menu option. When
#the user clicks on an option like "Plot 2D vector" the frame is deleted and a new one is created.
#Wigets are placed in this frame depending on the option selected.
refreshFrame = Frame(root, width=420, height=720)
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








