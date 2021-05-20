from IPython.core.display import display
import ipywidgets
from traitlets.config import application
from lib.widgets.testWidget import testWidget
from IPython.display import display

class WidgetManager():

    def __init__(self, app):
        self.widgets = []
        self.widgetsInspector = []
        self.widgetsPreview = []
        self.application = app


    def getWidget(self):
        #Use reference to get a Widget from self.widgets
        pass

    def addWidget(self,widget):
        #Verify if its a unique Widget and if it is then add it to widgets array
        print(widget)
        newWid = testWidget(widget)
        self.widgets.append(newWid)
        self.widgetsInspector.append(newWid.represent) 
        self.widgetsPreview.append(newWid.widget)
        self.application.redraw()
        print("success")

    def widgetInitialization(self, widgetType):
        ## Implement a type of switch to initialize a certain Widget
        pass

    def loader(self, widgets):
        self.widgets = widgets
