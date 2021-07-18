from lib.widgets.fileUpload import FileUpload
from lib.widgets.colorPicker import ColorPicker
from lib.widgets.datePicker import DatePicker
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
from lib.widgets.label import Label
from IPython.display import display

class WidgetManager():

    def __init__(self, app):
        self.screens = []
        self.screens.append([[],[],[]])
        self.application = app

    #Creates a new widget and places it on the appropriate array according to screen.
    def addWidget(self,screen,TypeWidget,ID,y):
        newWid = None

        if(TypeWidget == 'Button'):
            newWid = Button(self,ID,y)
        elif(TypeWidget =='HTML'):
            newWid = HTML(self,ID,y)
        elif(TypeWidget =='Markdown'):
            newWid = Markdown(self,ID,y)
        elif(TypeWidget =='Text Box'):
            newWid = TextBox(self,ID,y)
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
        elif(TypeWidget == 'Label'):
            newWid = Label(self,ID,y)
        elif(TypeWidget == 'DatePicker'):
            newWid = DatePicker(self,ID,y)
        elif(TypeWidget == 'ColorPicker'):
            newWid = ColorPicker(self,ID,y)
        elif(TypeWidget == 'FileUpload'):
            newWid = FileUpload(self,ID,y)
        
        if(newWid != None):
            self.screens[screen][0].append(newWid)
            self.screens[screen][1].append(newWid.represent)
            self.screens[screen][2].append(newWid.widget)
            self.application.redraw()

        return newWid

    #Deletes a widget
    def deleteWidget(self,currentScreen,widget):
        deleteIndex = -1
        for x in range(len(self.screens[currentScreen][0])):
            if(self.screens[currentScreen][0][x] == widget):
                deleteIndex = x
                break

        self.screens[currentScreen][0].pop(deleteIndex)
        self.screens[currentScreen][1].pop(deleteIndex)
        self.screens[currentScreen][2].pop(deleteIndex)

    #Used as an auxiliary function.
    def selectWidgetM(self,wid):
        self.application.selectWidget(wid)
        self.application.redraw()

    #Creates a new screen and initializes the necessary arrays
    def newScreen(self):
        self.screens.append([[],[],[]])
        self.application.redraw()

    #Returns all the widget Type and IDs of a certain screen
    def getWidgetsID(self,screen):
        widgetID = []
        for x in range(len(self.screens[screen][1])):
            widgetID.append(self.screens[screen][1][x].description)

        return widgetID

    #Returns a widget obtained by its screen and ID
    def getWidgetByID(self,screen,ID):
        wid = None
        for x in range(len(self.screens[screen][0])):
            if(self.screens[screen][0][x].id == ID):
                wid = self.screens[screen][0][x]
        return wid