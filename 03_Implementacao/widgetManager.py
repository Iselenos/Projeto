import ipywidgets

class WidgetManager():

    def __init__(self, app):
        self.widgets = []
        self.application = app


    def getWidget(self):
        #Use reference to get a Widget from self.widgets
        pass

    def addWidget(self,widget):
        #Verify if its a unique Widget and if it is then add it to widgets array
        pass

    def widgetInitialization(self, widgetType):
        ## Implement a type of switch to initialize a certain Widget
        pass

    def loader(self, widgets):
        self.widgets = widgets
