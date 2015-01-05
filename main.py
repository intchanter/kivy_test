from kivy.app import App
from kivy.lang import Builder

kivy_filename = 'main.kv'

class NumberNabberApp(App):
    def build(self):
        return Builder.load_file(kivy_filename)

if __name__ == '__main__':
    NumberNabberApp().run()
