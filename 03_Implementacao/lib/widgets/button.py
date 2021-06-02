import ipywidgets as widgets
from ..widget import Widget

class Button(Widget):

    def __init__(self,description,app):
        self.desc = description
        self.tooltip =''
        self.style = ''
        self.app = app
        #1st Initialize Widget itself
        self.widget = widgets.Button(
                                        
                                        description=description,
                                        disabled=False,
                                        button_style=''
                                        )
        #2nd Create Represent Button
        self.id = ''
        self.represent = widgets.Button(
            description= "Button - "+ str(self.id),
            disabled=False,
            button_style='', 
            )
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.Text(description="id: ", value =""+ str(self.id)))
        attribs.append(widgets.Text(description="Button Text: ", value =""+ str(self.desc)))
        attribs.append(widgets.Text(description="Tooltip: ", value =""+ str(self.tooltip)))
        attribs.append(widgets.Dropdown(description="Style: ", options=['success', 'info', 'warning', 'danger',''], value =""+ str(self.style)))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        #ID
        id = attribs[0].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Button - "+ str(id)
        
        #DESCRIPTION
        description = attribs[1].value
        self.desc = description

        #TOOLTIP
        tooltip = attribs[2].value
        self.tooltip = tooltip

        #STYLE
        style = attribs[3].value
        self.style = style

        
        self.widget = widgets.Button(
                                        description = description,
                                        button_style = style,
                                        tooltip = tooltip,
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

