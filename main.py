from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition import MDFadeSlideTransition
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList, TwoLineListItem


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        box = MDBoxLayout(orientation="vertical")

        # TopAppBar
        TopBar = MDTopAppBar(title="[font=ARLRDBD.TTF][size=35][b]Periodic Table[/b][/size][/font]",
                             type_height="large", right_action_items=[["sort-variant", lambda x: self.show0()]])

        # BottomAppBar
        BottomBar = MDBottomNavigation(panel_color=get_color_from_hex(
            "#663AB7"), text_color_active=get_color_from_hex("#FFC7F6"))

        home_nav_item = MDBottomNavigationItem(
            name='Element_screen', text='Periodic Table', icon='periodic-table')
        home_nav_item.add_widget(Elements_Portion())
        BottomBar.add_widget(home_nav_item)

        dict_nav_item = MDBottomNavigationItem(
            name='Dictionary', text='Dictionary', icon='table')
        dict_nav_item.add_widget(Dictionary())
        BottomBar.add_widget(dict_nav_item)

        desc_nav_item = MDBottomNavigationItem(
            name='Description', text='Description', icon='widgets')
        BottomBar.add_widget(desc_nav_item)

        # Add text_color_normal after adding all the items
        BottomBar.text_color_normal = get_color_from_hex("#3A1B2F")

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

    def change0(self, *args):
        self.manager.current = "Screen 2"


class Element_Description(MDScreen):

    def __init__(self, *args, **kwargs):
        global TopBar0, label1, label2, card1, overview, e_val_label, p_val_label, n_val_label, property, atomic
        super(Element_Description, self).__init__(*args, **kwargs)

        # OuterMost box
        OuterMostBox = MDBoxLayout(orientation="vertical")

        # Header or TopAppBar
        TopBar0 = MDTopAppBar(type_height="large", left_action_items=[
                              ["arrow-left", lambda x: self.change1()]])

        # main box Layout
        MainBox = MDBoxLayout(orientation="vertical", padding=8,
                              spacing=8)

        # Main Scroll View
        scroll = MDScrollView()

        # Creating Outer BoxLayout
        OuterBox = MDBoxLayout(orientation="vertical",
                               spacing=8, adaptive_height=True)

        # 1st MDCard
        card1 = MDCard(md_bg_color=get_color_from_hex(
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
        overview_label = MDCard(md_bg_color=get_color_from_hex(
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

        electron = MDCard(md_bg_color=get_color_from_hex(
            "#D0312D"), size_hint=(1, None), height=50)
        electron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]ELECTRONS:[/b][/color][/size]", markup=True, halign="center")
        electron.add_widget(electron_label)
        e_val = MDCard(md_bg_color=get_color_from_hex(
            "#20242B"), line_color=get_color_from_hex("#D0312D"), size_hint=(1, None), height=50)
        e_val_label = MDLabel(markup=True, halign="center", line_width=5)
        e_val.add_widget(e_val_label)

        proton = MDCard(md_bg_color=get_color_from_hex(
            "#FBB917"), size_hint=(1, None), height=50)
        proton_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]PROTONS:[/b][/color][/size]", markup=True, halign="center")
        proton.add_widget(proton_label)
        p_val = MDCard(md_bg_color=get_color_from_hex(
            "#20242B"), line_color=get_color_from_hex("#FBB917"), size_hint=(1, None), height=50)
        p_val_label = MDLabel(markup=True, halign="center", line_width=5)
        p_val.add_widget(p_val_label)

        neutron = MDCard(md_bg_color=get_color_from_hex(
            "#3944BC"), size_hint=(1, None), height=50)
        neutron_label = MDLabel(
            text="[size=18sp][color=#FFFFFF][b]NEUTRONS:[/b][/color][/size]", markup=True, halign="center")
        neutron.add_widget(neutron_label)
        n_val = MDCard(md_bg_color=get_color_from_hex(
            "#20242B"), line_color=get_color_from_hex("#3944BC"), size_hint=(1, None), height=50)
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

        '''# BoxLayout(Box3) for note of that element
        note_box1 = MDBoxLayout()
        note_label = MDCard(md_bg_color=get_color_from_hex(
            "#2832C2"), size_hint=(None, None), height=40, width=90)
        note_label.add_widget(MDLabel(
            text="[size=22sp][color=#FFFFFF][b]   NOTE:[/b][/color][/size]", markup=True, halign="left"))

        note_box2 = MDBoxLayout()
        note = MDLabel(markup=True)

        note_box1.adaptive_height = 40
        note_box2.adaptive_height = note.height
        note_box1.add_widget(note_label)
        note_box2.add_widget(note)'''

        # BoxLayout (box4) for properties
        property_box1 = MDBoxLayout()
        property_label = MDCard(md_bg_color=get_color_from_hex(
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
        atomic_label = MDCard(md_bg_color=get_color_from_hex(
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
        '''OuterBox.add_widget(MDSeparator())
        OuterBox.add_widget(note_box1)
        OuterBox.add_widget(MDSeparator(color=(0, 0, 0, 0)))
        OuterBox.add_widget(note_box2)'''
        OuterBox.add_widget(MDSeparator(color=(0, 0, 0, 0)))
        OuterBox.add_widget(MDSeparator())
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


class PeriodicTable(MDApp):
    def build(self):
        global screen_manager

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.material_style = "M2"
        self.device_orientation = "Vertical"

        screen_manager = MyScreenManager(transition=MDFadeSlideTransition())
        screen_manager.home_screen = HomeScreen(name="Screen 1")
        screen_manager.element_screen = Element_Description(name="Screen 2")
        screen_manager.add_widget(screen_manager.home_screen)
        screen_manager.add_widget(screen_manager.element_screen)
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

    store = JsonStore("elements.json")
    data = store.get("data")["elements"]
    no = 0
    new_no = 56
    period = 1

    box1 = ["57-71", "89-103"]
    box2 = ["La-Lu", "Ac-Lr"]
    box_no = 0

    Element = MDGridLayout(rows=11, cols=19, padding=9,
                           spacing=9, size_hint_y=None, size_hint_x=None, adaptive_size=True)

    def __init__(self, *args, **kwargs):
        super(Elements_Portion, self).__init__(*args, **kwargs)

        b = MDLabel(text="", size_hint=(None, None), size=("24dp", "24dp"))
        self.Element.add_widget(b)

        for i in range(18):
            self.Element.add_widget(MDLabel(text=f"[size=15sp][color=FFFFFF][b]{i+1}[/b][/color][/size]", markup=True, size_hint=(None, None), size=(
                "80dp", "24dp"), halign="center", valign="center", line_color=(.42, .47, .53, 1)))  # theme_text_color = "Custom", text_color=(1,1,1,1), font_size=30,

        for i in self.layout1:
            self.Element.add_widget(MDLabel(text=f"[size=15sp][color=FFFFFF][b]{self.period}[/b][/color][/size]", markup=True, size_hint=(
                None, None), size=("24dp", "80dp"), halign="center", valign="middle", line_color=(.42, .47, .53, 1)))

            for j in i:
                if j == 1:
                    a = MDRectangleFlatButton(text=self.data[self.no]["symbol"], font_size=40, font_name="ARLRDBD.TTF", size_hint=(
                        1, 1), text_color=get_color_from_hex(self.data[self.no]["cpk-hex"]),
                        line_color=get_color_from_hex(self.data[self.no]["cpk-hex"]), line_width=1)
                    a.bind(on_release=self.change2)
                    self.Element.add_widget(a)
                    self.no += 1
                elif j == "*":
                    self.no += 15
                    self.Element.add_widget(MDLabel(text=f"[color=FFFFFF][size=22sp][b]{self.box1[self.box_no]}[/b]\n{self.box2[self.box_no]}[/size][/color]",
                                            markup=True, font_name="ARLRDBD.TTF", size_hint=(None, None), size=("80dp", "80dp"), halign="center", valign="middle"))
                    self.box_no += 1
                else:
                    self.Element.add_widget(
                        MDLabel(text="", size_hint=(None, None), size=("80dp", "80dp")))
            self.period += 1

        self.Element.add_widget(
            MDLabel(size_hint=(None, None), size=("24dp", "10dp")))
        for i in range(18):
            self.Element.add_widget(
                MDLabel(size_hint=(None, None), size=("80dp", "10dp")))

        for i in self.layout2:
            self.Element.add_widget(MDLabel(text=f"[size=15sp][color=FFFFFF][b]{self.period}[/b][/color][/size]", markup=True, size_hint=(
                None, None), size=("24dp", "80dp"), halign="center", valign="middle", line_color=(.42, .47, .53, 1)))
            self.period += 1
            for j in i:
                if j == 1:
                    a = MDRectangleFlatButton(text=self.data[self.new_no]["symbol"], font_size=40, font_name="ARLRDBD.TTF", size_hint=(
                        1, 1), text_color=get_color_from_hex(self.data[self.new_no]["cpk-hex"]), line_color=get_color_from_hex(self.data[self.new_no]["cpk-hex"]), line_width=1)
                    a.bind(on_release=self.change2)
                    self.Element.add_widget(a)
                    self.new_no += 1
                else:
                    self.Element.add_widget(
                        MDLabel(text="", size_hint=(None, None), size=("80dp", "80dp")))
            self.new_no += 17

        self.scroll.add_widget(self.Element)
        self.add_widget(self.scroll)

    def change2(self, btn_obj):
        i = StringProperty()
        i = SymbolToIndex(btn_obj.text)
        element = self.data[i]

        TopBar0.title = f"[font=ARLRDBD.TTF][size=35][b]{element['name']}[/b][/size][/font]"
        card1.line_color = get_color_from_hex(element['cpk-hex'])
        label1.text = f"[b][size=26sp]  {element['name']}[/size]\n[size=60sp] {element['symbol']}[/size]  [size=20sp]{element['number']}[/size]\n[size=22sp]  {round(element['atomic_mass'],3)}[/size][/b] [size=18sp](g/mol)[/size]"
        label2.text = f"[size=20sp][b][color={element['cpk-hex']}]{element['category'].upper()}[/color][/b][/size]"

        overview.add_widget(TwoLineListItem(text="[b]English Name:[/b]", secondary_text=f"{element['name']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        overview.add_widget(TwoLineListItem(text="[b]Year Discovered:[/b]", secondary_text=f"{element['YearDiscovered']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        overview.add_widget(TwoLineListItem(text="[b]Discovered By:[/b]", secondary_text=f"{element['discovered_by']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        overview.add_widget(TwoLineListItem(text="[b]Named By:[/b]", secondary_text=f"{element['named_by']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))

        e_val_label.text = f"[size=25sp][color=#D0312D][b]{element['number']}[/b][/color][/size]"
        p_val_label.text = f"[size=25sp][color=#FBB917][b]{element['number']}[/b][/color][/size]"
        n_val_label.text = f"[size=25sp][color=#3944BC][b]{round(element['atomic_mass'])-element['number']}[/b][/color][/size]"

        '''note.text = f"[size=15sp][color=#FFFFFF][b]{element['summary']}[/b][/color][/size]"
        note_box2.adaptive_height = note.adaptive_height'''

        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Number:[/b][/color]", secondary_text=f"{element['number']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Weight (Atomic Mass):[/b][/color]", secondary_text=f"{round(element['atomic_mass'],4)} (g/mol)", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Density:[/b][/color]", secondary_text=f"{element['density']} (g/cm³)", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Phase:[/b][/color]", secondary_text=f"{element['phase']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Melting Point:[/b][/color]", secondary_text=f"{element['melt']} [color=#028A0F]K[/color]", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Boiling Point:[/b][/color]", secondary_text=f"{element['boil']} [color=#028A0F]K[/color]", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Period:[/b][/color]", secondary_text=f"{element['period']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Group:[/b][/color]", secondary_text=f"{element['group']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        property.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Block:[/b][/color]", secondary_text=f"{element['block']} - block", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))

        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Oxidation States:[/b][/color]", secondary_text=f"{element['OxidationStates']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronic Configuration:[/b][/color]", secondary_text=f"{element['electron_configuration_semantic']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Molar Heat:[/b][/color]", secondary_text=f"{element['molar_heat']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Bonding Type:[/b][/color]", secondary_text=f"{element['BondingType']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electron Affinity:[/b][/color]", secondary_text=f"{element['electron_affinity']} (kJ/mol)", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Electronegativity:[/b][/color]", secondary_text=f"{element['electronegativity_pauling']}", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Atomic Radius:[/b][/color]", secondary_text=f"{element['AtomicRadius']} pm", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))
        atomic.add_widget(TwoLineListItem(text="[color=#FFFFFF][b]Van Der Waals Radius :[/b][/color]", secondary_text=f"{element['VanDerWaalsRadius']} pm", secondary_text_color=(
            1, 1, 1, 1), font_style="H6", secondary_font_style="H6", radius=5, divider="Inset", _no_ripple_effect=True))

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
            self.add_widget(MDCard(md_bg_color=get_color_from_hex(
                color[i]), radius=15, size_hint=(None, None), size=("40dp", "40dp")))
            self.add_widget(
                MDLabel(text=f"[size=11sp][b]{i}[/b][/size]", markup=True))


class Dictionary(MDScreen):

    store = JsonStore("dict.json")
    data = store.get("data")

    def __init__(self, *args, **kwargs):
        super(Dictionary, self).__init__(*args, **kwargs)
        scroll = MDScrollView()
        box0 = MDBoxLayout(orientation="vertical",
                           padding=11, adaptive_height=True, spacing=15)

        # Electronic Configuration
        card1 = MDCard(orientation="vertical", md_bg_color=get_color_from_hex(
            "#20242b"), line_color=get_color_from_hex(
            "#FF006B"), style="elevated", size_hint=(1, None), height="490dp", line_width=2, radius=20, padding=15)
        head0 = MDLabel(
            text=f"[u][size=30sp][b]Electronic Configuration[/b][/size][/u]\n\n[size=15sp]{self.data['Electronic Configuration']}[/size]", markup=True, halign="center", valign="center")
        card1.add_widget(head0)

        # Electronegativity
        card2 = MDCard(orientation="vertical", md_bg_color=get_color_from_hex(
            "#20242b"), line_color=get_color_from_hex(
            "#00ABFF"), style="elevated", size_hint=(1, None), height="505dp", line_width=2, radius=20, padding=15)
        head1 = MDLabel(
            text=f"[u][size=30sp][b]Electronegativity[/b][/size][/u]\n\n[size=15sp]{self.data['Electronegativity']}[/size]", markup=True, halign="center", valign="center")
        card2.add_widget(head1)

        # Electronegativity
        card3 = MDCard(orientation="vertical", md_bg_color=get_color_from_hex(
            "#20242b"), line_color=get_color_from_hex(
            "#FFFF9C"), style="elevated", size_hint=(1, None), height="525dp", line_width=2, radius=20, padding=15)
        head2 = MDLabel(
            text=f"[u][size=30sp][b]Ionization  Potential[/b][/size][/u]\n\n[size=15sp]{self.data['ionization_energies']}[/size]", markup=True, halign="center", valign="center")
        card3.add_widget(head2)

        # standard_electrode_potential
        card4 = MDCard(orientation="vertical", md_bg_color=get_color_from_hex(
            "#20242b"), line_color=get_color_from_hex(
            "#00FFFF"), style="elevated", size_hint=(1, None), height="595dp", line_width=2, radius=20, padding=15)
        head3 = MDLabel(
            text=f"[u][size=30sp][b]Standard Electrode Potential[/b][/size][/u]\n\n[size=15sp]{self.data['standard_electrode_potential']}[/size]", markup=True, halign="center", valign="center")
        card4.add_widget(head3)

        box0.add_widget(card1)
        box0.add_widget(card2)
        box0.add_widget(card3)
        box0.add_widget(card4)
        scroll.add_widget(box0)
        self.add_widget(scroll)


def SymbolToIndex(symbol):
    store = JsonStore("elements.json")
    data = store.get("data")["elements"]
    for i in data:
        if i["symbol"] == symbol:
            return data.index(i)


if __name__ == '__main__':
    Window.size = (380, 800)
    PeriodicTable().run()
