import ipywidgets as widgets
from ..widget import Widget

class HTML(Widget):

    def __init__(self,description,widgetManager,ID,y):
        self.desc = description
        self.value =''
        self.id = ID
        self.placeholder = ''
        self.manager = widgetManager
        self.x = 0
        self.y = y
        #1st Initialize Widget itself
        self.widget = widgets.HTML(
                                        
                                        description=description,
                                        placeholder= self.placeholder,
                                        value=self.value
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Text (HTML) - "+ str(self.id),
            disabled=False,
            )
        self.represent.description = "HTML - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value =""+ str(self.id)))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
        attribs.append(widgets.Textarea(description="Value: ", value =""+ str(self.value)))
        attribs.append(widgets.Text(description="Description: ", value =""+ str(self.desc)))
        attribs.append(widgets.Text(description="Placeholder: ", value =""+ str(self.placeholder)))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        #ID
        self.x = attribs[0].value
        self.y = attribs[1].value

        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "HTML - "+ str(id)

        #VALUE
        value = attribs[4].value
        
        self.value = value

        #DESCRIPTION
        description = attribs[5].value
        self.desc = description

        #PLACEHOLDER
        placeholder = attribs[6].value

        self.placeholder = placeholder

        
        self.widget = widgets.HTML(
                                        description=description,
                                        placeholder= self.placeholder,
                                        value=self.value
                                        )
        self.manager.replaceWidget(currentScreen,self)

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def getAttributes(self):
        pass 

    def on_button_clicked(self,b):
        print(self.manager)
        self.manager.selectWidgetM(self)

    def createButton(self,desc):
        out = widgets.Button(
                description= desc,
                disabled=False,
                button_style='', 
                tooltip='Click me'#,
                #icon='check'
                )
        return out

