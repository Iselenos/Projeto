from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


class testWidget:
    def __init__(self,a):
        self.x = a
        self.widget = widgets.IntSlider(value=a,min=0,max=11,step=1,description='Test:',disabled=False,continuous_update=False,orientation='horizontal',readout=True,readout_format='d')


    def getWid(self):
        return self.widget
