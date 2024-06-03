import paho.mqtt.client as mqttc


PULSE_TOPIC = "pulse"
SHOCK_TOPIC = "shock"
EMERGENCY_TOPIC = "emergency"

BROKER_URL = "localhost"
BROKER_PORT = 1883


class Listener:

    def __init__(self, observador):
        self.client = mqttc.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.observador = observador
        try:
            self.client.connect(BROKER_URL, BROKER_PORT, 60)
        except ConnectionRefusedError:
            print("Sin conexión al broker")

    def start(self):
        print("Looping")
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(PULSE_TOPIC)
        client.subscribe(SHOCK_TOPIC)
        client.subscribe(EMERGENCY_TOPIC)

    def on_message(self, client, userdata, msg):
        print("Mensaje recibido: topic: {}, payload: {}".format(msg.topic, msg.payload.decode("utf-8")))
        self.observador.sendData(msg.topic,msg.payload.decode("utf-8"))

