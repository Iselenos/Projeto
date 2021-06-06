from ipywidgets import AppLayout, Button, Layout, Tab, Text, VBox, GridBox, Label, Layout, Box
import ipyvuetify as v
from IPython.display import clear_output, display
from IPython.core.display import display, HTML
from widgetManager import WidgetManager
from loader import Loader
from graphics import Graphics

class Application():

    def __init__(self,fileLocation = None) -> None:
        ##### If in Dev Mode #####
        #1st Step -> Loading (If needed)
        self.fileLocation = fileLocation
        self.loadModule = Loader(self.fileLocation)
        #2nd Step
        self.loader()
        #self.loadStyles()
        #3rd Step -> Initialize Viewing
        self.graphics = Graphics(self.widgetManager,self)

    def display(self):
        return self.graphics.graphics

    def addWidget(self,widget):
        self.widgetManager.addWidget(widget)
    
    def getWidget(self, reference):
        return self.widgetManager.getWidget(reference)

    def loader(self, fileLocation = None):
        #2nd Step -> Initialize widgetManager
        self.widgetManager = WidgetManager(self)

        if(fileLocation != None):
            widgetsLoaded = self.loadModule.load()
            self.widgetManager.loader(widgetsLoaded)
        else:
            pass

    def selectWidget(self,wid):
        self.graphics.setSelectedWidget(wid)

    def refreshWidget(self,currentScreen,wid):
        self.widgetManager.replaceWidget(currentScreen,wid)

    def redraw(self):
        self.graphics.updateGraphics()

    def loadStyles(self):
        display(HTML('<style>.jp-Notebook{background-color:black;}</style>'))