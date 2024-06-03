from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from iot import IoT
from kivy.core.window import Window
import os

class Contenedor(App):  # el archivo kv debe llamarse igual que esta clase
    sm = ScreenManager()
    path = os.path.dirname(os.path.abspath(__file__))

    def build(self):
        Window.size = (1024, 768)
        self.sm.add_widget(IoT(name='iot', path=self.path))
        return self.sm

Contenedor().run()