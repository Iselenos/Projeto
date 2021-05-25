import ipywidgets as widgets
from ..widget import Widget

class testWidget(Widget):

    def __init__(self,description,app):
        self.desc = description
        self.app = app
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
            tooltip='Click me',
            icon='check'
            )
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Min Value: "))
        attribs.append(widgets.IntText(description="Max Value: "))

        return attribs

    def widgetUpdate(self, attribs):
        min = attribs[0].value
        max = attribs[1].value
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
        self.app.refreshWidget(self)
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

