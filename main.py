from kivymd.app import MDApp
from kivy.lang import Builder
from scraper import *

KV = """
Screen:
    GridLayout:
        rows: 2

       
        ScrollView:
            MDLabel:
                id: mdlab
                text:"Welcome to Covid Application"
                font_style: "H4"
                color: "white"
                padding_x:20
                padding_y:50
                size_hint_y:None
                height: self.texture_size[1]
                text_size: self.width, None
                halign: "center"
    MDTextField:
        id: mdtext
        hint_text:"Search a state to see Covid stats for it"
        mode: "rectangle"
        padding_x:5
        pos_hint: {"x":0.1, "y":0.6} 
        size_hint: (.8, .1)

    MDRectangleFlatButton:
        id: mdbu
        text:"Search"
        pos_hint: {"center_x":0.5, "center_y":0.5} #or x,y
        on_press: app.covid_scraping() 

    MDLabel:
        id: info
        text:""
        font_style: "H6"
        color: "white"
        size_hint_y:None
        height: self.texture_size[1]
        text_size: self.width, None      
        pos_hint: {"center_y":0.3}
"""


class MainApp(MDApp):

    def build(self):
        self.title = "Covid Application"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def covid_scraping(self):
        self.root.ids["mdlab"].text = "You've pressed the button"
        new_text= scraper(self.root.ids["mdtext"].text)
        self.root.ids["info"].text = new_text

    def set_textarea(self):
        pass

MainApp().run()