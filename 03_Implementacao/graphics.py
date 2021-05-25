from ipywidgets import AppLayout, Button, Layout, Tab, Text, HBox, VBox, GridBox, Label, Layout, Box, Label, GridspecLayout
import ipyvuetify as v
from ipywidgets.widgets import widget
from widgetManager import WidgetManager

class Graphics():

    def __init__(self,widgetManager) -> None:
        self.widgetManager = widgetManager
        self.selectedWidget = None
        self.graphics = self.initApp()
        self.sideBar = None

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

    def setSelectedWidget(self,wid):
        
        self.selectedWidget = wid
        
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

        sizePreview = len(self.widgetManager.widgetsPreview)
        widgetPreview = self.widgetManager.widgetsPreview

        box = [HBox for x in widgetPreview]

        preview = GridspecLayout(sizePreview+2,3,layout=Layout(border='1px solid',align_items='center'))
        if(sizePreview>0):
            for i in range(sizePreview):
                preview[i,0] = widgetPreview[i]
        
        return preview

    def onClick_Instanciate(self,b):
        self.widgetManager.addWidget(b.description)
        self.sideBar.selected_index = 0

    def __initInspector__(self):

        intSlider = self.createButton('IntSlider')
        intSlider.on_click(self.onClick_Instanciate)
        button = self.createButton('Button')
        button.on_click(self.onClick_Instanciate)
        image = self.createButton('Image')
        image.on_click(self.onClick_Instanciate)

        widgetsInspector = []
        widgetsAtribs = []

        if(self.selectedWidget != None):
            widgetsAtribs = self.selectedWidget.attribs
            widgetsAtribs.append(Button(description="Apply"))
            
        if(len(self.widgetManager.widgetsInspector) >= 1):
            widgetsInspector = self.widgetManager.widgetsInspector
            

        inspectorItems = [VBox(widgetsInspector,layout=Layout(border='1px solid',height='420px',margin='0px 0px 30px 0px',align_items='center')), 
                VBox(widgetsAtribs,layout=Layout(border='1px solid',height='150px',align_items='center'))]

        inspector = VBox([inspectorItems[0], inspectorItems[1]],layout=Layout())

        widgetsAddWidgets = [intSlider,button,image]
        addWidgets = VBox(widgetsAddWidgets, layout=Layout(align_items='center'))
        sideBar_contents = ['Add Widget', 'Widgets Inspector']
        children_sideBar = [addWidgets,inspector]

        sideBar = Tab()
        sideBar.children = children_sideBar
        #sideBar.selected_index = None
        for i in range(len(children_sideBar)):
            sideBar.set_title(i, sideBar_contents[i])
        self.sideBar = sideBar
        
        return sideBar


    def __initFooter__(self):
        pass


    def initApp(self):
        #Combine all previous information into one place (Can be used to ReDraw as well!)
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