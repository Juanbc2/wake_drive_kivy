import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from iot import IoT
from kivy.core.window import Window

class Contenedor(App):  # el archivo kv debe llamarse igual que esta clase
    sm = ScreenManager()

    def build(self):
        # Cambia el directorio de trabajo actual al directorio del script
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        Window.size = (1024, 768)
        self.sm.add_widget(IoT(name='iot'))
        return self.sm

Contenedor().run()