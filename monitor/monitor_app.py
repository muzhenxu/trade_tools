from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='upper threshold'))
        self.upper = TextInput(multiline=False)
        self.add_widget(self.upper)
        self.add_widget(Label(text='lower threshold'))
        self.lower = TextInput(multiline=False)
        self.add_widget(self.lower)
        bn = Button(text='OK')
        self.add_widget(bn)


class MyApp(App):
    def build(self):
        return LoginScreen()
    
    def buttonClicked(self, bn):
        req = UrlRequest('127.0.0.1:10000/get_data?u=%s&l=%s' % (self.upper, self.lower))


if __name__ == '__main__':
    MyApp().run()
