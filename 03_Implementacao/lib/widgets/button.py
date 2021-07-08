import ipywidgets as widgets
from ..widget import Widget

class Button(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "Button"
        self.id = ID
        self.tooltip =''
        self.style = ''
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.Button(description=self.desc,disabled=False,button_style='')
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "Button - "+ str(self.id)
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
        attribs.append(widgets.Text(description="Tooltip: ", value =""+ str(self.tooltip)))
        attribs.append(widgets.Dropdown(description="Style: ", options=['success', 'info', 'warning', 'danger',''], value =""+ str(self.style)))

        return attribs

    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.desc)
        attribs.append(self.tooltip)
        attribs.append(self.style)

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
        #TOOLTIP
        tooltip = attribs[5].value
        self.tooltip = tooltip
        #STYLE
        style = attribs[6].value
        self.style = style
        self.widget = widgets.Button(description = description,button_style = style,tooltip = tooltip,disabled=False)
        self.manager.replaceWidget(currentScreen,self)

    def widgetLoader(self, currentScreen,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Button - "+ str(id)
        #DESCRIPTION
        description = attribs[4]
        self.desc = description
        #TOOLTIP
        tooltip = attribs[5]
        self.tooltip = tooltip
        #STYLE
        style = attribs[6]
        self.style = style
        self.widget = widgets.Button(description = description, button_style = style,tooltip = tooltip,disabled=False)
        self.manager.replaceWidget(currentScreen,self)


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["Button",self.x,self.y,self.id,"",self.desc,self.tooltip,self.style]
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