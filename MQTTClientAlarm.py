import time
import paho.mqtt.client as mqtt
import datetime
import json

from ifttt_webhook import IftttWebhook


IFTTT_KEY = ""
ifttt = IftttWebhook(IFTTT_KEY)

id = 'Spack'

client_telemetry_topic = 'champ/iot/spack'
server_command_topic = client_telemetry_topic
client_name = id + 'led'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = message.payload.decode()
    print(payload)
    recTime = datetime.datetime.now()


    print("Message received at: ", recTime)

    if(payload == "Alarm Active"):
        ifttt.trigger("alarm_active", value1="alarm_active")
 

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(1)