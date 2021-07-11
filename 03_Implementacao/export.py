import json
from re import S
import nbformat as nbf

class Export():

    def __init__(self,application,fileLocation) -> None:
        self.application = application
        self.fileLocation = fileLocation
        
    def saveData(self):
        if(self.fileLocation == ""):
            fileLocation = "config.json"
        else:
            fileLocation = self.fileLocation + ".json"

        #1st Create Array of Export
        self.manager = self.application.widgetManager
        data = {}
        data['Screens'] = []

        #2nd Go Trought all of Screens
        screens = self.manager.screens

        for x in range(len(screens)):
            screen = []
            for y in range(len(screens[x][0])):
                #3rd One Widget at a time get the info necessary
                #print("Saving Screen : " + str(x) + "   Widget : " + str(y))
                screen.append(screens[x][0][y].save())
            data['Screens'].append(screen)

        with open(fileLocation,'w') as f:
            json.dump(data, f)

    def exportNotebook(self):
        nb = nbf.v4.new_notebook()

        code = "from voilapp import VoilApp\n\napp = VoilApp('" + self.fileLocation + "',False)\n\n\ndisplay(app.display())"
        codeCell =  nbf.v4.new_code_cell(code)
        nb['cells'].append(codeCell)    
        fname = 'myApplication.ipynb'

        self.saveData()

        with open(fname, 'w') as _:
            nbf.write(nb, _)