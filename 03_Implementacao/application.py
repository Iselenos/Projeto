from ipywidgets import AppLayout, Button, Layout, Tab, Text, VBox, GridBox, Label, Layout, Box
import ipyvuetify as v
from IPython.display import clear_output, display
from widgetManager import WidgetManager
from loader import Loader
from graphics import Graphics

class Application():

    #Nota : Para limpar o ecra e dar redraw podemos usar clear_output()

    def __init__(self, out,fileLocation = None) -> None:
        ##### If in Dev Mode #####
        #1st Step -> Loading (If needed)
        self.fileLocation = fileLocation
        self.loadModule = Loader(self.fileLocation)
        self.output = out
        #2nd Step
        self.loader()
        #3rd Step -> Initialize Viewing
        self.graphics = Graphics(self.widgetManager)

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

    def refreshWidget(self,wid):
        self.widgetManager.replaceWidget(wid)

    def redraw(self):
        self.output.clear_output()
        self.graphics.graphics = self.graphics.initApp()
        with self.output :
            display(self.graphics.graphics)