import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from scraper import *
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
import pickle
from kivymd.uix.button import MDIconButton
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class FirstWindow(Screen):
    pass

class Blank_Page(Screen):
    pass

class MainApp(MDApp):
    count = 0
    info_dialog = None
    contact_dialog = None
    favorites_dialog = None
    button_ = None
    value_ = None
    my_dict = {}
 
    def build(self):
        self.title = "Covid Application"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("app_kv.kv")
 
    def scraping(self):
        new_text = scraper(self.root.ids["mdtext"].text)
        self.root.ids["info"].text = new_text
 
    def create_Button(self,count):
        if count==1:
            button = MDIconButton()
            button.icon = "star-outline"
            self.button_ = button
            button.pos_hint = {"center_x": 0.6, "center_y": 0}
            self.root.ids['icon'].add_widget(button)
            button.bind(on_press=self.icon_press)
        self.scraping()
 
    def search_press(self):
        self.count+=1
        self.root.ids["prefer"].text = "Add to prefer: "
        if not self.root.ids["mdtext"].text in self.my_dict:
            self.my_dict[self.root.ids["mdtext"].text] = False
        my_file = open("myDictionary.pickle", "wb")
        pickle.dump(self.my_dict, my_file)
        my_file.close()
        self.read_prefer()
        self.create_Button(self.count)
        self.reset_prefer()
 
    def icon_press(self,*args,**kwargs):
        self.read_prefer()
        if self.my_dict[self.root.ids["mdtext"].text]==False:
            self.my_dict[self.root.ids["mdtext"].text]=True
            self.button_.icon = "star-off"
        else:
            self.my_dict[self.root.ids["mdtext"].text]=False
            self.button_.icon = "star-outline"
        print(self.my_dict)
 
    def reset_prefer(self,*args,**kwargs):
        if self.my_dict[self.root.ids["mdtext"].text]==True:
            self.button_.icon = "star-off"
        else:
            self.button_.icon = "star-outline"

    def read_prefer(self):
        my_file = open("myDictionary.pickle", "rb")
        my_dict = pickle.load(my_file)
        my_file.close()
 
    def show_app_info_dialog(self):
        app_info = "Covid tracker\n"
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title="App Information",
                text=app_info,
                auto_dismiss=True
            )
        self.info_dialog.open()
 
    def show_contact_dialog(self):
        app_contact = "Contact: gabriele.sarti1@studenti.unimi.it\n"
        if not self.contact_dialog:
            self.contact_dialog = MDDialog(
                title="My Contact",
                text=app_contact,
                auto_dismiss=True
            )
        self.contact_dialog.open()
 
    def show_favorites_dialog(self):
        text= ""
        self.app_favorites = ""
        for item in self.my_dict:
            if self.my_dict[item]==True:
                self.app_favorites=self.app_favorites+"\n"+item 
        if not self.favorites_dialog:
            self.favorites_dialog = MDDialog(
                title="List of favorites",
                text=self.app_favorites,
                auto_dismiss=True
            )
        self.favorites_dialog.open()
        self.favorites_dialog = False


if __name__ == "__main__":
    MainApp().run()