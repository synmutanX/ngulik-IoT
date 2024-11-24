# File: microalgae_photobioreactor_iot.py

from machine import Pin, ADC, PWM
import network
import urequests
import time

# Wi-Fi credentials
SSID = "your_wifi_ssid"
PASSWORD = "your_wifi_password"
API_ENDPOINT = "http://your-iot-platform-url.com/data"  # Update with your IoT platform endpoint

# Hardware setup
led = PWM(Pin(2), freq=1000)  # GPIO2 for LED
photo_sensor = ADC(Pin(34))   # GPIO34 for photodiode
photo_sensor.atten(ADC.ATTN_11DB)  # Full range (0-3.3V)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected:", wlan.ifconfig())

# Measure light intensity
def measure_light():
    return photo_sensor.read()

# Send data to IoT platform
def send_data(od_value):
    data = {"optical_density": od_value}
    try:
        response = urequests.post(API_ENDPOINT, json=data)
        print("Data sent:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

# Main loop
connect_wifi()
I0 = 500  # Calibration: light intensity with no algae (set this experimentally)

while True:
    I = measure_light()
    if I > 0:
        OD = round(2 - (I0 / I), 2)  # Simplified Beer-Lambert approximation
        print("Optical Density (OD):", OD)
        send_data(OD)
    time.sleep(10)  # Send every 10 seconds
