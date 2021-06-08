from ipywidgets import AppLayout, Button, Layout, Tab, Text, HBox, VBox, GridBox, Label, Layout, Box, Label, GridspecLayout, Image
import ipyvuetify as v
import ipywidgets
from ipywidgets.widgets import widget
from ipywidgets.widgets.widget_style import Style
from widgetManager import WidgetManager

class Graphics():

    def __init__(self,widgetManager,application) -> None:
        self.widgetManager = widgetManager
        self.app = application
        self.__initVariables__()
        self.graphics = self.initApp()
        
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


    def __initHeader__(self):
        tab_contents_title = ['New App', 'Edit App']

        items = [v.ListItem(children=[
            v.ListItemTitle(children=[
                tab_contents_title[0]])]),
                v.ListItem(children=[
            v.ListItemTitle(children=[
                tab_contents_title[1]])])]

        for item in items:
            item.on_event('click', self.on_menu_click)

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
        previewSize = 20

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

        preview = VBox(box, layout=Layout(border='0.8px solid grey', padding='30px'))
        preview.add_class('preview')
        
        return preview

    def onClick_Instanciate(self,b):
        self.clearSelectedWidget()
        self.sideBar.selected_index = 0
        self.widgetManager.addWidget(self.currentScreen,b.description,str(self.minID),self.y)
        if(self.y < 20):
            self.y += 1
        self.minID += 1

    def __initInspector__(self):
        #Initialize all the buttons for new Instances TODO
        intSlider = self.createButton('IntSlider')
        intSlider.on_click(self.onClick_Instanciate)
        button = self.createButton('Button')
        button.on_click(self.onClick_Instanciate)
        html = self.createButton('HTML')
        html.on_click(self.onClick_Instanciate)
        markdown = self.createButton('Markdown')
        markdown.on_click(self.onClick_Instanciate)
        textBox = self.createButton('Text Input')
        textBox.on_click(self.onClick_Instanciate)
        image = self.createButton('Image')
        image.on_click(self.onClick_Instanciate)

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
        widgetsAddWidgets = [button,html,markdown,textBox,image]
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
        file = open("footer.png", "rb")
        image = file.read()
        footer = Image(value = image, layout = Layout(width='99%'))

        return footer

    
        
    def initApp(self):
        menu = self.__initHeader__()
        preview = self.__initPreview__()
        sideBar = self.__initInspector__()
        footerImg = self.__initFooter__()

        appLayout = AppLayout(header=menu,
          left_sidebar=None,
          center= preview,
          right_sidebar=sideBar,
          footer = footerImg,
          pane_heights=['50px', 3.5,1],
         grid_gap="20px")

        return appLayout

    def updateGraphics(self):
        preview = self.__initPreview__()
        sidebar = self.__initInspector__()
        self.graphics.right_sidebar = sidebar
        self.graphics.center = preview

    def newScreen(self,b):
        self.maxScreenNumber += 1
        self.currentScreenButton.button_style = ''
        self.currentScreen = self.maxScreenNumber
        self.currentScreenButton =   self.createButton("Screen: " + str(self.maxScreenNumber))
        self.currentScreenButton.on_click(self.changeScreen)
        self.currentScreenButton.button_style = 'warning'
        self.screens.append(self.currentScreenButton)
        #Reset selected widget
        self.clearSelectedWidget()
        self.widgetManager.newScreen()
        
        
    def changeScreen(self,b):
        self.currentScreenButton.button_style = ''
        self.currentScreen = int(b.description.split()[1])
        self.currentScreenButton = self.screens[int(b.description.split()[1])+1]
        self.currentScreenButton.button_style = 'warning'
        #Reset selected widget
        self.clearSelectedWidget()
        self.app.redraw()

        

    def setSelectedWidget(self,wid):
        if(self.selectedWidget != None):
            self.selectedWidget.represent.button_style=''
        self.selectedWidget = wid
        

    def createButton(self,desc, style = ''):
        out = Button(
                description= desc,
                disabled=False,
                button_style=style, 
                tooltip='Click me',
                )
        return out

    def on_menu_click(self,widget, event, data):
        if len(widget.layout.children) == 1:
            widget.layout.children = widget.layout.children + [widget.info]
        widget.info.children=[f'Item {widget.items.index(widget)+1} clicked']
        
    def clearSelectedWidget(self):
        #Reset selectedWidget
        if(self.selectedWidget != None):
            self.selectedWidget.represent.button_style=''
        self.selectedWidget = None  
