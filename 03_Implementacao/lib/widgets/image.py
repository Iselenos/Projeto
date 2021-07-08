import ipywidgets as widgets
from ..widget import Widget
import base64

class Image(Widget):
    #Image height is ignored as in CSS from jupyter it is set as auto only the width matters.
    #https://github.com/jupyter-widgets/ipywidgets/issues/1689 <- Reference

    def __init__(self,widgetManager,ID,y):
        self.manager = widgetManager
        self.__initVariables__(ID,y)
        self.__initViews__()

    def __initVariables__(self,ID,y):
        file = open("img.png", "rb")
        self.id = ID
        image = file.read()
        self.value = image
        self.x = 0
        self.y = y

    def __initViews__(self):
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

    def getAttribsView(self):
        #4th Information View
        attribs = []
        attribs.append(widgets.IntText(description="Column: " , value= str(self.x)))
        attribs.append(widgets.IntText(description="Line: " , value = str(self.y)))
        attribs.append(widgets.Text(description="ID: ", value =""+ str(self.id)))
        attribs.append(widgets.HTML(value="<b>Widget Details: </b>"))
        attribs.append(widgets.IntText(description="Width: ", value = int(self.widget.width)))
        attribs.append(widgets.IntText(description="Height: ", value = int(self.widget.height)))
        attribs.append(widgets.FileUpload())

        return attribs


    def getAttribsDev(self):
        attribs = []
        attribs.append(self.x)
        attribs.append(self.y)
        attribs.append(self.id)
        attribs.append("")
        attribs.append(self.width)
        attribs.append(self.height)
        attribs.append(self.value)

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
        self.width = attribs[4].value
        self.height = attribs[5].value

        #VALUE
        
        valueTemp = attribs[6].value
        if(len(valueTemp) > 0):
            value= list(valueTemp)[0]
            self.value=valueTemp[value].get('content')
        

        self.widget = widgets.Image(
                                        value=self.value,
                                        width=self.width,
                                        height=self.height
                                        )
      
        self.manager.replaceWidget(currentScreen,self)

    def widgetLoader(self, currentScreen,attribs):
        self.x = attribs[0]
        self.y = attribs[1]
        
        #ID
        id = attribs[2]
        if(len(id)>=0):
            self.id = id
            self.represent.description = "Image - "+ str(id)

        #Size
        self.width = attribs[4]
        self.height = attribs[5]

        #VALUE
        
        valueTemp = attribs[6]
        if(len(valueTemp) > 0):
            value= list(valueTemp)[0]
            self.value=valueTemp[value].get('content')
        

        self.widget = widgets.Image(
                                        value=self.value,
                                        width=self.width,
                                        height=self.height
                                        )
      
        self.manager.replaceWidget(currentScreen,self)

    def save(self):
        tempVal = base64.encodebytes(self.value).decode('utf-8')
        attribs = ["Image",self.x,self.y,self.id,"",self.width,self.height,tempVal]
        return attribs

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

