import ipywidgets as widgets
from ..widget import Widget

class Dropdown(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "Dropdown"
        self.id = ID
        self.options = 'Insert options'
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.Dropdown(description=self.desc,disabled=False, options = [self.options])
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "Dropdown - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value = self.id))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
        attribs.append(widgets.Text(description="Button Text: ", value =""+ str(self.desc)))
        attribs.append(widgets.Text(description="Options: ", value =""+ str(self.options)))
        #attribs.append(widgets.Text(description="Selected Value: ", value =""+ str(self.value)))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Button - "+ str(id)
        #DESCRIPTION
        description = attribs[4].value
        self.desc = description
        #OPTIONS
        options = attribs[5].value
        print(options)
        self.options = str(options)
        #VALUE
       # value = attribs[6]
       # self.style = value
        self.widget = widgets.Dropdown(description=self.desc,disabled=False, options = self.options.split(","))
        print(options)
        self.manager.replaceWidget(currentScreen,self)

    def widgetLoader(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Button - "+ str(id)
        #DESCRIPTION
        description = attribs[4].value
        self.desc = description
        #OPTIONS
        options = attribs[5].value
        print(options)
        self.options = str(options)
        #VALUE
       # value = attribs[6]
       # self.style = value
        self.widget = widgets.Dropdown(description=self.desc,disabled=False, options = self.options.split(","))
        print(options)
        self.manager.replaceWidget(currentScreen,self)


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["Dropdown",self.x,self.y,self.id,"",self.desc,self.options]
        return attribs

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def on_button_clicked(self,b):
        self.manager.selectWidgetM(self)

    def createButton(self,desc):
        out = widgets.Button(description= desc,disabled=False,button_style='', tooltip='Click me')
        return out