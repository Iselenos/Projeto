import ipywidgets as widgets
from ..widget import Widget

class FloatSlider(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "FloatSlider"
        self.min = 0
        self.max = 10
        self.value = 5
        self.step = 1
        self.orientation = 'horizontal'
        self.id = ID
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.FloatSlider(description=self.desc,value = self.value, min = self.min, max = self.max, step = self.step,disabled=False,continuous_update=False,
        orientation= self.orientation,readout=True,readout_format='d')
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "FloatSlider - "+ str(self.id)
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
        attribs.append(widgets.FloatText(description="Step Value: ", value =""+ str(self.step)))
        attribs.append(widgets.Dropdown(description="Orientation: ", options=['horizontal', 'vertical'], value =""+ str(self.orientation)))

        return attribs

    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.desc)
        attribs.append(self.value)
        attribs.append(self.min)
        attribs.append(self.max)
        attribs.append(self.step)
        attribs.append(self.orientation)

        return attribs


    def widgetUpdate(self,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "FloatSlider - "+ str(id)
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
        step = attribs[8].value
        self.step = step
        #STEP
        orientation = attribs[9].value
        self.orientation = orientation

        self.widget.value = self.value
        self.widget.description = self.desc
        self.widget.max = self.max
        self.widget.min = self.min
        self.widget.step = self.step
        self.widget.orientation = self.orientation

    def widgetLoader(self,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "FloatSlider - "+ str(id)
        #DESCRIPTION
        description = attribs[4]
        self.desc = description
        #VALUE
        value = attribs[5]
        self.value = value
        #MIN
        min = attribs[6]
        self.min = min
        #MAX
        max = attribs[7]
        self.max = max
        #STEP
        step = attribs[8]
        self.step = step
        #STEP
        orientation = attribs[9]
        self.orientation = orientation

        self.widget.value = self.value
        self.widget.description = self.desc
        self.widget.max = self.max
        self.widget.min = self.min
        self.widget.step = self.step
        self.widget.orientation = self.orientation


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["FloatSlider",self.x,self.y,self.id,"",self.desc,self.value,self.min,self.max,self.step,self.orientation]
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