'''
Demonstrate an apparent issue in Kivy:

Child widgets created in kivy language and the .children attribute are in
opposite order to each other. My intuition was that they would be in the same
order. I was unable to find any documentation one way or another, so
hopefully this will get it corrected if the behavior is incorrect and
clearly documented if the behavior is correct.

Observed behavior:

Child order in the kivy string: 0 through 8
Child order as displayed: 0 through 8
Child order from .children: 8 through 0
Output (between rows of asterisks):
    ['8', '7', '6', '5', '4', '3', '2', '1', '0']

Expected behavior:

Child order from .children matches the order in the kivy string and as
displayed.
Output (between rows of asterisks):
    ['0', '1', '2', '3', '4', '5', '6', '7', '8']
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

root_widget = None

kivy_text = '''
GridLayout:
    cols: 3
    Label:
        text: '0'
    Label:
        text: '1'
    Label:
        text: '2'
    Label:
        text: '3'
    Label:
        text: '4'
    Label:
        text: '5'
    Label:
        text: '6'
    Label:
        text: '7'
    Label:
        text: '8'
'''

class ChildOrderBugApp(App):
    def build(self):
        global root_widget
        root_widget = Builder.load_string(kivy_text)
        return root_widget

def print_children(dt):
    def get_text(widget):
        return widget.text
    print('*' * 45)
    print(map(get_text, root_widget.children))
    print('*' * 45)

if __name__ == '__main__':
    app = ChildOrderBugApp()
    Clock.schedule_once(print_children)
    app.run()
