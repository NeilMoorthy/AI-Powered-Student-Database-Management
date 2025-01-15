from kivymd.app import MDApp
import os, sys
from kivy.resources import resource_add_path
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from add_new import addstu
from edt_stu import estu
from find import fstu
from search import search
from searchfind import search1
from predict import predict
import webbrowser

class studentapp(Screen):
    def on_enter(self, *args):
        self.parent.transition.direction = "left"

    def sca(self, burr):
        self.parent.current = "adp"

    def scaf1(self, burr):
        self.parent.current = "sdp"

    def scaf2(self, burr):
        self.parent.current = "s1dp"
    def pred(self,burr):
        self.parent.current='pre'
    def open(self,burr):
        webbrowser.open('http://localhost:8501' )


    def __init__(self):
        super(studentapp, self).__init__()
        self.name = "hp"
        self.add_widget(Image(source="student data.jpg", pos_hint={"top": 1.1, "right": 1.3}))
        self.mylbl = Label(text="STUDENT DATABASE MANAGER", size_hint=(0.4, 0.35), pos_hint={"top": 0.9, "right": 0.45},
                           font_size='50sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.mylbl = Label(text="MADE BY NEIL B MOORTHY, KAVYA SINGH", size_hint=(0.4, 0.35),
                           pos_hint={"top": 0.3, "right": 0.9},
                           font_size='10sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.but = MDFlatButton(text=("ADD NEW STUDENT"), size_hint=(0.3, 0.1), pos_hint={"top": 0.4, "right": 0.3},
                                on_release=self.sca)
        self.add_widget(self.but)
        self.but.background_color = (1, 1, 1, 1)
        self.but = MDFlatButton(text=("EDIT OLDER DATA"), size_hint=(0.3, 0.1), pos_hint={"top": 0.5, "right": 0.3},
                                on_release=self.scaf1)
        self.add_widget(self.but)
        self.but.background_color = (1, 1, 1, 1)
        self.but = MDFlatButton(text=("FIND STUDENT DATA"), size_hint=(0.3, 0.1), pos_hint={"top": 0.6, "right": 0.3},
                                on_release=self.scaf2)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)
        self.but.background_color = (1, 1, 1, 1)
        self.but = MDFlatButton(text=("PREDICT"), size_hint=(0.3, 0.1), pos_hint={"top": 0.3, "right": 0.3},
                                on_release=self.pred)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)
        self.but = MDFlatButton(text=("CHAT"), size_hint=(0.3, 0.1), pos_hint={"top": 0.2, "right": 0.3},
                                on_release=self.open)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)


class sm(ScreenManager):
    def __init__(self):
        super(sm, self).__init__()
        hp = studentapp()
        self.add_widget(hp)
        adp = addstu()
        self.add_widget(adp)
        edp = estu()
        self.add_widget(edp)
        sdp = search()
        self.add_widget(sdp)
        fdp=fstu()
        self.add_widget(fdp)
        s1dp=search1()
        self.add_widget(s1dp)
        pre=predict()
        self.add_widget(pre)
        self.sk=None


class _App(MDApp):
    def build(self):
        self.icon = "files.png"
        self.title = "STUDENT DATA"
        return sm()


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    _App().run()
