import ipywidgets as widgets
from ..widget import Widget

class IntText(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "IntText"
        self.id = ID
        self.value = 7
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.IntText(description=self.desc,disabled=False,value= self.value)
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "IntText - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value = self.id))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
        attribs.append(widgets.Text(description="Description: ", value =""+ str(self.desc)))
        attribs.append(widgets.IntText(description="Value: ", value =""+ str(self.value)))

        return attribs

    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.desc)
        attribs.append(self.value)

        return attribs

    def widgetUpdate(self,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "IntText - "+ str(id)
        #DESCRIPTION
        description = attribs[4].value
        self.desc = description
        #VALUE
        value = attribs[5].value
        self.value = value
        
        self.widget.description = description
        self.widget.value = value

    def widgetLoader(self,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "IntText - "+ str(id)
        #DESCRIPTION
        description = attribs[4]
        self.desc = description
        #VALUE
        value = attribs[5]
        self.value = value
        
        self.widget.description = description
        self.widget.value = value


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["IntText",self.x,self.y,self.id,"",self.desc,self.value]
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