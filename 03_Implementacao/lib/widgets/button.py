import ipywidgets as widgets
from ..widget import Widget

class Button(Widget):

    def __init__(self,description,app,ID):
        self.desc = description
        self.id = ID
        self.tooltip =''
        self.style = ''
        self.app = app
        self.x = 0
        self.y = 0
        #1st Initialize Widget itself
        self.widget = widgets.Button(                                     
                                        description=description,
                                        disabled=False,
                                        button_style='',
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Button - "+ str(self.id),
            disabled=False,
            button_style=''
            #style =  {'button_color' : '#484848', 'color' : '#FFFFFF'}
        )

        self.represent.description = "Button - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def initializeWidget(self,parametros):
        pass

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Col: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="id: ", value = self.id))
        attribs.append(widgets.Text(description="Button Text: ", value =""+ str(self.desc)))
        attribs.append(widgets.Text(description="Tooltip: ", value =""+ str(self.tooltip)))
        attribs.append(widgets.Dropdown(description="Style: ", options=['success', 'info', 'warning', 'danger',''], value =""+ str(self.style)))

        return attribs

    def widgetUpdate(self, currentScreen,attribs):
        self.x = attribs[0].value
        self.y = attribs[1].value

        #ID
        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Button - "+ str(id)
        
        #DESCRIPTION
        description = attribs[3].value
        self.desc = description

        #TOOLTIP
        tooltip = attribs[4].value
        self.tooltip = tooltip

        #STYLE
        style = attribs[5].value
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