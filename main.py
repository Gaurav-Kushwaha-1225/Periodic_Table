from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel, MDIcon
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.button import MDRectangleFlatButton, MDRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivy.utils import rgba
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.transition import MDFadeSlideTransition
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList, TwoLineListItem, TwoLineAvatarListItem, TwoLineIconListItem, IconLeftWidget, OneLineIconListItem, ILeftBody
from kivy.lang import Builder
import webbrowser
from kivy.uix.image import AsyncImage


Builder.load_string('''
#:import hex kivy.utils.get_color_from_hex

<Search_Description>:
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            id: search_top_bar
            halign: "left"
            left_action_items: [["arrow-left", lambda x: root.change2()]]
            md_bg_color: hex("#630436")
    
        MDBoxLayout:
            padding: 10
            spacing: 30
            adaptive_height: True
            MDIconButton:
                icon: "magnify"
                disabled: True
            MDTextField:
                id: field
                hint_text: "Search Element Name "
                on_text: root.set_list_md_icons(self.text)
                
        MDBoxLayout:
            orientation: 'vertical'
            padding: 10
            RecycleView:
                id: rv
                data: root.names
                key_viewclass: 'viewclass'
                key_size: 'height'
        
                RecycleBoxLayout:
                    spacing: 20
                    default_size_hint: 1, None
                    default_size: None,70
                    size_hint_y: None
                    height: self.minimum_height
                    orientation: 'vertical'

<CustomListItem>
    on_release: root.playboy(self)

    text: root.text1
    theme_text_color: "Custom"
    text_color: hex("#FCFBFC")
    font_style: "H6"
    
    secondary_text: root.text2
    secondary_theme_text_color: "Custom"
    secondary_font_style: "H6"
    
    divider: "Inset"
    radius: 10

    LabelLeftWidget:
        id: left_label
        text: root.icon_text
        halign: "center"
        markup: True
        canvas.before:
            Color:
                rgba: hex(root.color_icon)
            RoundedRectangle:
                pos: (self.pos[0]-dp(4), self.pos[1]-dp(4))
                size: (self.size[0]+dp(7), self.size[1]+dp(7))
                radius:[(50,50),(50,50),(50,50),(50,50)]

<CustomHeader>:
    orientation: "horizontal"
    md_bg_color: hex("#202028")
    spacing: 10
    padding: 35

    MDIcon:
        icon: "circle-double"
        font_size: "25dp"
        theme_text_color: "Custom"
        text_color: hex(root.color)
        pos_hint: {"center_x":0.2, "center_y":0.5}

    MDLabel:
        text: root.header
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.5}
'''
)


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box = MDBoxLayout(orientation="vertical")

        # TopAppBar
        TopBar = MDTopAppBar(title="[font=assets/fonts/arlrdbd.ttf][size=35][b]Periodic Table[/b][/size][/font]",
                             right_action_items=[["sort-variant", lambda x: self.show0()]], md_bg_color=rgba("#630436"))

        # BottomAppBar
        BottomBar = MDBottomNavigation(panel_color=rgba(
            "#630436"), text_color_active=rgba("#E39FF6"), widget_style="android", radius=20, padding=20, selected_color_background=rgba("#A1045A"))
        BottomBar.mode = "legacy"

        home_nav_item = MDBottomNavigationItem(
            name='Element_screen', text='Periodic Table', icon='periodic-table')
        home_nav_item.add_widget(Elements_Portion())
        BottomBar.add_widget(home_nav_item)

        dict_nav_item = MDBottomNavigationItem(
            name='Dictionary', text='Dictionary', icon='table', widget_style='android')
        dict_nav_item.add_widget(Dictionary())
        BottomBar.add_widget(dict_nav_item)

        search_nav_item = MDBottomNavigationItem(
            name='Search', text='Search Element', icon='table-search')
        search_nav_item.add_widget(Search())
        BottomBar.add_widget(search_nav_item)

        about_nav_item = MDBottomNavigationItem(
            name='Other', text='Other', icon='dots-hexagon')
        about_nav_item.add_widget(OtherScreen())
        BottomBar.add_widget(about_nav_item)

        # Add text_color_normal after adding all the items
        BottomBar.text_color_normal = rgba("#E39FF6")

        # Adding widgets to HomePage
        box.add_widget(TopBar)
        box.add_widget(BottomBar)
        self.add_widget(box)

    def show0(self):
        dialog = None
        if not dialog:
            self.dialog = MDDialog(
                title="Categories: ", type="custom", content_cls=description_content())
        self.dialog.open()

    def change0(self):
        self.manager.current = "Screen 2"


class OtherScreen(MDScreen):

    scroll = MDScrollView()
    scroll.size = scroll.size

    store = JsonStore("assets/data/others.json")
    data = store.get("data")


    def __init__(self, *args, **kwargs):
        super(OtherScreen, self).__init__(*args, **kwargs)
        
        self.main_box = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        self.main_box.adaptive_height = True

        about_header = CustomHeader(header="[size=30sp][font=assets/fonts/arlrdbd.ttf][b]  About:[/b][/font][/size]", color="#3DED97", size_hint_y=None, height=60, line_width=2, line_color=rgba("#26282A"))
        about_label = MDLabel(text=f"[font=assets/fonts/SegUIVar.ttf][size=23sp]{self.data['about']}[/size][/font]", markup=True, adaptive_height =True, valign='center')

        social_header = CustomHeader(header="[size=30sp][font=assets/fonts/arlrdbd.ttf][b]  Follow us on social networks:[/b][/font][/size]", color="#F9E076", size_hint_y=None, height=60, line_width=2, line_color=rgba("#26282A"))
        github = TwoLineIconListItem(IconLeftWidget(icon='github', theme_text_color="Custom", text_color= rgba("#FFFFFF"), icon_size=35, _no_ripple_effect=True), text="[b]GitHub  Repository  Link[/b]", secondary_text="https://github.com/Gaurav-Kushwaha-1225/Periodic_Table.git" ,secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset")
        github.bind(on_release=lambda x: webbrowser.open("https://github.com/Gaurav-Kushwaha-1225/Periodic_Table.git"))
        linkedin = TwoLineIconListItem(IconLeftWidget(icon='linkedin', theme_text_color="Custom", text_color= rgba("#0077B5"), icon_size=35, _no_ripple_effect=True), text="[b]LinkedIn[/b]", secondary_text="https://www.linkedin.com/in/gaurav-kushwaha-330a39251/" ,secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset")
        linkedin.bind(on_release=lambda x: webbrowser.open("https://www.linkedin.com/in/gaurav-kushwaha-330a39251/"))
        
        devs_header = CustomHeader(header="[size=30sp][font=assets/fonts/arlrdbd.ttf][b]  Project Developers:[/b][/font][/size]", color="#FC6A03", size_hint_y=None, height=60, line_width=2, line_color=rgba("#26282A"))
        name_label = MDLabel(text="[font=assets/fonts/arlrdbd.ttf][size=35sp][b]   Gaurav  Kushwaha[/b][/size][/font]", markup=True, adaptive_height=True, valign='center')
        mail = OneLineIconListItem(IconLeftWidget(icon='email', theme_text_color="Custom", text_color= rgba("#FFFC00"), icon_size=35, _no_ripple_effect=True), text="[b]  E-Mail[/b]", font_style="H6", radius=5, divider="Inset")
        ig = OneLineIconListItem(IconLeftWidget(icon='instagram', theme_text_color="Custom", text_color= rgba("#E3242B"), icon_size=35, _no_ripple_effect=True), text="[b]  Instagram[/b]", font_style="H6", radius=5, divider="Inset")
        ig.bind(on_release=lambda x: webbrowser.open("https://www.instagram.com"))
        facebook = OneLineIconListItem(IconLeftWidget(icon='facebook', theme_text_color="Custom", text_color= rgba("#3B5998"), icon_size=35, _no_ripple_effect=True), text="[b]  Facebook[/b]", font_style="H6", radius=5, divider="Inset")
        facebook.bind(on_release=lambda x: webbrowser.open("https://m.facebook.com"))
        twitter = OneLineIconListItem(IconLeftWidget(icon='twitter', theme_text_color="Custom", text_color= rgba("#55ACEE"), icon_size=35, _no_ripple_effect=True), text="[b]  Twitter[/b]", font_style="H6", radius=5, divider="Inset")
        twitter.bind(on_release=lambda x: webbrowser.open("https://twitter.com"))

        data_header = CustomHeader(header="[size=30sp][font=assets/fonts/arlrdbd.ttf][b]  Data Source:[/b][/font][/size]", color="#82EEFD", size_hint_y=None, height=60, line_width=2, line_color=rgba("#26282A"))
        data = TwoLineIconListItem(IconLeftWidget(icon='github', theme_text_color="Custom", text_color= rgba("#FFFFFF"), icon_size=35, _no_ripple_effect=True), text="[b]GitHub  Repository  Link  Of  Data  Source[/b]", secondary_text="https://github.com/Bowserinator/Periodic-Table-JSON.git" ,secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset")
        data.bind(on_release= lambda x: webbrowser.open("https://github.com/Bowserinator/Periodic-Table-JSON.git"))
        
        bug_header = CustomHeader(header="[size=30sp][font=assets/fonts/arlrdbd.ttf][b]  Extra:[/b][/font][/size]", color="#ADADC9", size_hint_y=None, height=60, line_width=2, line_color=rgba("#26282A"))
        bug = TwoLineIconListItem(IconLeftWidget(icon='bug', theme_text_color="Custom", text_color= rgba("#900D09"), icon_size=35, _no_ripple_effect=True), text="[b]Report a Bug[/b]", secondary_text="Help us make the app better" ,secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True)
        
        # Adding widgets to main box
        self.main_box.add_widget(about_header)
        self.main_box.add_widget(about_label)
        self.main_box.add_widget(social_header)
        self.main_box.add_widget(github)
        self.main_box.add_widget(linkedin)
        self.main_box.add_widget(devs_header)
        self.main_box.add_widget(name_label)
        self.main_box.add_widget(mail)
        self.main_box.add_widget(ig)
        self.main_box.add_widget(facebook)
        self.main_box.add_widget(twitter)
        self.main_box.add_widget(data_header)
        self.main_box.add_widget(data)
        self.main_box.add_widget(bug_header)
        self.main_box.add_widget(bug)

        #adding box layout to scroll view
        self.scroll.add_widget(self.main_box)
        self.add_widget(self.scroll)


class CustomHeader(MDBoxLayout):
    header = StringProperty()
    color = StringProperty()


class Element_Description(MDScreen):

    def __init__(self, *args, **kwargs):
        global TopBar0, label1, label2, card1, overview, e_val_label, p_val_label, n_val_label, img, img_lab, property, atomic
        super(Element_Description, self).__init__(*args, **kwargs)

        # OuterMost box
        OuterMostBox = MDBoxLayout(orientation="vertical")

        # Header or TopAppBar
        TopBar0 = MDTopAppBar(left_action_items=[
            ["arrow-left", lambda x: self.change1()]], md_bg_color=rgba("#630436"))

        # main box Layout
        MainBox = MDBoxLayout(orientation="vertical", padding=8,
                              spacing=8)

        # Main Scroll View
        scroll = MDScrollView()

        # Creating Outer BoxLayout
        OuterBox = MDBoxLayout(orientation="vertical",
                               spacing=8, adaptive_height=True)

        # 1st MDCard
        card1 = MDCard(md_bg_color=rgba(
            "#20242b"), style="elevated", size_hint=(1, None), height="150dp")
        # 1 label and 1 BoxLayout in MDcard
        label1 = MDLabel(markup=True, halign="left")
        box1 = MDBoxLayout(orientation="vertical")

        # 2 Labels in BoxLayout present in MDCard
        label2 = MDLabel(markup=True, halign="center", valign="bottom")
        box1.add_widget(MDLabel(text=""))  # 2nd Label
        box1.add_widget(label2)
        card1.add_widget(label1)
        card1.add_widget(box1)

        # Overview of the Element
        # Overview List Item
        overview_box1 = MDBoxLayout()
        overview_label = MDCard(md_bg_color=rgba(
            "#A91B0D"), size_hint=(None, None), height=40, width=145)
        overview_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   OVERVIEW:[/b][/color][/size]", markup=True, halign="left"))

        overview_box2 = MDBoxLayout()
        overview = MDList()
        overview_box1.adaptive_height = 40
        overview_box2.adaptive_height = overview.adaptive_height
        overview_box1.add_widget(overview_label)
        overview_box2.add_widget(overview)

        # BoxLayout(box2) for Electrons, Protons And Neutrons
        box2 = MDBoxLayout(orientation="horizontal", spacing=6)
        box3 = MDBoxLayout(orientation="horizontal", spacing=6)

        electron = MDCard(md_bg_color=rgba(
            "#D0312D"), size_hint=(1, None), height=50)
        electron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]ELECTRONS:[/b][/color][/size]", markup=True, halign="center")
        electron.add_widget(electron_label)
        e_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("D0312D"), size_hint=(1, None), height=50)
        e_val_label = MDLabel(markup=True, halign="center", line_width=5)
        e_val.add_widget(e_val_label)

        proton = MDCard(md_bg_color=rgba(
            "#FBB917"), size_hint=(1, None), height=50)
        proton_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]PROTONS:[/b][/color][/size]", markup=True, halign="center")
        proton.add_widget(proton_label)
        p_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("FBB917"), size_hint=(1, None), height=50)
        p_val_label = MDLabel(markup=True, halign="center", line_width=5)
        p_val.add_widget(p_val_label)

        neutron = MDCard(md_bg_color=rgba(
            "#3944BC"), size_hint=(1, None), height=50)
        neutron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]NEUTRONS:[/b][/color][/size]", markup=True, halign="center")
        neutron.add_widget(neutron_label)
        n_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("3944BC"), size_hint=(1, None), height=50)
        n_val_label = MDLabel(markup=True, halign="center", line_width=5)
        n_val.add_widget(n_val_label)

        box2.adaptive_height = 50
        box3.adaptive_height = 50
        box2.add_widget(electron)
        box2.add_widget(proton)
        box2.add_widget(neutron)
        box3.add_widget(e_val)
        box3.add_widget(p_val)
        box3.add_widget(n_val)

        # BoxLayout (box_img) for image
        img_box1 = MDBoxLayout()
        img_label = MDCard(md_bg_color=rgba(
            "#000080"), size_hint=(None, None), height=40, width=110)
        img_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   IMAGE:[/b][/color][/size]", markup=True, halign="left"))

        img_box2 = MDBoxLayout(
            pos_hint={"center_x": 0.5}, spacing=25, padding=25)
        img = AsyncImage(size_hint=(None, None), height=300, width=300)
        img_lab = MDLabel(markup=True)

        img_box1.adaptive_height = 40
        img_box2.adaptive_height = img.height
        img_box1.add_widget(img_label)
        img_box2.add_widget(img)
        img_box2.add_widget(img_lab)

        # BoxLayout (box4) for properties
        property_box1 = MDBoxLayout()
        property_label = MDCard(md_bg_color=rgba(
            "#028A0F"), size_hint=(None, None), height=40, width=165)
        property_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   PROPERTIES:[/b][/color][/size]", markup=True, halign="left"))

        property_box2 = MDBoxLayout()
        property = MDList()

        property_box1.adaptive_height = 40
        property_box2.adaptive_height = property.adaptive_height
        property_box1.add_widget(property_label)
        property_box2.add_widget(property)

        # BoxLayout (box5) for atomic properties
        atomic_box1 = MDBoxLayout()
        atomic_label = MDCard(md_bg_color=rgba(
            "#FF1694"), size_hint=(None, None), height=40, width=250)
        atomic_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   ATOMIC PROPERTIES:[/b][/color][/size]", markup=True, halign="left"))

        atomic_box2 = MDBoxLayout()
        atomic = MDList()

        atomic_box1.adaptive_height = 40
        atomic_box2.adaptive_height = atomic.adaptive_height
        atomic_box1.add_widget(atomic_label)
        atomic_box2.add_widget(atomic)

        # Adding widgets to the Outer BoxLayout
        OuterBox.add_widget(card1)
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(overview_box1)
        OuterBox.add_widget(overview_box2)
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(box2)
        OuterBox.add_widget(box3)
        OuterBox.add_widget(MDSeparator(color=(0, 0, 0, 0)))
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(img_box1)
        OuterBox.add_widget(img_box2)
        OuterBox.add_widget(property_box1)
        OuterBox.add_widget(property_box2)
        OuterBox.add_widget(atomic_box1)
        OuterBox.add_widget(atomic_box2)

        # Adding widgets to the Main ScrollLayout
        OuterMostBox.add_widget(TopBar0)
        OuterMostBox.add_widget(MainBox)

        # Adding widgets to the Main ScrollLayout
        MainBox.add_widget(scroll)
        scroll.add_widget(OuterBox)

        # Adding everything to MDScreen
        self.add_widget(OuterMostBox)

    def change1(self, *args):
        overview.clear_widgets()
        property.clear_widgets()
        atomic.clear_widgets()

        self.manager.current = "Screen 1"


class MyScreenManager(MDScreenManager):
    home_screen = ObjectProperty(None)
    element_screen = ObjectProperty(None)
    element_screen_1 = ObjectProperty(None)
    search_screen = ObjectProperty(None)


class PeriodicTable(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global screen_manager

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.material_style = "M3"
        # self.device_orientation = "Vertical"

        screen_manager = MyScreenManager(transition=MDFadeSlideTransition())
        screen_manager.home_screen = HomeScreen(name="Screen 1")
        screen_manager.element_screen = Element_Description(name="Screen 2")
        screen_manager.element_screen_1 = Element_Description_1(
            name="Screen 4")
        screen_manager.search_screen = Search_Description(name="Screen 3")

        screen_manager.add_widget(screen_manager.home_screen)
        screen_manager.add_widget(screen_manager.search_screen)
        screen_manager.add_widget(screen_manager.element_screen)
        screen_manager.add_widget(screen_manager.element_screen_1)

    def build(self):
        self.title = "Periodic Table"
        self.icon = "assets/image/icon.png"
        return screen_manager


class Elements_Portion(MDScreen):
    scroll = MDScrollView()
    scroll.size = scroll.size
    layout1 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, "*", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, "*", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    layout2 = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

    store = JsonStore("assets/data/elements.json")
    data = store.get("data")["elements"]
    no = 0
    new_no = 56
    period = 1

    box1 = ["57-71", "89-103"]
    box2 = ["La-Lu", "Ac-Lr"]
    box_no = 0

    def __init__(self, *args, **kwargs):
        super(Elements_Portion, self).__init__(*args, **kwargs)

        self.grid = MDGridLayout(rows=11, cols=19, padding=9,
                        spacing=9, size_hint_y=None, size_hint_x=None, adaptive_size=True)
        
        b = MDLabel(text="", size_hint=(None, None), size=("24dp", "24dp"))
        self.grid.add_widget(b)

        for i in range(18):
            self.grid.add_widget(MDLabel(text=f"[size=15sp][color=FFFFFF][b]{i + 1}[/b][/color][/size]", markup=True,
                                         size_hint=(None, None), size=(
                                             "80dp", "24dp"), halign="center", valign="center", line_color=(.42, .47, .53, 1)))

        for i in self.layout1:
            self.grid.add_widget(
                MDLabel(text=f"[size=15sp][color=FFFFFF][b]{self.period}[/b][/color][/size]", markup=True, size_hint=(
                    None, None), size=("24dp", "80dp"), halign="center", valign="middle",
                    line_color=(.42, .47, .53, 1)))

            for j in i:
                if j == 1:
                    a = MDRectangleFlatButton(text=self.data[self.no]["symbol"], font_size=40, font_name="assets/fonts/arlrdbd.ttf",
                                              size_hint=(
                                                  1, 1), text_color=rgba(self.data[self.no]["cpk-hex"]),
                                              line_color=rgba(
                                                  self.data[self.no]["cpk-hex"]),
                                              line_width=1)
                    a.bind(on_release=self.change2)
                    self.grid.add_widget(a)
                    self.no += 1
                elif j == "*":
                    self.no += 15
                    self.grid.add_widget(MDLabel(
                        text=f"[color=FFFFFF][size=22sp][b]{self.box1[self.box_no]}[/b]\n{self.box2[self.box_no]}[/size][/color]",
                        markup=True, font_name="assets/fonts/arlrdbd.ttf", size_hint=(None, None), size=("80dp", "80dp"),
                        halign="center", valign="middle"))
                    self.box_no += 1
                else:
                    self.grid.add_widget(
                        MDLabel(text="", size_hint=(None, None), size=("80dp", "80dp")))
            self.period += 1

        self.grid.add_widget(
            MDLabel(size_hint=(None, None), size=("24dp", "10dp")))
        for i in range(18):
            self.grid.add_widget(
                MDLabel(size_hint=(None, None), size=("80dp", "10dp")))

        for i in self.layout2:
            self.grid.add_widget(
                MDLabel(text=f"[size=15sp][color=FFFFFF][b]{self.period}[/b][/color][/size]", markup=True, size_hint=(
                    None, None), size=("24dp", "80dp"), halign="center", valign="middle",
                    line_color=(.42, .47, .53, 1)))
            self.period += 1
            for j in i:
                if j == 1:
                    a = MDRectangleFlatButton(text=self.data[self.new_no]["symbol"], font_size=40,
                                              font_name="assets/fonts/arlrdbd.ttf", size_hint=(
                        1, 1), text_color=rgba(self.data[self.new_no]["cpk-hex"]),
                        line_color=rgba(self.data[self.new_no]["cpk-hex"]),
                        line_width=1)
                    a.bind(on_release=self.change2)
                    self.grid.add_widget(a)
                    self.new_no += 1
                else:
                    self.grid.add_widget(
                        MDLabel(text="", size_hint=(None, None), size=("80dp", "80dp")))
            self.new_no += 17

        self.scroll.add_widget(self.grid)
        self.add_widget(self.scroll)

    def change2(self, btn_obj):
        i = StringProperty()
        i = SymbolToIndex(btn_obj.text)
        value = self.data[i]

        TopBar0.title = f"[font=assets/fonts/arlrdbd.ttf][size=35][b]{value['name']}[/b][/size][/font]"
        card1.line_color = rgba(value['cpk-hex'])
        label1.text = f"[b][size=26sp]  {value['name']}[/size]\n[size=60sp] {value['symbol']}[/size]  [size=20sp]{value['number']}[/size]\n[size=22sp]  {round(value['atomic_mass'], 3)}[/size][/b] [size=18sp](g/mol)[/size]"
        label2.text = f"[size=20sp][b][color={value['cpk-hex']}]{value['category'].upper()}[/color][/b][/size]"

        overview.add_widget(
            TwoLineListItem(text="[b]English Name:[/b]", secondary_text=f"{value['name']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview.add_widget(
            TwoLineListItem(text="[b]Year Discovered:[/b]", secondary_text=f"{value['YearDiscovered']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        overview.add_widget(TwoLineListItem(text="[b]Discovered By:[/b]", secondary_text=f"{value['discovered_by']}",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        overview.add_widget(
            TwoLineListItem(text="[b]Named By:[/b]", secondary_text=f"{value['named_by']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview.add_widget(
            TwoLineListItem(text="[b]CAS Number:[/b]", secondary_text=f"CAS{value['CAS Number']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview.add_widget(
            TwoLineListItem(text="[b]Electron Shells:[/b]", secondary_text=f"{ElectronShell(value['shells'])}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))

        e_val_label.text = f"[size=25sp][color=#D0312D][b]{value['number']}[/b][/color][/size]"
        p_val_label.text = f"[size=25sp][color=#FBB917][b]{value['number']}[/b][/color][/size]"
        n_val_label.text = f"[size=25sp][color=#3944BC][b]{round(value['atomic_mass']) - value['number']}[/b][/color][/size]"

        img.source = value["image"]["url"]
        img_lab.text = f"[b][size=25sp][color=#F8EEEC][font=assets/fonts/arlrdbd.ttf]{value['summary']}[/font][/color][/size][/b]"

        property.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Atomic Number:[/b][/color]", secondary_text=f"{value['number']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Weight (Atomic Mass):[/b][/color]",
                                            secondary_text=f"{round(value['atomic_mass'], 4)} (g/mol)",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Density:[/b][/color]",
                                            secondary_text=f"{value['density']} (g/cmÂ³)", secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                            _no_ripple_effect=True))
        property.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Phase:[/b][/color]", secondary_text=f"{value['phase']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Melting Point:[/b][/color]",
                                            secondary_text=f"{value['melt']} [color=#028A0F]K[/color]",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Boiling Point:[/b][/color]",
                                            secondary_text=f"{value['boil']} [color=#028A0F]K[/color]",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        property.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Period:[/b][/color]", secondary_text=f"{value['period']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Group:[/b][/color]", secondary_text=f"{value['group']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Block:[/b][/color]", secondary_text=f"{value['block']} - block",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))

        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Oxidation States:[/b][/color]",
                                          secondary_text=f"{value['OxidationStates']}", secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                          _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronic Configuration:[/b][/color]",
                                          secondary_text=f"{value['electron_configuration_semantic']}",
                                          secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                          divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Molar Heat:[/b][/color]", secondary_text=f"{value['molar_heat']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Bonding Type:[/b][/color]",
                                          secondary_text=f"{value['BondingType']}", secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                          _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electron Affinity:[/b][/color]",
                                          secondary_text=f"{value['electron_affinity']} (kJ/mol)",
                                          secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                          divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronegativity:[/b][/color]",
                                          secondary_text=f"{value['electronegativity_pauling']}",
                                          secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                          divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Radius:[/b][/color]",
                                          secondary_text=f"{value['AtomicRadius']} pm", secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                          _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Van Der Waals Radius :[/b][/color]",
                                          secondary_text=f"{value['VanDerWaalsRadius']} pm", secondary_text_color=(
                                              1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                          _no_ripple_effect=True))

        screen_manager.current = "Screen 2"


class description_content(MDGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = 5
        self.cols = 4
        self.padding = 10
        self.spacing = 10
        self.size_hint_y = None
        self.adaptive_height = True

        color = {"Alkaline Earth Metals": "#FFCAF5",
                 "Alkali Metals": "#FF0000",
                 "Actinide": "#FFC192",
                 "Lanthanide": "#87C1F2",
                 "Metalloid": "#FFFF7F",
                 "Post-Transition Metal": "#00FFFF",
                 "Halogen": "#997FBC",
                 "Transition Metal": "#EAA31A",
                 "Noble Gas": "#E5AAC1",
                 "Nonmetal": "#92FAA3"}

        for i in color:
            self.add_widget(MDCard(md_bg_color=rgba(
                color[i]), radius=15, size_hint=(None, None), size=("40dp", "40dp")))
            self.add_widget(
                MDLabel(text=f"[font=assets/fonts/arlrdbd.ttf][size=15sp]{i}[/size][/font]", markup=True))


class Dictionary(MDScreen):
    store = JsonStore("assets/data/dict.json")
    data = store.get("data")

    def __init__(self, *args, **kwargs):
        super(Dictionary, self).__init__(*args, **kwargs)
        scroll = MDScrollView()
        box0 = MDGridLayout(rows=2, cols=3,
                            padding=11, adaptive_height=True, spacing=15)

        # Electronic Configuration
        card1 = MDBoxLayout(orientation="vertical", md_bg_color=rgba(
            "#20242b"), line_color=rgba(
            "#FF006B"), size_hint=(1, None), height=450, line_width=2, radius=20, padding=15, width=500)
        head0 = MDLabel(
            text=f"[u][size=30sp][b]Electronic Configuration[/b][/size][/u]\n\n[size=17sp]{self.data['Electronic Configuration']}[/size]",
            markup=True, halign="center", valign="center")
        card1.add_widget(head0)

        # Electronegativity
        card2 = MDBoxLayout(orientation="vertical", md_bg_color=rgba(
            "#20242b"), line_color=rgba(
            "#00ABFF"), size_hint=(1, None), height=450, line_width=2, radius=20, padding=15)
        head1 = MDLabel(
            text=f"[u][size=30sp][b]Electronegativity[/b][/size][/u]\n\n[size=17sp]{self.data['Electronegativity']}[/size]",
            markup=True, halign="center", valign="center")
        card2.add_widget(head1)

        # Electronegativity
        card3 = MDBoxLayout(orientation="vertical", md_bg_color=rgba(
            "#20242b"), line_color=rgba(
            "#FFFF9C"), size_hint=(1, None), height=450, line_width=2, radius=20, padding=15)
        head2 = MDLabel(
            text=f"[u][size=30sp][b]Ionization  Potential[/b][/size][/u]\n\n[size=17sp]{self.data['ionization_energies']}[/size]",
            markup=True, halign="center", valign="center")
        card3.add_widget(head2)

        # standard_electrode_potential
        card4 = MDBoxLayout(orientation="vertical", md_bg_color=rgba(
            "#20242b"), line_color=rgba(
            "#00FFFF"), size_hint=(1, None), height=460, line_width=2, radius=20, padding=15)
        head3 = MDLabel(
            text=f"[u][size=30sp][b]Standard Electrode Potential[/b][/size][/u]\n\n[size=17sp]{self.data['standard_electrode_potential']}[/size]",
            markup=True, halign="center", valign="center")
        card4.add_widget(head3)

        box0.add_widget(card1)
        box0.add_widget(card2)
        box0.add_widget(card3)
        box0.add_widget(card4)
        scroll.add_widget(box0)
        self.add_widget(scroll)


def SymbolToIndex(symbol):
    store = JsonStore("assets/data/elements.json")
    data = store.get("data")["elements"]
    for i in data:
        if i["symbol"] == symbol:
            return data.index(i)


def NameToIndex(name):
    store = JsonStore("assets/data/elements.json")
    data = store.get("data")["elements"]
    for i in data:
        if i["name"] == name:
            return data.index(i)
    return 0

class Search(MDScreen):
    items = {" Name ": ["rename-box", "#E91E63"],
             "Symbol": ["alpha-b-box-outline", "#4FC3F7"],
             "Number": ["numeric-2-box-outline", "#FFEB3B"],
             " Year ": ["calendar-range-outline", "#86F86A"],
             "Weight": ["weight-kilogram", "#FF8A65"],
             "Density": ["table", "#FF46FF"],
             # "Conductivity": ["meter-electric-outline", "#1565C0"],
             "Electronegativity": ["electron-framework", "#008B00"],
             " CAS Number": ["numeric-8-box-multiple", "#A6000F"]}

    def __init__(self, *args, **kwargs):
        super(Search, self).__init__(*args, **kwargs)

        box0 = MDBoxLayout(orientation="vertical")

        box1 = MDBoxLayout(size_hint_x=1, md_bg_color=rgba("#202028"), size_hint=(.97, .2),
                           pos_hint={"top": .98, "center_x": .5}, line_width=2, line_color=rgba("#CE93D8"), radius=20)
        box1.add_widget(MDLabel(
            text="[color=#CE93D8][font=assets/fonts/arlrdbd.ttf][size=60sp][b]Search By Properties:[/b][/size][/font][/color]",
            markup=True, halign="center"))

        box2 = MDBoxLayout(size_hint_x=1, md_bg_color=rgba("#202028"), size_hint=(.97, .73),
                           pos_hint={"top": .75, "center_x": .5}, line_width=2, line_color=rgba("#CE93D8"), radius=20)
        scroll = MDScrollView()
        stack = MDStackLayout(orientation="lr-tb", spacing=20,
                              padding=20, adaptive_height=True)

        for i in self.items:
            button = MDRoundFlatIconButton(text=f"{i}", icon=f"{self.items[i][0]}", line_width=2,
                                           line_color=rgba(f"{self.items[i][1]}"), font_size=35,
                                           size_hint=(1 / 2, None),
                                           font_name="assets/fonts/arlrdbd.ttf", text_color=rgba(f"{self.items[i][1]}"),
                                           icon_color=rgba(f"{self.items[i][1]}"))
            button.bind(on_release=self.search_choice)
            stack.add_widget(button)

        scroll.add_widget(stack)
        box2.add_widget(scroll)

        # Adding elements to Search
        self.add_widget(box0)
        self.add_widget(box1)
        self.add_widget(box2)

    def search_choice(self, btn_obj):
        screen_manager.get_screen(
            "Screen 3").ids.search_top_bar.title = f"[font=assets/fonts/arlrdbd.ttf][size=35][b]Search By {btn_obj.text.strip()}[/b][/size][/font]"
        screen_manager.get_screen(
            "Screen 3").ids.field.hint_text = f" Search By {btn_obj.text.strip()}"
        screen_manager.current = "Screen 3"


class Search_Description(MDScreen):
    store = JsonStore("assets/data/elements.json")
    data = store.get("data")["elements"]
    names = [
        {"viewclass": "CustomListItem",
         'text1': f"[color=#FFFFFF][font=assets/fonts/arlrdbd.ttf][size=30sp][b]{j['name']}[/b][/size][/font][/color][color=#FFFFFF]",
         'text2': f"[color={j['cpk-hex']}][font=assets/fonts/arlrdbd.ttf][size=20sp][b]{round(j['atomic_mass'], 3)}[/size][size=18sp] (g/mol)[/size][/b][/font][/color]",
         'color_icon': f"{j['cpk-hex']}",
         'icon_text': f"[font=assets/fonts/arlrdbd.ttf][color=#050100][size=23sp][b]{j['symbol']}[/b][/size][/color][/font]"}
        for j in data]

    data_list = [
        {'Name': j['name'],
         'Weight': str(j['atomic_mass']),
         'Number': str(j['number']),
         'Symbol': j['symbol'],
         'Year': str(j['YearDiscovered']),
         'Density': str(j['density']),
         # 'Conductivity': j['number'],
         'Electronegativity': str(j['electronegativity_pauling']),
         'CAS Number': j['CAS Number'],
         } for j in data]

    def set_list_md_icons(self, text=""):
        def add_icon_item(text1, text2,color_icon,icon_text):
            self.ids.rv.data.append(
                {"viewclass": "CustomListItem",
                 'text1': text1,
                 'text2': text2,
                 'color_icon': color_icon,
                 'icon_text': icon_text}
            )

        search_category = (self.ids.search_top_bar.title)[53:-18].strip()
        self.ids.rv.data = []
        for element in self.names:
            if text.lower() in self.data_list[self.names.index(element)][search_category].lower():
                add_icon_item(element['text1'], element['text2'], element['color_icon'], element['icon_text'])

    def change2(self):
        self.manager.current = "Screen 1"


class Element_Description_1(MDScreen):

    def __init__(self, *args, **kwargs):
        global TopBar0_1, label1_1, label2_1, card1_1, overview_1, e_val_label_1, p_val_label_1, n_val_label_1, img_1, img_lab_1, property_1, atomic_1
        super(Element_Description_1, self).__init__(*args, **kwargs)

        # OuterMost box
        OuterMostBox = MDBoxLayout(orientation="vertical")

        # Header or TopAppBar
        TopBar0_1 = MDTopAppBar(left_action_items=[
            ["arrow-left", lambda x: self.change1()]], md_bg_color=rgba("#630436"))

        # main box Layout
        MainBox = MDBoxLayout(orientation="vertical", padding=8,
                              spacing=8)

        # Main Scroll View
        scroll = MDScrollView()

        # Creating Outer BoxLayout
        OuterBox = MDBoxLayout(orientation="vertical",
                               spacing=8, adaptive_height=True)

        # 1st MDCard
        card1_1 = MDCard(md_bg_color=rgba(
            "#20242b"), style="elevated", size_hint=(1, None), height="150dp")
        # 1 label and 1 BoxLayout in MDcard
        label1_1 = MDLabel(markup=True, halign="left")
        box1 = MDBoxLayout(orientation="vertical")

        # 2 Labels in BoxLayout present in MDCard
        label2_1 = MDLabel(markup=True, halign="center", valign="bottom")
        box1.add_widget(MDLabel(text=""))  # 2nd Label
        box1.add_widget(label2_1)
        card1_1.add_widget(label1_1)
        card1_1.add_widget(box1)

        # Overview of the Element
        # Overview List Item
        overview_box1 = MDBoxLayout()
        overview_label = MDCard(md_bg_color=rgba(
            "#A91B0D"), size_hint=(None, None), height=40, width=145)
        overview_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   OVERVIEW:[/b][/color][/size]", markup=True, halign="left"))

        overview_box2 = MDBoxLayout()
        overview_1 = MDList()
        overview_box1.adaptive_height = 40
        overview_box2.adaptive_height = overview_1.adaptive_height
        overview_box1.add_widget(overview_label)
        overview_box2.add_widget(overview_1)

        # BoxLayout(box2) for Electrons, Protons And Neutrons
        box2 = MDBoxLayout(orientation="horizontal", spacing=6)
        box3 = MDBoxLayout(orientation="horizontal", spacing=6)

        electron = MDCard(md_bg_color=rgba(
            "#D0312D"), size_hint=(1, None), height=50)
        electron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]ELECTRONS:[/b][/color][/size]", markup=True, halign="center")
        electron.add_widget(electron_label)
        e_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("D0312D"), size_hint=(1, None), height=50)
        e_val_label_1 = MDLabel(markup=True, halign="center", line_width=5)
        e_val.add_widget(e_val_label_1)

        proton = MDCard(md_bg_color=rgba(
            "#FBB917"), size_hint=(1, None), height=50)
        proton_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]PROTONS:[/b][/color][/size]", markup=True, halign="center")
        proton.add_widget(proton_label)
        p_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("FBB917"), size_hint=(1, None), height=50)
        p_val_label_1 = MDLabel(markup=True, halign="center", line_width=5)
        p_val.add_widget(p_val_label_1)

        neutron = MDCard(md_bg_color=rgba(
            "#3944BC"), size_hint=(1, None), height=50)
        neutron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]NEUTRONS:[/b][/color][/size]", markup=True, halign="center")
        neutron.add_widget(neutron_label)
        n_val = MDCard(md_bg_color=rgba(
            "#20242B"), line_color=rgba("3944BC"), size_hint=(1, None), height=50)
        n_val_label_1 = MDLabel(markup=True, halign="center", line_width=5)
        n_val.add_widget(n_val_label_1)

        box2.adaptive_height = 50
        box3.adaptive_height = 50
        box2.add_widget(electron)
        box2.add_widget(proton)
        box2.add_widget(neutron)
        box3.add_widget(e_val)
        box3.add_widget(p_val)
        box3.add_widget(n_val)

        # BoxLayout (box_img) for image
        img_box1 = MDBoxLayout()
        img_label = MDCard(md_bg_color=rgba(
            "#000080"), size_hint=(None, None), height=40, width=110)
        img_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   IMAGE:[/b][/color][/size]", markup=True, halign="left"))

        img_box2 = MDBoxLayout(
            pos_hint={"center_x": 0.5}, spacing=25, padding=25)
        img_1 = AsyncImage(size_hint=(None, None), height=300, width=300)
        img_lab_1 = MDLabel(markup=True)

        img_box1.adaptive_height = 40
        img_box2.adaptive_height = img_1.height
        img_box1.add_widget(img_label)
        img_box2.add_widget(img_1)
        img_box2.add_widget(img_lab_1)

        # BoxLayout (box4) for properties
        property_box1 = MDBoxLayout()
        property_label = MDCard(md_bg_color=rgba(
            "#028A0F"), size_hint=(None, None), height=40, width=165)
        property_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   PROPERTIES:[/b][/color][/size]", markup=True, halign="left"))

        property_box2 = MDBoxLayout()
        property_1 = MDList()

        property_box1.adaptive_height = 40
        property_box2.adaptive_height = property_1.adaptive_height
        property_box1.add_widget(property_label)
        property_box2.add_widget(property_1)

        # BoxLayout (box5) for atomic properties
        atomic_box1 = MDBoxLayout()
        atomic_label = MDCard(md_bg_color=rgba(
            "#FF1694"), size_hint=(None, None), height=40, width=250)
        atomic_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   ATOMIC PROPERTIES:[/b][/color][/size]", markup=True, halign="left"))

        atomic_box2 = MDBoxLayout()
        atomic_1 = MDList()

        atomic_box1.adaptive_height = 40
        atomic_box2.adaptive_height = atomic_1.adaptive_height
        atomic_box1.add_widget(atomic_label)
        atomic_box2.add_widget(atomic_1)

        # Adding widgets to the Outer BoxLayout
        OuterBox.add_widget(card1_1)
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(overview_box1)
        OuterBox.add_widget(overview_box2)
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(box2)
        OuterBox.add_widget(box3)
        OuterBox.add_widget(MDSeparator(color=(0, 0, 0, 0)))
        OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(img_box1)
        OuterBox.add_widget(img_box2)
        OuterBox.add_widget(property_box1)
        OuterBox.add_widget(property_box2)
        OuterBox.add_widget(atomic_box1)
        OuterBox.add_widget(atomic_box2)

        # Adding widgets to the Main ScrollLayout
        OuterMostBox.add_widget(TopBar0_1)
        OuterMostBox.add_widget(MainBox)

        # Adding widgets to the Main ScrollLayout
        MainBox.add_widget(scroll)
        scroll.add_widget(OuterBox)

        # Adding everything to MDScreen
        self.add_widget(OuterMostBox)

    def change1(self, *args):
        overview_1.clear_widgets()
        property_1.clear_widgets()
        atomic_1.clear_widgets()

        self.manager.current = "Screen 3"


class CustomListItem(TwoLineAvatarListItem):
    text1 = StringProperty()
    text2 = StringProperty()
    color_icon = StringProperty()
    icon_text = StringProperty()

    store = JsonStore("assets/data/elements.json")
    data = store.get("data")["elements"]

    def playboy(self, instance):
        start = instance.text.find('[b]') + 3  # +3 to skip '[b]'
        end = instance.text.find('[/b]')
        name = instance.text[start:end]
        index = StringProperty()
        index = NameToIndex(name)
        value = self.data[index]

        TopBar0_1.title = f"[font=assets/fonts/arlrdbd.ttf][size=35][b]{value['name']}[/b][/size][/font]"
        card1_1.line_color = rgba(value['cpk-hex'])
        label1_1.text = f"[b][size=26sp]  {value['name']}[/size]\n[size=60sp] {value['symbol']}[/size]  [size=20sp]{value['number']}[/size]\n[size=22sp]  {round(value['atomic_mass'], 3)}[/size][/b] [size=18sp](g/mol)[/size]"
        label2_1.text = f"[size=20sp][b][color={value['cpk-hex']}]{value['category'].upper()}[/color][/b][/size]"

        overview_1.add_widget(
            TwoLineListItem(text="[b]English Name:[/b]", secondary_text=f"{value['name']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview_1.add_widget(
            TwoLineListItem(text="[b]Year Discovered:[/b]", secondary_text=f"{value['YearDiscovered']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        overview_1.add_widget(TwoLineListItem(text="[b]Discovered By:[/b]", secondary_text=f"{value['discovered_by']}",
                                              secondary_text_color=(
                                                  1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                              divider="Inset", _no_ripple_effect=True))
        overview_1.add_widget(
            TwoLineListItem(text="[b]Named By:[/b]", secondary_text=f"{value['named_by']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview_1.add_widget(
            TwoLineListItem(text="[b]CAS Number:[/b]", secondary_text=f"CAS{value['CAS Number']}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))
        overview_1.add_widget(
            TwoLineListItem(text="[b]Electron Shells:[/b]", secondary_text=f"{ElectronShell(value['shells'])}", secondary_text_color=(
                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                _no_ripple_effect=True))

        e_val_label_1.text = f"[size=25sp][color=#D0312D][b]{value['number']}[/b][/color][/size]"
        p_val_label_1.text = f"[size=25sp][color=#FBB917][b]{value['number']}[/b][/color][/size]"
        n_val_label_1.text = f"[size=25sp][color=#3944BC][b]{round(value['atomic_mass']) - value['number']}[/b][/color][/size]"

        img_1.source = value["image"]["url"]
        img_lab_1.text = f"[b][size=25sp][color=#F8EEEC][font=assets/fonts/arlrdbd.ttf]{value['summary']}[/font][/color][/size][/b]"

        property_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Atomic Number:[/b][/color]", secondary_text=f"{value['number']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Weight (Atomic Mass):[/b][/color]",
                                              secondary_text=f"{round(value['atomic_mass'], 4)} (g/mol)",
                                              secondary_text_color=(
                                                  1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                              divider="Inset", _no_ripple_effect=True))
        property_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Density:[/b][/color]",
                                              secondary_text=f"{value['density']} (g/cmÂ³)", secondary_text_color=(
                                                  1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                              _no_ripple_effect=True))
        property_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Phase:[/b][/color]", secondary_text=f"{value['phase']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Melting Point:[/b][/color]",
                                              secondary_text=f"{value['melt']} [color=#028A0F]K[/color]",
                                              secondary_text_color=(
                                                  1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                              divider="Inset", _no_ripple_effect=True))
        property_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Boiling Point:[/b][/color]",
                                              secondary_text=f"{value['boil']} [color=#028A0F]K[/color]",
                                              secondary_text_color=(
                                                  1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                              divider="Inset", _no_ripple_effect=True))
        property_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Period:[/b][/color]", secondary_text=f"{value['period']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Group:[/b][/color]", secondary_text=f"{value['group']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        property_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Block:[/b][/color]", secondary_text=f"{value['block']} - block",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))

        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Oxidation States:[/b][/color]",
                                            secondary_text=f"{value['OxidationStates']}", secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                            _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronic Configuration:[/b][/color]",
                                            secondary_text=f"{value['electron_configuration_semantic']}",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        atomic_1.add_widget(
            TwoLineListItem(text="[color=#FFFFFF][b]Molar Heat:[/b][/color]", secondary_text=f"{value['molar_heat']}",
                            secondary_text_color=(
                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                            _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Bonding Type:[/b][/color]",
                                            secondary_text=f"{value['BondingType']}", secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                            _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electron Affinity:[/b][/color]",
                                            secondary_text=f"{value['electron_affinity']} (kJ/mol)",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronegativity:[/b][/color]",
                                            secondary_text=f"{value['electronegativity_pauling']}",
                                            secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5,
                                            divider="Inset", _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Radius:[/b][/color]",
                                            secondary_text=f"{value['AtomicRadius']} pm", secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                            _no_ripple_effect=True))
        atomic_1.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Van Der Waals Radius :[/b][/color]",
                                            secondary_text=f"{value['VanDerWaalsRadius']} pm", secondary_text_color=(
                                                1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset",
                                            _no_ripple_effect=True))

        screen_manager.current = "Screen 4"


def ElectronShell(list_):
    shells = ['K','L','M','N','O','P','Q','R']
    str_shell=""
    for i in range(len(list_)):
        str_shell += shells[i]
        str_shell += str(list_[i])
        str_shell += " "
    return str_shell


class LabelLeftWidget(ILeftBody, MDLabel):
    pass


if __name__ == '__main__':
    Window.maximize()
    PeriodicTable().run()
