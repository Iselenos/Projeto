import ipywidgets as widgets
from ..widget import Widget

class Image(Widget):

    def __init__(self,description,app):
        
        file = open("img.png", "rb")
        image = file.read()
        self.value = image
        self.app = app
        #1st Initialize Widget itself
        self.widget = widgets.Image(
                                        value=self.value
                                        )
        #2nd Create Represent Button
        self.id = ''
        self.represent = widgets.Button(
            description= "Image - "+ str(self.id),
            disabled=False,
            )
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.Text(description="id: ", value =""+ str(self.id)))
        attribs.append(widgets.FileUpload())

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        #ID
        id = attribs[0].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Image - "+ str(id)

        #VALUE
        valueTemp = attribs[1].value
        
        value= list(valueTemp)[0]
        self.value=valueTemp[value].get('content')
        
        self.widget = widgets.Image(
                                        value=self.value
                                        )
        self.app.refreshWidget(currentScreen,self)
        self.app.redraw()

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def getAttributes(self):
        pass 

    def on_button_clicked(self,b):
        self.app.selectWidget(self)
        self.app.redraw()

    def createButton(self,desc):
        out = widgets.Button(
                description= desc,
                disabled=False,
                button_style='', 
                tooltip='Click me'#,
                #icon='check'
                )
        return out

