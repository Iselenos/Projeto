import ipywidgets as widgets
from ..widget import Widget

class testWidget(Widget):

    def __init__(self,description,app,ID):
        self.desc = description
        self.app = app
        self.id = ID
        self.x = 0
        self.y = 0
        #1st Initialize Widget itself
        self.widget = widgets.IntSlider(
                                        value=7,
                                        min=0,
                                        max=10,
                                        step=1,
                                        description=description,
                                        disabled=False,
                                        continuous_update=False,
                                        orientation='horizontal',
                                        readout=True,
                                        readout_format='d'
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= description,
            disabled=False,
            button_style='', 
            tooltip='Click me'
            )
        self.represent.description = "TextWidget - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Col: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.IntText(description="Min Value: "))
        attribs.append(widgets.IntText(description="Max Value: "))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value

        min = attribs[2].value
        max = attribs[3].value
        self.widget = widgets.IntSlider(
                                        value=(max +min) /2,
                                        min=min,
                                        max=max,
                                        step=1,
                                        description=self.desc,
                                        disabled=False,
                                        continuous_update=False,
                                        orientation='horizontal',
                                        readout=True,
                                        readout_format='d'
                                        )
        self.app.refreshWidget(currentScreen,self)
        self.app.redraw()

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def getAttributes(self):
        pass 

    def on_button_clicked(self,b):
        self.app.selectWidget(self)
        self.app.redraw()

    def createButton(self,desc):
        out = widgets.Button(
                description= desc,
                disabled=False,
                button_style='', 
                tooltip='Click me'#,
                #icon='check'
                )
        return out

