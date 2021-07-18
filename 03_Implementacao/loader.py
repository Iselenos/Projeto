import json
from os import path

class Loader():

    def __init__(self, application,fileLocation) -> None:
        self.application = application
        self.fileLocation = fileLocation + ".json"
        self.manager = application.widgetManager

    #Reads from the JSON file and initializes all the widgets and screens necessary to load the state in the configuration file
    def load(self):
        if(self.fileLocation == ".json"):
            self.fileLocation = "config.json"

        if(path.exists(self.fileLocation) == False):
            return
        f = open(self.fileLocation,)

        data = json.load(f)

        counter = -1
        for p in data['Screens']:
            counter += 1
            if(counter > 0):
                self.application.newScreen()
            for x in p:
                widget = self.manager.addWidget(counter,x[0],0,0)
                x.pop(0)
                widget.widgetLoader(x)
                self.application.graphics.minID += 1
        
        self.application.setCurrentScreen(0)
