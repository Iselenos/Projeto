from ipywidgets import AppLayout, Button, Layout, Tab, Text, VBox, GridBox, Label, Layout, Box
import ipyvuetify as v
from .widgetManager import WidgetManager

class Graphics():

    def __init__(self,widgetManager) -> None:
        self.widgetManager = widgetManager
        self.__initHeader__()
        self.__initPreview__()
        self.__initInspector__()
        self.graphics = self.__initApp__()
        

    def __initHeader__(self):
        #Initalize all header related features
        pass


    def __initPreview__(self):
        #Initialize all preview related features
        pass


    def __initInspector__(self):
        pass


    def __initFooter__(self):
        pass


    def __initApp__(self):
        #Combine all previous information into one place (Can be used to ReDraw as well!)
        pass