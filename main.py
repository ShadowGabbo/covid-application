from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:

    MDRectangleFlatButton:
        text:"Press to see Covid"
        pos_hint: {"center_x":0.5, "center_y":0.5} #or x,y
"""


class MainApp(MDApp):
    
    def build(self):
        self.title = "Hello Kivymd"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

MainApp().run()