from ipywidgets import AppLayout, Button, Layout, Tab, Text, VBox, GridBox, Label, Layout, Box
import ipyvuetify as v
from IPython.display import clear_output, display
from IPython.core.display import display, HTML
from widgetManager import WidgetManager
from loader import Loader
from graphics import Graphics
from export import Export

class Application():

    def __init__(self,fileLocation = None, editmode = True) -> None:
        ##### If in Dev Mode #####
        #1st Step -> Loading (If needed)
        self.fileLocation = fileLocation
        self.widgetManager = WidgetManager(self)
        self.loadModule = Loader(self,self.fileLocation)
        #2nd Step
        #3rd Step -> Initialize Viewing
        self.graphics = Graphics(self,editmode)
        #self.loader()
        self.loadStyles()
        self.export = Export(self)

    def display(self):
        return self.graphics.graphics

    def addWidget(self,widget):
        self.widgetManager.addWidget(widget)
    
    def getWidget(self, reference):
        return self.widgetManager.getWidget(reference)

    def loader(self, fileLocation = None):
            self.loadModule.load()

    def selectWidget(self,wid):
        self.graphics.setSelectedWidget(wid)

    def refreshWidget(self,currentScreen,wid):
        self.widgetManager.replaceWidget(currentScreen,wid)

    def redraw(self):
        self.graphics.updateGraphics()

    def loadStyles(self):
        display(HTML('<style>.jp-Notebook{margin:0 10% 0 10%}.jp-Notebook, .vuetify-styles div.v-application--wrap {background-color:slategray;}.inspector{background-color:white;}</style>'))

    def newScreen(self):
        self.graphics.newScreen("Holder")

    def exportData(self,widget, event, data):
        self.export.exportData()

    def newApp(self,widget, event, data):
        self.widgetManager = WidgetManager(self)
        self.graphics.resetGraphics()
        