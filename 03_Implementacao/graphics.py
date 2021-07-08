from ipywidgets import AppLayout, Button, Layout, Tab, Text, HBox, VBox, GridBox, Label, Layout, Box, Label, GridspecLayout, Image,HTML
import ipyvuetify as v
import ipywidgets
from ipyvuetify.extra import FileInput
from ipywidgets.widgets import widget
from ipywidgets.widgets.widget_style import Style
from widgetManager import WidgetManager

class Graphics():

    def __init__(self,application,editMode) -> None:
        self.app = application
        self.widgetManager = self.app.widgetManager
        self.__initVariables__()
        self.editMode = editMode
        self.graphics = self.initApp()

    def __initHeader__(self):
        tab_contents_title = ['New', 'Save','Export Notebook']

        items = [v.ListItem(children=[
            v.ListItemTitle(children=[
                tab_contents_title[0]])]),
                v.ListItem(children=[
            v.ListItemTitle(children=[
                tab_contents_title[1]])]),
                v.ListItem(children=[
            v.ListItemTitle(children=[
                tab_contents_title[2]])])]

        for item in items:
            item.on_event('click', self.app.newApp)

        items[1].on_event('click', self.app.saveDataMenu)
        items[2].on_event('click', self.app.exportNotebook)

        menu = v.Menu(layout = Layout(width='150px'),offset_y=True,
            v_slots=[{
                'name': 'activator',
                'variable': 'menuData',
                'children': v.Btn(v_on='menuData.on', class_='ma-2', color='primary', children=[
                    'menu', 
                    v.Icon(right=True, children=[
                        'mdi-menu-down'
                    ])
                ]),
            }]
            ,
            children=[
                
                v.List(children=items)
            ]
        )
        return menu

    def __initPreview__(self):
        previewSize = 50

        widgetPreview = self.widgetManager.screens[self.currentScreen][2]
        widgetsParents = self.widgetManager.screens[self.currentScreen][0]
        
        layoutPreview = Layout(flex_flow='row',align_items='center',
                    display='flex', width='100%', border = '0px', margin='0 0 5px 0')
        box = []
        for y in range(previewSize):
            positions = []
            widgetsXFinal = []
            for yx in range(len(widgetsParents)):
                if(widgetsParents[yx].y == y):
                    positions.append(yx)
            for x in range(previewSize):
                for xy in range(len(positions)):
                    if(widgetsParents[positions[xy]].x == x):
                        widgetsXFinal.append(widgetPreview[positions[xy]])
            box.append(HBox(widgetsXFinal, layout = layoutPreview))

        layoutV = None
        if(self.editMode):
            layoutV = Layout(border='0.8px solid grey', padding='30px')
        else:
            layoutV = Layout()

        preview = VBox(box, layout=layoutV)
        preview.add_class('inspector')
        
        return preview

    def onClick_Instanciate(self,b):
        self.clearSelectedWidget()
        self.sideBar.selected_index = 0
        self.widgetManager.addWidget(self.currentScreen,b.description,str(self.minID),self.y)
        if(self.y < 20):
            self.y += 1
        self.minID += 1

    def __initInspector__(self):

        #Inspector Definition
        widgetsInspector = []
        self.widgetsAtribs = []

        #Apply for Attribs
        Apply = Button(description="Apply Changes", button_style = 'success', layout = Layout(margin = '10px'))
        Apply.on_click(self.apply_changes)
        Apply.add_class('button')
        Delete = Button(description="Delete Widget", button_style = 'danger', layout = Layout(margin = '10px'))
        Delete.on_click(self.deleteWidget)
        Delete.add_class('button')

        #Attribs View
        if(self.selectedWidget != None):
            self.widgetsAtribs = self.selectedWidget.getAttribsView()
            self.widgetsAtribs.append(HBox([Apply,Delete], layout = Layout()))

            #Selected widget bg
            self.selectedWidget.represent.button_style='warning'
        

        #Get Inspector Views
        if(len(self.widgetManager.screens[self.currentScreen][1]) >= 1):
            widgetsInspector = self.widgetManager.screens[self.currentScreen][1]
            
        #Inspector
        inspectorItems = [VBox(widgetsInspector,layout=Layout(border='1px solid slategray',height='auto', min_height='20%',margin='0px 0px 30px 0px',align_items='center')), 
        VBox(self.widgetsAtribs,layout=Layout(border='1px solid slategray',height='auto', min_height='40%',align_items='center',overflow_y='auto'))]
        inspector = VBox([inspectorItems[0], inspectorItems[1]],layout=Layout(height = '100%'))

        #WidgetsAdd
        widgetsAddWidgets = self.initializeInspectorAddTab()
        addWidgets = VBox(widgetsAddWidgets, layout=Layout(align_items='center'))

        #Screens
        screensView = VBox(self.screens, layout=Layout(align_items='center'))

        sideBar_contents = ['Add Widget', 'Widgets Inspector', 'Screens']
        children_sideBar = [addWidgets,inspector, screensView]

        sideBar = Tab()
        sideBar.children = children_sideBar
        if(self.selectedWidget != None):
            sideBar.selected_index = 1
        for i in range(len(children_sideBar)):
            sideBar.set_title(i, sideBar_contents[i])
        self.sideBar = sideBar
        
        return sideBar

    def deleteWidget(self,b):
        
        self.widgetManager.deleteWidget(self.currentScreen,self.selectedWidget)
        self.clearSelectedWidget()
        self.app.redraw()
        

    def apply_changes(self, b):
        self.selectedWidget.widgetUpdate(self.currentScreen,self.widgetsAtribs)

    def __initFooter__(self):
        file = open("resources/footer.png", "rb")
        image = file.read()
        footer = Image(value = image, layout = Layout(width='99%'))

        return footer

    def initApp(self):
        menu = self.__initHeader__()
        preview = self.__initPreview__()
        sideBar = self.__initInspector__()
        footerImg = self.__initFooter__()

        if(self.editMode):
            appLayout = AppLayout(header=menu,left_sidebar=None,center= preview, right_sidebar=sideBar,footer = footerImg,pane_heights=['50px', 3.5,1],grid_gap="20px")
        else:
            appLayout = AppLayout(header=None,left_sidebar=None,center= preview, right_sidebar=None ,footer = None,pane_heights=['50px', 3.5,1],grid_gap="20px")

        return appLayout

    def updateGraphics(self):
        if(self.editMode):
            sidebar = self.__initInspector__()
            self.graphics.right_sidebar = sidebar
        preview = self.__initPreview__()
        self.graphics.center = preview

    def resetGraphics(self):
        self.widgetManager = self.app.widgetManager
        self.__initVariables__()
        menu = self.__initHeader__()
        preview = self.__initPreview__()
        sideBar = self.__initInspector__()
        footerImg = self.__initFooter__()

        self.graphics.header = menu
        self.graphics.right_sidebar = sideBar
        self.graphics.center = preview
        self.graphics.footer = footerImg
        
    def newScreen(self,b):
        self.maxScreenNumber += 1
        self.currentScreenButton.button_style = ''
        self.currentScreen = self.maxScreenNumber
        self.currentScreenButton =  self.createButton("Screen: " + str(self.maxScreenNumber))
        self.currentScreenButton.on_click(self.changeScreen)
        self.currentScreenButton.button_style = 'warning'
        self.screens.append(self.currentScreenButton)
        self.clearSelectedWidget()
        self.widgetManager.newScreen()
        
    def setSelectedScreen(self, number):
        self.currentScreenButton.button_style = ''
        self.currentScreen = number
        self.currentScreenButton = self.screens[number+1]
        self.currentScreenButton.button_style = 'warning'
        self.clearSelectedWidget()
        self.app.redraw()

    def changeScreen(self,b):
        self.currentScreenButton.button_style = ''
        self.currentScreen = int(b.description.split()[1])
        self.currentScreenButton = self.screens[int(b.description.split()[1])+1]
        self.currentScreenButton.button_style = 'warning'
        self.clearSelectedWidget()
        self.app.redraw()

    def setSelectedWidget(self,wid):
        if(self.selectedWidget != None):
            self.selectedWidget.represent.button_style=''
        self.selectedWidget = wid
        
    def createButton(self,desc, style = ''):
        out = Button( description= desc, disabled=False, button_style=style,  tooltip='Click me', )
        return out

    def createTitle(self,text):
        out = HTML(value = text)
        return out

    def on_menu_click(self,widget, event, data):
        if len(widget.layout.children) == 1:
            widget.layout.children = widget.layout.children + [widget.info]
        widget.info.children=[f'Item {widget.items.index(widget)+1} clicked']
        
    def clearSelectedWidget(self):
        if(self.selectedWidget != None):
            self.selectedWidget.represent.button_style=''
        self.selectedWidget = None  

    def initializeInspectorAddTab(self):
        #TITLE
        dropdownsTitle = self.createTitle('<strong>Dropdown Widgets</strong>')
        #----
        dropdown = self.createButton('Dropdown')
        dropdown.on_click(self.onClick_Instanciate)
        radiobuttons = self.createButton('RadioButtons')
        radiobuttons.on_click(self.onClick_Instanciate)

        #TITLE
        slidersTitle = self.createTitle('<strong>Slider Widgets</strong>')
        #----
        intSlider = self.createButton('IntSlider')
        intSlider.on_click(self.onClick_Instanciate)
        intProgress = self.createButton('IntProgress')
        intProgress.on_click(self.onClick_Instanciate)
        floatSlider = self.createButton('FloatSlider')
        floatSlider.on_click(self.onClick_Instanciate)
        floatLogSlider = self.createButton('FloatLogSlider')
        floatLogSlider.on_click(self.onClick_Instanciate)
        floatProgress = self.createButton('FloatProgress')
        floatProgress.on_click(self.onClick_Instanciate)

        #TITLE
        textTitle = self.createTitle('<strong>Text Widgets</strong>')
        #----
        html = self.createButton('HTML')
        html.on_click(self.onClick_Instanciate)
        markdown = self.createButton('Markdown')
        markdown.on_click(self.onClick_Instanciate)
        textBox = self.createButton('Text Input')
        textBox.on_click(self.onClick_Instanciate)
        password = self.createButton('Password')
        password.on_click(self.onClick_Instanciate)
        intText = self.createButton('IntText')
        intText.on_click(self.onClick_Instanciate)
        floatText = self.createButton('FloatText')
        floatText.on_click(self.onClick_Instanciate)

        #TITLE
        othersTitle = self.createTitle('<strong>Other Widgets</strong>')
        #----
        button = self.createButton('Button')
        button.on_click(self.onClick_Instanciate)
        image = self.createButton('Image')
        image.on_click(self.onClick_Instanciate)
        checkbox = self.createButton('Checkbox')
        checkbox.on_click(self.onClick_Instanciate)
        valid = self.createButton('Valid')
        valid.on_click(self.onClick_Instanciate)

        return [dropdownsTitle,dropdown, radiobuttons,slidersTitle, intSlider,intProgress,floatSlider,floatLogSlider,floatProgress,textTitle,html,markdown,textBox,password,intText,floatText,othersTitle,button,image,checkbox,valid]
       
    def __initVariables__(self):
        self.selectedWidget = None  
        self.currentScreen = 0
        self.maxScreenNumber = 0
        buttonScreen = self.createButton('Add New Screen','info')
        buttonScreen.on_click(self.newScreen)
        FirstScreen = self.createButton("Screen: 0", 'warning')
        FirstScreen.on_click(self.changeScreen)
        self.currentScreenButton = FirstScreen
        self.screens = []
        self.screens.append(buttonScreen)
        self.screens.append(self.currentScreenButton)
        self.sideBar = None
        self.minID = 0
        self.y = 0