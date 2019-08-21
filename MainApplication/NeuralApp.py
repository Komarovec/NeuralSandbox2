"""
Basic menu system for NS2

Denis Kurka - 11.7.2019
"""

import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from windows.CanvasWindow import CanvasWindow

from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.write()

#Window classes
class MainMenuWindow(Screen):
    pass

#KV files import
Builder.load_file("templates/mainmenu.kv")
Builder.load_file("templates/canvas.kv")

#Screen manager
sm = ScreenManager()
screens = [MainMenuWindow(name="mainmenu"), CanvasWindow(name="canvas")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "mainmenu"

#Main class
class NeuralApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    NeuralApp().run()