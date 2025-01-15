from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from testing import Database
from kivymd.uix.textfield import MDTextFieldRect

db = Database(key="AIzaSyCsKfN8Ynpln93Dp2RpOTw40x4VKb0rUdE",
              endpoint="https://studentdata-6eb8f-default-rtdb.firebaseio.com")


class estu(Screen):
    def on_enter(self, *args):
        d = self.parent.sk
        self.ftf.text = d["name"]
        self.stf.text = d["class"]
        self.ttf.text = d['rollno']
        self.etf.text = d["eng"]
        self.ptf.text = d["phy"]
        self.ctf.text = d['chem']
        self.mtf.text = d['math']
        self.otf.text = d['opt']

    def sub(self, butt):
        sd = {"name": self.ftf.text.lower(), "class": self.stf.text, "rollno": self.ttf.text, "eng": self.etf.text
            , "math": self.mtf.text, "phy": self.ptf.text, "chem": self.ctf.text, "opt": self.otf.text}

        db.child("studentdata").child(sd["name"]).set(sd)

        toast("SUCCESSFULLY UPDATED")

    def back(self, butt):
        self.parent.current = "hp"
        self.parent.transition.direction = "right"

    def __init__(self):
        super(estu, self).__init__()
        self.name = "edp"
        self.add_widget(Image(source="student data.jpg", pos_hint={"top": 1.1, "right": 1.3}))
        self.mylbl = Label(text="Edit student details", size_hint=(0.5, 0.35), pos_hint={"top": 0.9, "right": 0.6},
                           font_size='50sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.mylbl = Label(text="Name", size_hint=(0.2, 0.07), pos_hint={"top": 0.67, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.ftf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.6, "right": 0.3})
        self.add_widget(self.ftf)

        self.stf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.43, "right": 0.3})
        self.mylbl = Label(text="Class", size_hint=(0.2, 0.07), pos_hint={"top": 0.5, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.stf)
        self.ttf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.26, "right": 0.3})
        self.mylbl = Label(text="Roll Number", size_hint=(0.2, 0.07), pos_hint={"top": 0.33, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.ttf)

        self.mylbl = Label(text="English", size_hint=(0.2, 0.07), pos_hint={"top": 0.67, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.etf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.6, "right": 0.7})
        self.add_widget(self.etf)

        self.ptf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.43, "right": 0.7})
        self.mylbl = Label(text="Physics", size_hint=(0.2, 0.07), pos_hint={"top": 0.5, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.ptf)

        self.ctf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.26, "right": 0.7})
        self.mylbl = Label(text="Chemistry", size_hint=(0.2, 0.07), pos_hint={"top": 0.33, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.ctf)

        self.mtf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.1, "right": 0.3})
        self.mylbl = Label(text="Mathematics", size_hint=(0.2, 0.07), pos_hint={"top": 0.16, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.mtf)

        self.otf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.1, "right": 0.7})
        self.mylbl = Label(text="Optional", size_hint=(0.2, 0.07), pos_hint={"top": 0.16, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.otf)

        self.but = MDFlatButton(text="SUBMIT", size_hint=(0.3, 0.1), pos_hint={"top": 0.1, "right": 0.99},
                                on_release=self.sub)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)

        self.but = MDIconButton(icon="keyboard-backspace", size_hint=(0.1, 0.1), pos_hint={"top": 0.999, "right": 0.1},
                                on_release=self.back)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)
