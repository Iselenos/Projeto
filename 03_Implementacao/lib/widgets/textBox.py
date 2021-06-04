import ipywidgets as widgets
from ..widget import Widget

class TextBox(Widget):

    def __init__(self,description,app,ID):
        self.desc = description
        self.id = ID
        self.placeholder = ''
        self.app = app
        self.x = 2
        self.y = 0
        #1st Initialize Widget itself
        self.widget = widgets.Text(
                                        
                                        description=description,
                                        placeholder= self.placeholder,
                                        disabled=False
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Text - "+ str(self.id),
            disabled=False,
            )
        self.represent.description = "TextBox - "+ str(self.id)
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
        #attribs.append(widgets.Textarea(description="Value: ", value =""+ str(self.value)))
        attribs.append(widgets.Text(description="Description: ", value =""+ str(self.desc)))
        attribs.append(widgets.Text(description="Placeholder: ", value =""+ str(self.placeholder)))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value
        
        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "TextBox - "+ str(id)

        #VALUE
        #value = attribs[1].value
        #self.value = value

        #DESCRIPTION
        description = attribs[3].value
        self.desc = description

        #PLACEHOLDER
        placeholder = attribs[4].value
        self.placeholder = placeholder

        
        self.widget = widgets.Text(
                                        description=description,
                                        placeholder= self.placeholder,
                                        disabled=False
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

