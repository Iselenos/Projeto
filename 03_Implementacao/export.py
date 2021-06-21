import json
from re import S

class Export():

    def __init__(self,application) -> None:
        self.manager = application.widgetManager
        
    def export(self):
        #1st Create Array of Export
        data = {}
        data['Screens'] = []

        #2nd Go Trought all of Screens
        screens = self.manager.screens

        for x in range(len(screens)):
            screen = []
            for y in range(len(screens[x][0])):
                #3rd One Widget at a time get the info necessary
                print("Saving Screen : " + str(x) + "   Widget : " + str(y))
                screen.append(screens[x][0][y].save())
            data['Screens'].append(screen)

        #4th Dump
        y = json.dumps(data)
        print(y)
