import ipywidgets as widgets
from ..widget import Widget

class testWidget(Widget):

    def __init__(self):
        self.testValue = "test"
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

    def widgetUpdate(self):
        pass

    def getWidget(self):
        return self.slider

    def getAttributes(self):
        pass 