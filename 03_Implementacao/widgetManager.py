from IPython.core.display import display
import ipywidgets
from traitlets.config import application
from lib.widgets.testWidget import testWidget
from lib.widgets.button import Button
from lib.widgets.html import HTML
from lib.widgets.textBox import TextBox
from lib.widgets.image import Image
from IPython.display import display

class WidgetManager():

    def __init__(self, app):
        #Implements multiple screens
        self.screens = []
        self.screens.append([[],[],[]])
        #self.widgets = []
        #self.widgetsInspector = []
        #self.widgetsPreview = []
        self.application = app

    def getWidget(self,widget):
        for x in range(len(self.widgets)):
            if(self.widgets[x] == widget):
                return widget

    def addWidget(self,screen,widget,ID,y):
        #Verify if its a unique Widget and if it is then add it to widgets array
        if(widget == 'Button'):
            newWid = Button(widget,self.application,ID,y)
        elif(widget =='HTML'):
            newWid = HTML(widget,self.application,ID,y)
        elif(widget =='Text'):
            newWid = TextBox(widget,self.application,ID,y)
        elif(widget =='Image'):
            newWid = Image(widget,self.application,ID,y)
        else:
            newWid = testWidget(widget,self.application,ID,y)

        self.screens[screen][0].append(newWid)
        self.screens[screen][1].append(newWid.represent)
        self.screens[screen][2].append(newWid.widget)
        #print(widget)
        
        #self.widgets.append(newWid)
        #self.widgetsInspector.append(newWid.represent) 
        #self.widgetsPreview.append(newWid.widget)
        self.application.redraw()

    def widgetInitialization(self, widgetType):
        ## Implement a type of switch to initialize a certain Widget
        pass

    def loader(self, widgets):
        self.widgets = widgets

    def replaceWidget(self, currentScreen,widget):
        for x in range(len(self.screens[currentScreen][0])):
            if(self.screens[currentScreen][0][x] == widget):
                self.screens[currentScreen][2][x] = widget.widget

    def deleteWidget(self,currentScreen,widget):
        deleteIndex = -1
        for x in range(len(self.screens[currentScreen][0])):
            if(self.screens[currentScreen][0][x] == widget):
                deleteIndex = x
                break

        self.screens[currentScreen][0].pop(deleteIndex)
        self.screens[currentScreen][1].pop(deleteIndex)
        self.screens[currentScreen][2].pop(deleteIndex)
        self.application.redraw()


    def newScreen(self):
        self.screens.append([[],[],[]])
        self.application.redraw()