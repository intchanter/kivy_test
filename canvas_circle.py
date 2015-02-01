# this is for testing angle_stop/angle_start

from kivy.app import App
from kivy.lang import Builder

class CircleApp(App):
    def build(self):
        return Builder.load_file('canvas_circle.kv')

CircleApp().run()
