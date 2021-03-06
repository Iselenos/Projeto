import ipywidgets as widgets
from ..widget import Widget
import markdown

class Markdown(Widget):

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        self.desc = "Markdown"
        self.value =''
        self.id = ID
        self.placeholder = ''
        self.x = 0
        self.y = y

    def __initViews__(self):
        #1st Initialize Widget itself
        self.widget = widgets.HTML(
                                        
                                        description=self.desc,
                                        placeholder= self.placeholder,
                                        value=self.value
                                        )
        #2nd Create Represent Button
        self.represent = widgets.Button(
            description= "Markdown - "+ str(self.id),
            disabled=False,
            )
        self.represent.description = "Markdown - "+ str(self.id)
        #3rd Customize On Click Function
        self.represent.on_click(self.on_button_clicked)

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


    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.desc)
        attribs.append(self.value)
        attribs.append(self.placeholder)

        return attribs

    def widgetUpdate(self,attribs):
        #ID
        self.x = attribs[0].value
        self.y = attribs[1].value

        id = attribs[2].value
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Markdown - "+ str(id)

        #VALUE
        value = attribs[4].value
        
        self.value = value

        #DESCRIPTION
        description = attribs[5].value
        self.desc = description

        #PLACEHOLDER
        placeholder = attribs[6].value

        self.placeholder = placeholder

        
        self.widget.description= description
        self.widget.value=markdown.markdown(self.value)
        self.widget.placeholder = self.placeholder


    def widgetLoader(self,attribs):
            #ID
            self.x = attribs[0]
            self.y = attribs[1]

            id = attribs[2]
            if(len(id)>=0):
                self.id = id
                self.represent.description = "Markdown - "+ str(id)

            #VALUE
            value = attribs[4]
            
            self.value = value

            #DESCRIPTION
            description = attribs[5]
            self.desc = description

            #PLACEHOLDER
            placeholder = attribs[6]

            self.placeholder = placeholder

            self.widget.description= description
            self.widget.value=markdown.markdown(self.value)
            self.widget.placeholder = self.placeholder
          

    def save(self):
        #1st -> Nome de Widget
        #5th -> Empty String - Para completar o facto que temos um widget nao representativo
        attribs = ["Markdown",self.x,self.y,self.id,"",self.value,self.desc,self.placeholder]
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

