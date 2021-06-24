import json

class Loader():

    def __init__(self, application,fileLocation) -> None:
        self.application = application
        self.fileLocation = fileLocation
        self.manager = application.widgetManager

    def load(self):
        #Reference!
        #["Button", 0, 0, "0","","Button", "", ""]
        #Structure -> [WidgetType, Attribs]

        #data = {"Screens": [[["Button", 0, 0, "0","", "Teste", "", ""], ["Button", 0, 1, "1","", "Button", "", ""]], []]}
        data = {"Screens": [[["Button", 0, 0, "0", "", "Teste", "", ""], ["Button", 0, 1, "1", "", "Button", "", ""]], [["Button", 0, 0, "0", "", "Button", "", ""], ["Button", 1, 0, "1", "", "Teste Screen 2", "", ""]], []]}
        
        f = open('data.json',)

        data = json.load(f)

        counter = -1
        for p in data['Screens']:
            counter += 1
            if(counter > 0):
                self.application.newScreen()
            for x in p:
                widget = self.manager.addWidget(counter,x[0],0,0)
                x.pop(0)
                widget.widgetLoader(counter, x)
