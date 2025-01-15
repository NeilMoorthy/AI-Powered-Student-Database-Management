import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import MDTextFieldRect

import pickle

'''data = pd.read_csv("student-mat.csv", sep=';')
cols=['G1',"G2","G3","studytime",'failures','absences']
rows=[(g1,g2,g3,st,fail,ab)]
data=pd.DataFrame(columns=cols)
data=data[['G1',"G2","G3","studytime",'failures','absences']]
predict= 'G3'
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
print(x_test)'''

'''best =0
for x in range (100):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)


    linear=linear_model.LinearRegression()
    linear.fit(x_train,y_train)
    acc=linear.score(x_test,y_test)

    if acc>best:
        best=acc
        with open("stumodel.pickle","wb") as f:
            pickle.dump(linear,f)'''
pickle_in = open("stumodel.pickle", "rb")
linear = pickle.load(pickle_in)


class predict(Screen):
    def sub(self, butt):
        x = self.ftf.text
        y = self.stf.text
        z = self.ttf.text
        b = self.etf.text
        c = self.ptf.text
        a = [[int(x), int(y), int(z), int(b), int(c)]]
        predictions = linear.predict(a)
        score = 0
        for x in range(len(predictions)):
            score = predictions[x]
        s = str(int(score))
        if int(s)>100:
            s="NOT DEFINED"
        f = 'PREDICTED SCORE IS '
        toast(f + s)

        for widget in self.children:
            if isinstance(widget, MDTextFieldRect):
                widget.text = ""

    def back(self, butt):
        self.parent.current = "hp"
        self.parent.transition.direction = "right"

    def __init__(self):
        super(predict, self).__init__()
        self.name = "pre"
        self.add_widget(Image(source="student data.jpg", pos_hint={"top": 1.1, "right": 1.3}))
        self.mylbl = Label(text="PREDICT SCORE", size_hint=(0.5, 0.35), pos_hint={"top": 0.98, "right": 0.5},
                           font_size='50sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)

        self.mylbl = Label(text="Grade 1", size_hint=(0.2, 0.07), pos_hint={"top": 0.67, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.ftf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.6, "right": 0.3})
        self.add_widget(self.ftf)

        self.stf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.43, "right": 0.3})
        self.mylbl = Label(text="Grade 2", size_hint=(0.2, 0.07), pos_hint={"top": 0.5, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.stf)
        self.ttf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.26, "right": 0.3})
        self.mylbl = Label(text="Study time", size_hint=(0.2, 0.07), pos_hint={"top": 0.33, "right": 0.2},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.ttf)

        self.mylbl = Label(text="Failures", size_hint=(0.2, 0.07), pos_hint={"top": 0.67, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.etf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.6, "right": 0.7})
        self.add_widget(self.etf)

        self.ptf = MDTextFieldRect(size_hint=(0.3, 0.07), pos_hint={"top": 0.43, "right": 0.7})
        self.mylbl = Label(text="Absences", size_hint=(0.2, 0.07), pos_hint={"top": 0.5, "right": 0.6},
                           font_size='25sp', color=(0, 0, 0, 1))
        self.add_widget(self.mylbl)
        self.add_widget(self.ptf)

        self.but = MDFlatButton(text="SUBMIT", size_hint=(0.3, 0.1), pos_hint={"top": 0.1, "right": 0.99},
                                on_press=self.sub)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)
        self.but = MDIconButton(icon="keyboard-backspace", size_hint=(0.1, 0.1), pos_hint={"top": 0.999, "right": 0.1},
                                on_release=self.back)
        self.but.background_color = (1, 1, 1, 1)
        self.add_widget(self.but)


class _App(MDApp):
    def build(self):
        self.icon = "files.png"
        self.title = "STUDENT DATA"
        return predict()


if __name__ == '__main__':
    burr = _App()
    burr.run()
