import json
import time

import paho.mqtt.client as mqtt

id = '67d75ceb-5e94-4531-8472-c05f7864e462'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'nightlight-server'

protocol_version = mqtt.MQTTv5

mqtt_client = mqtt.Client(client_id=client_name, protocol=protocol_version)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received: ", payload)

    command = { 'led_on' : payload['light'] < 300}
    print("Sending message:", command)

    client.publish(server_command_topic, json.dumps(command))

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)