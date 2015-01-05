from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

app_definition = '''
FloatLayout:
    Scatter:
        Label:
            text: 'Hey, Jeff!'
            font_size: 150
'''

class TutorialApp(App):
    def build(self):
        return Builder.load_string(app_definition)

if __name__ == '__main__':
    TutorialApp().run()
