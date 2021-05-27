from ipywidgets import AppLayout, Button, Layout, Tab, Text, HBox, VBox, GridBox, Label, Layout, Box, Label, GridspecLayout
import ipyvuetify as v
from ipywidgets.widgets import widget
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
        buttonScreen = self.createButton('New Screen')
        buttonScreen.on_click(self.newScreen)
        FirstScreen = self.createButton('0')
        FirstScreen.on_click(self.changeScreen)
        self.screens = []
        self.screens.append(buttonScreen)
        self.screens.append(FirstScreen)
        self.sideBar = None


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
        items = Label(str(1))

        sizePreview = len(self.widgetManager.screens[self.currentScreen][2])
        widgetPreview = self.widgetManager.screens[self.currentScreen][2]
        

        box = [HBox for x in widgetPreview]

        preview = GridspecLayout(sizePreview+2,3,layout=Layout(border='1px solid',align_items='center'))
        if(sizePreview>0):
            for i in range(sizePreview):
                preview[i,0] = widgetPreview[i]
        
        return preview

    def onClick_Instanciate(self,b):
        self.widgetManager.addWidget(self.currentScreen,b.description)
        self.sideBar.selected_index = 0

    def __initInspector__(self):

        #Initialize all the buttons for new Instances TODO
        intSlider = self.createButton('IntSlider')
        intSlider.on_click(self.onClick_Instanciate)
        button = self.createButton('Button')
        button.on_click(self.onClick_Instanciate)
        image = self.createButton('Image')
        image.on_click(self.onClick_Instanciate)

        #Inspector Definition
        widgetsInspector = []
        self.widgetsAtribs = []

        #Apply for Attribs
        Apply = Button(description="Apply")
        Apply.on_click(self.apply_changes)

        #Attribs View
        if(self.selectedWidget != None):
            self.widgetsAtribs = self.selectedWidget.getAttribsView()
            self.widgetsAtribs.append(Apply)
        
        #Get Inspector Views
        if(len(self.widgetManager.screens[self.currentScreen][1]) >= 1):
            widgetsInspector = self.widgetManager.screens[self.currentScreen][1]
            
        #Inspector
        inspectorItems = [VBox(widgetsInspector,layout=Layout(border='1px solid',height='420px',margin='0px 0px 30px 0px',align_items='center')), VBox(self.widgetsAtribs,layout=Layout(border='1px solid',height='150px',align_items='center'))]
        inspector = VBox([inspectorItems[0], inspectorItems[1]],layout=Layout())

        #WidgetsAdd
        widgetsAddWidgets = [intSlider,button,image]
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

    def apply_changes(self, b):
        self.selectedWidget.widgetUpdate(self.currentScreen,self.widgetsAtribs)

    def __initFooter__(self):
        pass


    def initApp(self):
        menu = self.__initHeader__()
        preview = self.__initPreview__()
        sideBar = self.__initInspector__()
        

        appLayout = AppLayout(header=menu,
          left_sidebar=None,
          center= preview,
          right_sidebar=sideBar,
          pane_widths=[3,3,2],
          pane_heights=[1, 13,1],
         grid_gap="20px")

        return appLayout

    def newScreen(self,b):
        self.maxScreenNumber += 1
        self.currentScreen = self.maxScreenNumber
        buttonScreen = self.createButton(str(self.maxScreenNumber))
        buttonScreen.on_click(self.changeScreen)
        self.screens.append(buttonScreen)
        self.widgetManager.newScreen()
        
    def changeScreen(self,b):
        self.currentScreen = int(b.description)
        self.app.redraw()
        

    def setSelectedWidget(self,wid):
        self.selectedWidget = wid

    def createButton(self,desc):
        out = Button(
                description= desc,
                disabled=False,
                button_style='', 
                tooltip='Click me'#,
                #icon='check'
                )
        return out

    def on_menu_click(self,widget, event, data):
        if len(widget.layout.children) == 1:
            widget.layout.children = widget.layout.children + [widget.info]
        widget.nfo.children=[f'Item {widget.items.index(widget)+1} clicked']
        