import ipywidgets as widgets
from ..widget import Widget

class Image(Widget):
    #Image height is ignored as in CSS from jupyter it is set as auto only the width matters.
    #https://github.com/jupyter-widgets/ipywidgets/issues/1689 <- Reference

    def __init__(self,description,app,ID,y):
        
        file = open("img.png", "rb")
        self.id = ID
        image = file.read()
        self.value = image
        self.app = app
        self.x = 0
        self.y = y
        #1st Initialize Widget itself
        self.widget = widgets.Image(
                                        value=self.value,
                                        width = 200,
                                        height = 100
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Image - "+ str(self.id),
            disabled=False,
            )
        self.represent.description = "Image - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Col: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="id: ", value =""+ str(self.id)))
        attribs.append(widgets.IntText(description="Width: ", value = int(self.widget.width)))
        attribs.append(widgets.IntText(description="Height: ", value = int(self.widget.height)))
        attribs.append(widgets.FileUpload())

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Image - "+ str(id)

        #Size
        self.width = attribs[3].value
        self.height = attribs[4].value

        #VALUE
        valueTemp = attribs[5].value
        if(len(valueTemp) > 0):
            value= list(valueTemp)[0]
            self.value=valueTemp[value].get('content')
        
        print(self.width)
        print(self.height)

        self.widget = widgets.Image(
                                        value=self.value,
                                        width=self.width,
                                        height=self.height
                                        )

        print(self.widget.width)
        print(self.widget.height)
        print("Here")                              
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

