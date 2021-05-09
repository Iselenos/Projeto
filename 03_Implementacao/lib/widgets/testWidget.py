import ipywidgets as widgets
from ..widget import Widget

class testWidget(Widget):

    def __init__(self):
        #1st Initialize Widget itself
        self.slider = widgets.IntSlider(
                                        value=7,
                                        min=0,
                                        max=10,
                                        step=1,
                                        description='Test:',
                                        disabled=False,
                                        continuous_update=False,
                                        orientation='horizontal',
                                        readout=True,
                                        readout_format='d'
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Im a Int Slider",
            disabled=False,
            button_style='', 
            tooltip='Click me',
            icon='check'
            )
        #3rd Customize On Click Function
        self.represent.on_click(on_button_clicked)

    def widgetUpdate(self):
        pass

    def getReferenceButton(self):
        return self.represent


    def getWidget(self):
        return self.slider

    def getAttributes(self):
        pass 

def on_button_clicked(b):
    b.description = "Test"