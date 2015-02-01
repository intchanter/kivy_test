from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

filename = 'variables.kv'
app = None

class VariableApp(App):
    def build(self):
        return Builder.load_file(filename)

def increment(time):
    app.root.level_number += 1

if __name__ == '__main__':
    Clock.schedule_interval(increment, 1)
    app = VariableApp()
    app.run()


