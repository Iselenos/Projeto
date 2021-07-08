import ipywidgets as widgets
from ..widget import Widget

class TextBox(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "Text Box"
        self.id = ID
        self.placeholder = ''
        self.x = 0
        self.y = y


    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.Text(     description=self.desc,
                                        placeholder= self.placeholder,
                                        disabled=False,
                                        layout = widgets.Layout(width='100%'),
                                        style= {'description_width' : 'auto'}
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Text - "+ str(self.id),
            disabled=False,
            )
        self.represent.description = "TextBox - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value =""+ str(self.id)))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
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


        #DESCRIPTION
        description = attribs[4].value
        self.desc = description

        #PLACEHOLDER
        placeholder = attribs[5].value
        self.placeholder = placeholder

        
        self.widget = widgets.Text(
                                        description=description,
                                        placeholder= self.placeholder,
                                        disabled=False,
                                        layout = widgets.Layout(width='100%'),
                                        style= {'description_width' : 'auto'}
                                        )
        self.manager.replaceWidget(currentScreen,self)

    def widgetLoader(self, currentScreen,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "TextBox - "+ str(id)


        #DESCRIPTION
        description = attribs[4]
        self.desc = description

        #PLACEHOLDER
        placeholder = attribs[5]
        self.placeholder = placeholder

        
        self.widget = widgets.Text(
                                        description=description,
                                        placeholder= self.placeholder,
                                        disabled=False,
                                        layout = widgets.Layout(width='100%'),
                                        style= {'description_width' : 'auto'}
                                        )
        self.manager.replaceWidget(currentScreen,self)

    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["Text Box",self.x,self.y,self.id,"",self.desc,self.placeholder]
        return attribs

    def getReferenceButton(self):
        return self.represent

    def getWidget(self):
        return self.widget

    def on_button_clicked(self,b):
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

