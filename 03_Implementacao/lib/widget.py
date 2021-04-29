import ipywidgets

class Widget:

    def widgetUpdate(self):
        raise NotImplementedError

    def getWidget(self):
        raise NotImplementedError

    def getAttributes(self):
        raise NotImplementedError 

    def getAttributesView(self):
        raise NotImplementedError

    def getReferenceButton(self):
        raise NotImplementedError