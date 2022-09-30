
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import randint

Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 500)

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical',padding=80, spacing=40)
        self.txt = TextInput()
        self.lbl = Label(text='Вы выйграли: 0')
        btnHow = Button(text='Как играть?')
        btn = Button(text='Сделать ставку')
        layout.add_widget(self.lbl)
        layout.add_widget(self.txt)
        layout.add_widget(btnHow)
        layout.add_widget(btn)
        btn.on_press = self.stavka
        btnHow.on_press = self.menutoplay
        self.add_widget(layout)
    def stavka(self):
        text = self.txt.text
        try:
            text = int(text)
            if text >= 1000:
                text = randint(0, text+5906)
            elif text >= 500 and text < 1000:
                text = randint(0, text+1999)
            else:
                text = randint(0, text*2)
            if int(self.txt.text) > text:
                pro = 'проиграли'
                text = int(self.txt.text) - text
            else:
                pro = 'выйграли'
            text = str(text)
            self.lbl.text = 'Вы {}: {}'.format(pro, text)
        except:
            self.txt.text = '0'
            self.lbl.text = 'Это не число!'
    def menutoplay(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'howtoplay'

class HowToPlayScr(Screen):
    def __init__(self, name='howtoplay'):
        super().__init__(name=name)
        layout = BoxLayout(padding=13, orientation='vertical')
        lbl = Label(text='''Как играть?
         Всё просто в тектовом окне введите ставку, например 100, 200, 1000.
          Игра потом по математичиским моделям напишет ваш выйгрыш.
           Ты везунчик? Проверим! Вперёд!
Автор: Рауф Хабибуллин''')
        btn = Button(text='К игре <--')
        layout.add_widget(lbl)
        layout.add_widget(btn)
        btn.on_press = self.next
        self.add_widget(layout)
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'

        

class Casino(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(HowToPlayScr())
        return sm

app = Casino()
app.run()
