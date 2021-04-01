import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from scraper import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
import pickle
from kivymd.uix.button import MDIconButton

my_dict = {}
KV = """
Screen:

    NavigationLayout:

        ScreenManager:
        
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "CovidApp"
                        elevation: 5
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    GridLayout:
                        rows: 5

                        MDLabel:
                            id: mdlab
                            padding_y:30
                            text:"Welcome to Covid Application"
                            font_style: "H4"
                            color: "white"
                            size_hint_y: None
                            height: self.texture_size[1]
                            text_size: self.width, None
                            halign:"center"

                        MDTextField:
                            id: mdtext
                            hint_text:"Search a state to see Covid stats for it"
                            mode: "rectangle"
                            halign:"center"

                        MDRaisedButton:
                            id: mdbu
                            text:"Search"
                            on_press: app.search_press()
                            size_hint_x:0.2

                        FloatLayout:
                            id : icon 
                            
                            MDLabel:
                                id : prefer
                                color:"white"
                                pos_hint : {"center_x":0.85,"center_y":0.5}
                                text:""


                        MDLabel:
                            id: info
                            text:"\\n\\n\\n\\n\\n\\n\\n\\n\\n"

                            font_style: "H6"
                            padding_y:30
                            padding_x:250
                            color: "white"
                            size_hint_y:None
                            height: self.texture_size[1]
                            text_size: self.width, None      
                            pos_hint: {"center_y":0.3}

        MDNavigationDrawer:
            id: nav_drawer
            

            BoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                color:"white"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "data/logo/kivy-icon-256.png"

                MDLabel:
                    text: "CovidApp App 0.1"
                    color: "white"
                    font_style: "Button"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "gabriele.sarti1@studenti.unimi.it"
                    color: "white"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:

                    MDList:
                        OneLineAvatarListItem:
                            text: "Login"

                            IconLeftWidget:
                                icon: "login"
                                on_press:

                        OneLineAvatarListItem:
                            text: "Info App"
                            on_press: app.show_app_info_dialog()

                            IconLeftWidget:
                                icon: "information-outline"
                        
                        OneLineAvatarListItem:
                            text: "Contact"
                            on_press: app.show_contact_dialog()

                            IconLeftWidget:
                                icon: "contact-mail-outline"

                                            
"""

#added a class
class MainApp(MDApp):

    info_dialog = None
    contact_dialog = None

    def build(self):
        self.title = "Covid Application"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def scraping(self):
        new_text= scraper(self.root.ids["mdtext"].text)
        self.root.ids["info"].text = new_text

    def create_Button(self,value):
        button = MDIconButton()
        button.icon = "star-outline"
        print("before")
        button.bind(on_press = self.icon_press(button,value))
        print("after")
        button.pos_hint = {"center_x":0.5,"center_y":0.5}
        self.root.ids['icon'].add_widget(button)
        self.scraping()
        pass

    def search_press(self):
        self.root.ids["mdlab"].text = "Data for "+self.root.ids["mdtext"].text
        self.root.ids["prefer"].text = "Add to prefer: "
        if self.root.ids["mdtext"].text in my_dict:
            my_dict[self.root.ids["mdtext"].text] = not my_dict[self.root.ids["mdtext"].text]
        else:
            my_dict[self.root.ids["mdtext"].text] = True
        
        my_file = open("myDictionary.pickle","wb")
        pickle.dump(my_dict,my_file)
        my_file.close()
        self.read_prefer()
        value = True
        my_dict[self.root.ids["mdtext"].text] = value
        self.create_Button(value)

    def icon_press(button,self,value):
        print("inside")
        if value==True:
            button.icon = "star-outline" 
        else:
            button.icon = "star-off-outline" 
        pass

    def show_app_info_dialog(self):
        app_info= "Covid tracker\n"
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title = "App Information",
                text = app_info,
                auto_dismiss = True
            )
        self.info_dialog.open()
        pass

    def read_prefer(self):
        my_file = open("myDictionary.pickle","rb")
        my_dict = pickle.load(my_file)
        my_file.close()
        print(my_dict)
        pass

    def show_contact_dialog(self):
        app_info= "Contact: gabriele.sarti1@studenti.unimi.it\n"
        if not self.contact_dialog:
            self.contact_dialog = MDDialog(
                title = "My Contact",
                text = app_info,
                auto_dismiss = True
            )
        self.contact_dialog.open()
        pass


MainApp().run()

