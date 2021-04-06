from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


class testWidget:
    def __init__(self,a):
        self.x = a
        tempwidget = widgets.IntSlider(value=a,min=0,max=11,step=1,description='Test:',disabled=False,continuous_update=False,orientation='horizontal',readout=True,readout_format='d')
        self.widget = interact(self.select, x=tempwidget)
        self.newWida = ""
        
        
    def getWid(self):
        return self.widget

    def select(self, x):
        if x != self.x:
            print("num")
            display(self.newWid())
            

    def newWid(self):
        return widgets.IntSlider(value=5,min=0,max=11,step=1,description='Test:',disabled=False,continuous_update=False,orientation='horizontal',readout=True,readout_format='d')
