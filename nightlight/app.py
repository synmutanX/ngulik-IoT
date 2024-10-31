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

# Use the appropriate protocol version (MQTTv5 or MQTTv311)
protocol_version = mqtt.MQTTv5  # Use mqtt.MQTTv311 if you're working with MQTT 3.1.1

# Pass the client_id explicitly to avoid the multiple values error
mqtt_client = mqtt.Client(client_id=client_name, protocol=protocol_version)

# Connect to the MQTT broke
mqtt_client.connect('test.mosquitto.org')

# Start the MQTT client loop in the background
mqtt_client.loop_start()

print("MQTT Connected!")

# Infinite loop to monitor light levels and control LED
while True:
    light = light_sensor.light
    print('Light level:', light)
    
    if light < 300:
        led.on()
    else:
        led.off()

    time.sleep(1)