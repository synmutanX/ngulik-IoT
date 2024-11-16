import json
import paho.mqtt.client as mqtt
import time
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed

# Initialize CounterFit Connection (IoT simulation)
CounterFitConnection.init('127.0.0.1', 5000)

print("Hello IoT World!")

# Setup the light sensor and LED
light_sensor = GroveLightSensor(0)
led = GroveLed(5)

# Define client ID and name
id = '67d75ceb-5e94-4531-8472-c05f7864e462'
client_name = id + 'nightlight_client'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

# Use the appropriate protocol version (MQTTv5 or MQTTv311)
protocol_version = mqtt.MQTTv5  # Use mqtt.MQTTv311 if you're working with MQTT 3.1.1

# Pass the client_id explicitly to avoid the multiple values error
mqtt_client = mqtt.Client(client_id=client_name, protocol=protocol_version)

# Connect to the MQTT broker
mqtt_client.connect('test.mosquitto.org')

# Start the MQTT client loop in the background
mqtt_client.loop_start()

def handle_command(client, userdata, message):
    """
    Handle MQTT command messages from the CounterFit server.

    This is a callback function that is called whenever an MQTT message is received from the
    CounterFit server with a topic matching the server_command_topic. The message payload is
    expected to contain a JSON object with a single key-value pair. The key is named
    'led_on' and the value is a boolean (True or False). If the value is True, the LED
    is turned on; otherwise, the LED is turned off.

    Parameters:
        client: The MQTT client that received the message.
        userdata: User-defined data associated with the MQTT client.
        message: The MQTT message that was received.

    Returns:
        None
    """
    # Decodes the message payload as JSON
    payload = json.loads(message.payload.decode())
    print("message received: ", payload)

    # Turns the LED on or off based on the value of the 'led_on' key in the JSON payload (True for on, False for off)
    if payload['led_on']:
        led.on()
    else:
        led.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

print("MQTT Connected!")

# Infinite loop to monitor light levels and control LED
# while True:
#     light = light_sensor.light
#     print('Light level:', light)

#     if light < 300:
#         led.on()
#     else:
#         led.off()    
#     time.sleep(1)

while True:
    light = light_sensor.light
    telemetry = json.dumps({'light': light})

    # print("Sending telemetry ", telemetry)
    print('Light level:', light)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(5)