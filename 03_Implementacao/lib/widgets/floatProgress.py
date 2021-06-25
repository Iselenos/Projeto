import ipywidgets as widgets
from ..widget import Widget

class FloatProgress(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "FloatProgress"
        self.min = 0
        self.max = 10
        self.value = 7
        self.bar_style = ''
        self.orientation = 'horizontal'
        self.id = ID
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.FloatProgress(description=self.desc,value = self.value, min = self.min, max = self.max, bar_style = self.bar_style,
        orientation= self.orientation)
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "FloatProgress - "+ str(self.id)
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
        attribs.append(widgets.FloatText(description="Default Value: ", value =""+ str(self.value)))
        attribs.append(widgets.FloatText(description="Min Value: ", value =""+ str(self.min)))
        attribs.append(widgets.FloatText(description="Max Value: ", value =""+ str(self.max)))
        attribs.append(widgets.Dropdown(description="Bar Style: ", options=['success', 'info', 'warning', 'danger',''], value =""+ str(self.bar_style)))
        attribs.append(widgets.Dropdown(description="Orientation: ", options=['horizontal', 'vertical'], value =""+ str(self.orientation)))

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
        #VALUE
        value = attribs[5].value
        self.value = value
        #MIN
        min = attribs[6].value
        self.min = min
        #MIN
        max = attribs[7].value
        self.max = max
        #STEP
        style = attribs[8].value
        self.bar_style = style
        #STEP
        orientation = attribs[9].value
        self.orientation = orientation

        self.widget = widgets.FloatProgress(description = description,value = self.value, min = self.min, max = self.max, bar_style = self.bar_style, orientation= self.orientation)
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
        #VALUE
        value = attribs[5].value
        self.value = value
        #MIN
        min = attribs[6].value
        self.min = min
        #MIN
        max = attribs[7].value
        self.max = max
        #BAR_STYLE
        style = attribs[8].value
        self.bar_style = style
        #STEP
        orientation = attribs[9].value
        self.orientation = orientation

        self.widget = widgets.FloatProgress(description = description,value = self.value, min = self.min, max = self.max, bar_style = self.bar_style, orientation= self.orientation)
        self.manager.replaceWidget(currentScreen,self)


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["FloatProgress",self.x,self.y,self.id,"",self.desc,self.value,self.min,self.max,self.bar_style,self.orientation]
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