import ipywidgets

class Widget:

    #Initialize all the necessary variables
    def __initVariables__(self):
        raise NotImplementedError

    #Initialize the iPyWidget widget, and an inspector representation button
    def __initViews__(self):
        raise NotImplementedError

    #update widget attributes and reinitialize the widget
    def widgetUpdate(self,attribs):
        raise NotImplementedError 

    #return the attribute view listing
    def getAttribsView(self):
        raise NotImplementedError

    #update widget attributes and reinitialize the widget -> Version used for the loader as the array received does not contain .value
    def widgetLoader(self,attribs):
        raise NotImplementedError

    #returns an array that will be serialized into a JSON file
    def save(self):
        raise NotImplementedError
    
    #returns the reference button for the inspector
    def getReferenceButton(self):
        raise NotImplementedError

    #returns the ipywidget widget
    def getWidget(self):
        raise NotImplementedError

    #function used in the reference button
    def on_button_clicked(self,b):
        raise NotImplementedError
