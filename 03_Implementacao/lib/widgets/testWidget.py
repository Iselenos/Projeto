import ipywidgets
from ..widget import Widget

class testWidget(Widget):

    def __init__(self):
        self.testValue = "test"

    def test(self):
        print(self.testValue)