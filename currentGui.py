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

#This lets us create arrays of 2D vectors 
from VectorList2D import *
######################################################################





class redrawFrameSingle2DVector():

    def __init__(self, refreshFrame):

        #Top Label widget
        self.vectorEntryLabel = ttk.Label(refreshFrame, text="Enter Vector Components", font="bold")
        self.vectorEntryLabel.grid(column=1, row=1, padx=(20,20), pady=(20,20))

        #Label and input box for x component
        self.componentLabelX = ttk.Label(refreshFrame, text="X-Component")
        self.componentLabelX.grid(column=1, row=2)

        #Entry box for the x component
        self.vectorEntryX = ttk.Entry(refreshFrame, width=20)
        self.vectorEntryX.grid(pady=(10,10), column=1, row=3)

        #Label and input box for y component
        self.componentLabelY = ttk.Label(refreshFrame, text="Y-Component")
        self.componentLabelY.grid(column=1, row=4)

        #Entry box for the y component
        self.vectorEntryY = ttk.Entry(refreshFrame, width=20)
        self.vectorEntryY.grid(pady=(10,10), column=1, row=5)

        #Plots the vector on a graph
        self.button1 = ttk.Button(refreshFrame, text="Plot Vector", width = 20, command=lambda: self.plotVector(self.vectorEntryX.get(), self.vectorEntryY.get()))
        self.button1.grid(pady=(30,0), column=1, row=8)

    def plotVector(self, componentX, componentY):

        #convert data from text boxes to float and store
        self.componentX = float(componentX)
        self.componentY = float(componentY)

        #Instantiate a vector with an x and y component from the
        #Vector2D_Components class
        self.vector2D = Vector2D(self.componentX, self.componentY)

        #This creates a graph object and plots a single vector
        self.graph = Vector2D_Graph()
        self.graph.graphSingleVector(self.vector2D)


#Adds widgets back for plotting multiple vectors
class redrawFrameMultiple2DVectors():
    def __init__(self, refreshFrame):
        
        #declares a list of vectors that will be used to pass as arguments to methods
        #TODO create a list class that maybe uses a stack to undo the adding of vectors to the list
        #i.e pop the last vector added to make is so actions can be undone.

        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D() 

        #Positions children widgets to left.
        self.leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
        self.leftFrame.grid(column=0, row=0, sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
        self.rightFrame.grid(column=1, row=0, sticky = "nwes")

        #Top Label widget
        self.vectorEntryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold")
        self.vectorEntryLabel.grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

        #Label and input box for x component
        self.componentLabelX = ttk.Label(self.leftFrame, text="X-Component")
        self.componentLabelX.grid(column=1, row=2)
        
        #Entry box for the x component
        self.vectorEntryX = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryX.grid(pady=(10,10), column=1, row=3)
        
        #Label and input box for y component
        self.componentLabelY = ttk.Label(self.leftFrame, text="Y-Component")
        self.componentLabelY.grid(column=1, row=4)
     
        #Entry box for the y component
        self.vectorEntryY = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryY.grid(pady=(10,10), column=1, row=5)

        #Add vector to list of vectors to graph
        self.addVectorButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addVectorButtonAction(self.vectorEntryX.get(), self.vectorEntryY.get(), self.vectorList, self.rightFrame))
        self.addVectorButton.grid(column=1, row=6)

        #Plots the vectors on a graph.
        self.button3 = ttk.Button(self.leftFrame, text="Plot Vectors", width=20, command=lambda: self.multiGraphButtonAction(self.vectorList))
        self.button3.grid(pady=(30,0), column=1, row=7)
    
        #Label to show the current vectors.
        self.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
        self.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)


    #When the user clicks the "Add Vector" button this method is called.
    #It takes a list and creates a new Vector2D object before adding it to
    #this list. In addition it displays the user entered values to the right
    #to keep track of what they are entering.
    def addVectorButtonAction(self, vectorX, vectorY, vectorList, frameToPrintTo):
        
        vectorList.addVector2D(vectorX, vectorY)
         
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)
 

        
    def multiGraphButtonAction(self, vectorList):
        #Should take a list of vector2D objects and graph them.
        self.graph = Vector2D_Graph()
        self.graph.graphMultipleVectors(vectorList)

####################################################################################################
class redrawFrameResultant2DVectors():
    
    def addVectorButtonAction(self, vectorX, vectorY, vectorList, frameToPrintTo):
        
        vectorList.addVector2D(vectorX, vectorY)
         
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

    def findResultantButtonAction(self, vectorList):
        self.graph = Vector2D_Graph()
        self.graph.graphResultant(vectorList)


    def __init__(self, refreshFrame):
        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D()

        #Positions children widgets to left.
        self.leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
        self.leftFrame.grid(column=0, row=0, sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
        self.rightFrame.grid(column=1, row=0, sticky = "nwes")

        #Top Label widget
        self.vectorEntryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold")
        self.vectorEntryLabel.grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

        #Label and input box for x component
        self.componentLabelX = ttk.Label(self.leftFrame, text="X-Component")
        self.componentLabelX.grid(column=1, row=2)

        #Entry box for the x component
        self.vectorEntryX = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryX.grid(pady=(10,10), column=1, row=3)

        #Label and input box for y component
        self.componentLabelY = ttk.Label(self.leftFrame, text="Y-Component")
        self.componentLabelY.grid(column=1, row=4)

        #Entry box for the y component
        self.vectorEntryY = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryY.grid(pady=(10,10), column=1, row=5)

        #Add vector to list of vectors to graph
        self.addVectorButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addVectorButtonAction(self.vectorEntryX.get(), self.vectorEntryY.get(), self.vectorList, self.rightFrame))
        self.addVectorButton.grid(column=1, row=6)
   
        #Plots the vectors on a graph.
        self.button3 = ttk.Button(self.leftFrame, text="Find Resultant", width=20, command=lambda: self.findResultantButtonAction(self.vectorList))
        self.button3.grid(pady=(30,0), column=1, row=7)

        #Label to show the current vectors.
        self.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
        self.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)

####################################################################################################

class redrawFrameEquilibrium2DVectors():
    
    def addVectorButtonAction(self, vectorX, vectorY, vectorList, frameToPrintTo):
        
        vectorList.addVector2D(vectorX, vectorY)
         
        #Should take the current list of vectors and display it in the right frame.
        self.outputToShowUser = ttk.Label(frameToPrintTo, text=vectorList.toString())
        self.outputToShowUser.grid(padx=(40, 40), column=1, row=2)

    def findResultantButtonAction(self, vectorList):
        self.graph = Vector2D_Graph()
        self.graph.graphResultant(vectorList)


    def __init__(self, refreshFrame):
        #This list belongs to this instance and is reset everytime this window is drawn so it is declared here
        #This list basically holds a list of vector2D objects as well as  providing convient calculation methods
        #on the collection of vectors.
        self.vectorList = VectorList2D()

        #Positions children widgets to left.
        self.leftFrame = Frame(refreshFrame, width=360, height=720, bg = "blue")
        self.leftFrame.grid(column=0, row=0, sticky="nwes")

        #Positions children widgets to right.
        self.rightFrame = Frame(refreshFrame, width=360, height=720, bg = "red")
        self.rightFrame.grid(column=1, row=0, sticky = "nwes")

        #Top Label widget
        self.vectorEntryLabel = ttk.Label(self.leftFrame, text="Enter Multiple Vector Components", font="bold")
        self.vectorEntryLabel.grid(column=1, row=1, padx=(20,20), pady=(20,20), sticky=(W))

        #Label and input box for x component
        self.componentLabelX = ttk.Label(self.leftFrame, text="X-Component")
        self.componentLabelX.grid(column=1, row=2)

        #Entry box for the x component
        self.vectorEntryX = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryX.grid(pady=(10,10), column=1, row=3)

        #Label and input box for y component
        self.componentLabelY = ttk.Label(self.leftFrame, text="Y-Component")
        self.componentLabelY.grid(column=1, row=4)

        #Entry box for the y component
        self.vectorEntryY = ttk.Entry(self.leftFrame, width=20)
        self.vectorEntryY.grid(pady=(10,10), column=1, row=5)

        #Add vector to list of vectors to graph
        self.addVectorButton = ttk.Button(self.leftFrame, text="Add Vector", width=20, command=lambda: self.addVectorButtonAction(self.vectorEntryX.get(), self.vectorEntryY.get(), self.vectorList, self.rightFrame))
        self.addVectorButton.grid(column=1, row=6)
   
        #Plots the vectors on a graph.
        self.button3 = ttk.Button(self.leftFrame, text="Find Equilibrium Vector", width=20, command=lambda: self.findResultantButtonAction(self.vectorList))
        self.button3.grid(pady=(30,0), column=1, row=7)

        #Label to show the current vectors.
        self.currentVectorLabel = ttk.Label(self.rightFrame, text="Current Vectors:")
        self.currentVectorLabel.grid(padx=(100, 100), pady=(20,20), column=1, row=1)











class drawRootWindow():

    def __init__(self):
        #Creates main/root window by calling constructor.
        self.root = Tk()

        #Sets size and title of window
        self.root.geometry("720x720")
        self.root.title("VectorCalc")

        #Creates a frame to put in window. This container is used to when selecting a menu option. When
        #the user clicks on an option like "Plot 2D vector" the frame is deleted and a new one is created.
        #Wigets are placed in this frame depending on the option selected.
        self.refreshFrame = Frame(self.root, width=720, height=720)
        self.refreshFrame.grid(column=0, row=0)


        #Create the menu bar to act as container for menu buttons  
        self.menuBar = Menu(self.root)

        #We have to tell the root window to use menuBar as our menu
        self.root.config(menu=self.menuBar)

        #Instantiating Menu items to act as our buttons in the menu bar
        self.graphButton = Menu(self.menuBar, tearoff = 0)
        self.calcButton = Menu(self.menuBar, tearoff = 0)
        self.helpButton = Menu(self.menuBar, tearoff = 0)

        #Calls the add_cascade method to cause these buttons to show up in the menu.
        #We instantiated them but we need to display them 
        #This is similar to the grid() or pack() methods)
        self.menuBar.add_cascade(label="Graph", menu=self.graphButton)
        self.menuBar.add_cascade(label="Calculations", menu=self.calcButton)
        self.menuBar.add_cascade(label="Help", menu=self.helpButton)

        #Adds commands to the "Graph" menu button

        self.graphButton.add_command(label="Plot single 2D vector", command=lambda: self.redrawFrame(self.refreshFrame, "plotSingle2DVector"))
        self.graphButton.add_command(label="Plot multiple 2D vectors", command=lambda: self.redrawFrame(self.refreshFrame, "plotMultiple2DVectors"))

        #Adds commands to the "Calculations" menu button
        self.calcButton.add_command(label="Resultant 2D vector", command=lambda: self.redrawFrame(self.refreshFrame, "findResultant2DVectors"))
        self.calcButton.add_command(label="Find equlibrium 2D vector", command=lambda: self.redrawFrame(self.refreshFrame, "findEquilibrium2DVectors"))

        #Adds command to the Help menu for getting help
        self.helpButton.add_command(label="Get help", command=self.showHelp)

        #Runs main window in a loop to make the gui interactive. (like moving the mouse and allowing actions to occur)
        self.root.mainloop()

    def showHelp(self):
        
        self.response = '''Hello welcome to vector calc this program aids in the visualization of vectors as well as their calculations.

        Click on the Graph menu item and select an option to begin graphing vectors.

        The Calculations menu item is for performing calculations with vectors like adding or subtracting them.

        - To get started select a menu item and click on an option. You will be presented with input boxes for entering data.

        - Enter the vectors components i.e. their x, y, or z values as a number

        - Click on the button in the menu when finished to perform an action.

        - The program will then preform an action based on what menu option you have selected.
        '''
        #Creates popup to show user how to get started.  takes title and a message as parameters
        messagebox.showinfo("help", self.response)

    #Refreshes the frame and adds widgets back for plotting single vectors
    def redrawFrame(self, refreshFrame, frameToBeDrawn):

        #clears the frame first before we add widgets back when we redraw it.
        for widget in refreshFrame.winfo_children():
            widget.destroy()

        #Defines what frame will be drawn dependent on the menu item selected by the user.
        if(frameToBeDrawn == "plotSingle2DVector"):
            self.window = redrawFrameSingle2DVector(refreshFrame)
        elif(frameToBeDrawn == "plotMultiple2DVectors"):
            self.window = redrawFrameMultiple2DVectors(refreshFrame)
        elif(frameToBeDrawn == "findResultant2DVectors"):
            self.window = redrawFrameResultant2DVectors(refreshFrame)
        elif(frameToBeDrawn == "findEquilibrium2DVectors"):
            self.window = redrawFrameEquilibrium2DVectors(refreshFrame)

window = drawRootWindow()

