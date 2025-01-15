from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from testing import Database
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.toast import toast

db = Database(key="AIzaSyCsKfN8Ynpln93Dp2RpOTw40x4VKb0rUdE",
              endpoint="https://studentdata-6eb8f-default-rtdb.firebaseio.com")


class search(Screen):
    def sea(self, butt):

        stu = db.child("studentdata").child(self.ftf.text.lower()).get()
        if stu == None:
            toast("PLEASE CHECK THE NAME ENTERED")
        if stu != None:
            self.parent.sk = stu

            self.parent.current = "edp"

    def back(self, butt):
        self.parent.current = "hp"
        self.parent.transition.direction = "right"

    def __init__(self):

        super(search, self).__init__()
        self.name = "sdp"
        self.add_widget(Image(source="student data.jpg", pos_hint={"top": 1.1, "right": 1.3}))
        self.mylbl = Label(text="FIND", size_hint=(0.5, 0.35), pos_hint={"top": 0.99, "right": 0.35},
                           font_size='50sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.mylbl = Label(text="Search", size_hint=(0.2, 0.07), pos_hint={"top": 0.7, "right": 0.15},
                           font_size='20sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.ftf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.65, "right": 0.3})
        self.add_widget(self.ftf)

        self.but = MDIconButton(icon="account-search", size_hint=(0.1, 0.1), pos_hint={"top": 0.66, "right": 0.38},
                                on_release=self.sea)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)

        self.but = MDIconButton(icon="keyboard-backspace", size_hint=(0.1, 0.1), pos_hint={"top": 0.999, "right": 0.1},
                                on_release=self.back)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)
