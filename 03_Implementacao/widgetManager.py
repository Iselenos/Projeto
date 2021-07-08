from ipywidgets.widgets import widget
from lib.widgets.password import Password
from lib.widgets.radioButtons import RadioButtons
from lib.widgets.dropdown import Dropdown
from lib.widgets.valid import Valid
from lib.widgets.checkbox import Checkbox
from lib.widgets.intText import IntText
from lib.widgets.floatText import FloatText
from lib.widgets.intSlider import IntSlider
from lib.widgets.intProgress import IntProgress
from lib.widgets.floatProgress import FloatProgress
from lib.widgets.floatSlider import FloatSlider
from lib.widgets.floatLogSlider import FloatLogSlider
from lib.widgets.button import Button
from lib.widgets.html import HTML
from lib.widgets.textBox import TextBox
from lib.widgets.image import Image
from lib.widgets.markdown import Markdown
from IPython.display import display

class WidgetManager():

    def __init__(self, app):
        self.screens = []
        self.screens.append([[],[],[]])
        self.application = app

    def getWidget(self,widget):
        for x in range(len(self.widgets)):
            if(self.widgets[x] == widget):
                return widget

    def addWidget(self,screen,TypeWidget,ID,y):
        #Verify if its a unique Widget and if it is then add it to widgets array
        if(TypeWidget == 'Button'):
            newWid = Button(self,ID,y)
        elif(TypeWidget =='HTML'):
            newWid = HTML(self,ID,y)
        elif(TypeWidget =='Markdown'):
            newWid = Markdown(self,ID,y)
        elif(TypeWidget =='Text Input'):
            newWid = TextBox(self,ID,y) # (self,attribs)
        elif(TypeWidget =='Image'):
            newWid = Image(self,ID,y)
        elif(TypeWidget == 'IntSlider'):
            newWid = IntSlider(self,ID,y)
        elif(TypeWidget == 'FloatSlider'):
            newWid = FloatSlider(self,ID,y)
        elif(TypeWidget == 'FloatLogSlider'):
            newWid = FloatLogSlider(self,ID,y)
        elif(TypeWidget == 'IntProgress'):
            newWid = IntProgress(self,ID,y)
        elif(TypeWidget == 'FloatProgress'):
            newWid = FloatProgress(self,ID,y)
        elif(TypeWidget == 'IntText'):
            newWid = IntText(self,ID,y)
        elif(TypeWidget == 'FloatText'):
            newWid = FloatText(self,ID,y)
        elif(TypeWidget == 'Checkbox'):
            newWid = Checkbox(self,ID,y)
        elif(TypeWidget == 'Valid'):
            newWid = Valid(self,ID,y)
        elif(TypeWidget == 'Dropdown'):
            newWid = Dropdown(self,ID,y)
        elif(TypeWidget == 'RadioButtons'):
            newWid = RadioButtons(self,ID,y)
        elif(TypeWidget == 'Password'):
            newWid = Password(self,ID,y)
        self.screens[screen][0].append(newWid)
        self.screens[screen][1].append(newWid.represent)
        self.screens[screen][2].append(newWid.widget)

        self.application.redraw()

        return newWid

    def replaceWidget(self, currentScreen,widget):
        for x in range(len(self.screens[currentScreen][0])):
            if(self.screens[currentScreen][0][x] == widget):
                self.screens[currentScreen][2][x] = widget.widget

        self.application.redraw()

    def deleteWidget(self,currentScreen,widget):
        deleteIndex = -1
        for x in range(len(self.screens[currentScreen][0])):
            if(self.screens[currentScreen][0][x] == widget):
                deleteIndex = x
                break

        self.screens[currentScreen][0].pop(deleteIndex)
        self.screens[currentScreen][1].pop(deleteIndex)
        self.screens[currentScreen][2].pop(deleteIndex)

    def selectWidgetM(self,wid):
        self.application.selectWidget(wid)
        self.application.redraw()

    def newScreen(self):
        self.screens.append([[],[],[]])
        self.application.redraw()

    def getWidgetsID(self,screen):
        widgetID = []
        for x in range(len(self.screens[screen][0])):
            widgetID.append(self.screens[screen][0][x].id)

        return widgetID

    def getWidgetByID(self,screen,ID):
        wid = None
        for x in range(len(self.screens[screen][0])):
            if(self.screens[screen][0][x].id == ID):
                wid = self.screens[screen][0][x]
        return wid