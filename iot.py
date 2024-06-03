from _thread import start_new_thread
from kivy.uix.screenmanager import Screen
from external_comm import UbidotsPublisher
from internal_comm import Listener
from kivy.clock import mainthread
from kivy.properties import NumericProperty
class IoT(Screen):

    pulse = NumericProperty(0)
    shock = NumericProperty(0)
    emergency = NumericProperty(0)

    def __init__(self, **kw):
        super().__init__(**kw)
        escuchador = Listener(self)
        try:
            start_new_thread(escuchador.start, ())
        except Exception as ex:
            print("Error: no se pudo iniciar el hilo. ex: {}".format(ex))

    def handleEmergencyState(self):
        if self.emergency == 1:
            self.ids.emergency_button.background_color = (1, 0, 0, 1)
        else:
            self.ids.emergency_button.background_color = (0, 1, 0, 1)

    @mainthread
    def sendData(self,topic,msg):
        print("Mensaje recibido: topic: {}, payload: {}".format(topic, msg))
        if topic == "pulse":
            self.pulse = int(msg)
        elif topic == "shock":
            self.shock = int(msg)
        elif topic == "emergency":
            self.emergency = int(msg)
        UbidotsPublisher.send_message(topic, msg)
    




