from ipywidgets import AppLayout, Button, Layout, Tab, Text, VBox, GridBox, Label, Layout, Box
import ipyvuetify as v
from IPython.display import clear_output, display
from IPython.core.display import display, HTML
from widgetManager import WidgetManager
from loader import Loader
from graphics import Graphics
from export import Export

class VoilApp():

    #####
    # init
    #
    # Params ->
    # fileLocation - File path refering to configuration file
    # editmode - boolean regarding the presentation of application
    ####
    def __init__(self,fileLocation = None, editmode = True) -> None:
        self.fileLocation = fileLocation
        self.widgetManager = WidgetManager(self)
        self.loadModule = Loader(self,self.fileLocation)
        self.graphics = Graphics(self,editmode)
        self.loader()

        if(editmode):
            self.loadStyles()
        self.export = Export(self,self.fileLocation)

    #Returns the Object to wich display the application
    def display(self):
        return self.graphics.graphics
    
    #Returns a widget with the object reference - Param -> reference - Widget Object
    def getWidget(self, reference):
        return self.widgetManager.getWidget(reference)

    #Loads the current configuration file
    def loader(self):
            self.loadModule.load()

    #Sets widget that is currently being edited - Param -> wid - Widget Object
    def selectWidget(self,wid):
        self.graphics.setSelectedWidget(wid)

    #Runs a widgetManager function with updates the current displayed widget - Params -> currentScren - int referencing the screen, wid - widget Object
    def refreshWidget(self,currentScreen,wid):
        self.widgetManager.replaceWidget(currentScreen,wid)

    #Runs a graphics update
    def redraw(self):
        self.graphics.updateGraphics()

    #Used to load CSS look when in non edit mode
    def loadStyles(self):
        display(HTML('<style>.jp-Notebook{margin:0 10% 0 10%}.jp-Notebook, .vuetify-styles div.v-application--wrap {background-color:slategray;}.inspector{background-color:white;}</style>'))

    #Creates a new screen within graphics
    def newScreen(self):
        self.graphics.newScreen("Holder")

    #Function to be used in iPyVuetify Menu
    def saveDataMenu(self,widget, event, data):
        self.export.saveData()

    #Function to save configuration file to be used by the Developer
    def saveData(self):
        self.export.saveData()

    #Export jupyter notebook trought the ipyvuetify menu
    def exportNotebook(self,widget, event, data):
        self.export.exportNotebook()

    #Start an application from scratch trough the menu
    def newApp(self,widget, event, data):
        self.widgetManager = WidgetManager(self)
        self.graphics.resetGraphics()
        
    #Defines what is the current screen being rendered - Param -> number - int referencing the screen
    def setCurrentScreen(self, number):
        self.graphics.setSelectedScreen(number)

    #Returns the number of screens available on the exported application
    def getScreenNumber(self):
        return len(self.graphics.screens)

    #Returns widget IDs and their type from a certain screen - Param -> screen, int referencing the screen
    def getWidgetIDs(self, screen):
        return self.widgetManager.getWidgetsID(screen)

    #Returns a widget from a x screen with an y ID - Params -> screen, int referencing the screen. ID, string referencing the ID of the widget
    def getWidget(self,screen,ID):
        return self.widgetManager.getWidgetByID(screen,ID)

    #Adds a widget from x type to y screen - Params -> screen, int referencing the screen. type, string referencing the type of Widget
    def addWidget(self,screen,type):
        widget = self.widgetManager.addWidget(screen,type,str(self.graphics.minID),self.graphics.y)
        if(self.graphics.y < 20):
            self.graphics.y += 1
        self.graphics.minID += 1
        return widget



    