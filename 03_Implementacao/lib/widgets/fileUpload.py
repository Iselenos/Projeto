import ipywidgets as widgets
from ..widget import Widget

class FileUpload(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "FileUpload"
        self.id = ID
        self.accept = '.pdf'
        self.multiple = False
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.FileUpload(accept=self.accept,multiple = self.multiple)
        #2nd Create Represent Button
        self.represent = widgets.Button(description= "Button - "+ str(self.id),disabled=False,button_style='')
        self.represent.description = "FileUpload - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value = self.id))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
        attribs.append(widgets.Text(description="Accepted File Extension: ", value =""+ str(self.accept)))
        attribs.append(widgets.Dropdown(description="Multiple Files: ", options= [False,True],value = self.multiple))

        return attribs

    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.desc)
        attribs.append(self.value)

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "FileUpload - "+ str(id)
        #ACCEPT
        accept = attribs[4].value
        self.accept = accept
        #MULTIPLE
        multiple = attribs[5].value
        self.multiple = multiple
        
        try:
            self.widget = widgets.FileUpload(accept=self.accept,multiple = self.multiple)
            self.manager.replaceWidget(currentScreen,self)
        except:
            print("exception")

    def widgetLoader(self, currentScreen,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "FileUpload - "+ str(id)
        #ACCEPT
        accept = attribs[4]
        self.accept = accept
        #MULTIPLE
        multiple = attribs[5]
        self.multiple = multiple
        
        try:
            self.widget = widgets.FileUpload(accept=self.accept,multiple = self.multiple)
            self.manager.replaceWidget(currentScreen,self)
        except:
            pass


    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["FileUpload",self.x,self.y,self.id,"",self.accept,self.multiple]
        return attribs

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def on_button_clicked(self,b):
        self.manager.selectWidgetM(self)

    def createButton(self,desc):
        out = widgets.Button(description= desc,disabled=False,button_style='', tooltip='Click me')
        return out