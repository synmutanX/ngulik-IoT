# # File: microalgae_photobioreactor_iot.py

# from machine import Pin, ADC, PWM
# import network
# import urequests
# import time

# # Wi-Fi credentials
# SSID = "your_wifi_ssid"
# PASSWORD = "your_wifi_password"
# API_ENDPOINT = "http://your-iot-platform-url.com/data"  # Update with your IoT platform endpoint

# # Hardware setup
# led = PWM(Pin(2), freq=1000)  # GPIO2 for LED
# photo_sensor = ADC(Pin(34))   # GPIO34 for photodiode
# photo_sensor.atten(ADC.ATTN_11DB)  # Full range (0-3.3V)

# # Connect to Wi-Fi
# def connect_wifi():
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(SSID, PASSWORD)
#     while not wlan.isconnected():
#         print("Connecting to Wi-Fi...")
#         time.sleep(1)
#     print("Connected:", wlan.ifconfig())

# # Measure light intensity
# def measure_light():
#     return photo_sensor.read()

# # Send data to IoT platform
# def send_data(od_value):
#     data = {"optical_density": od_value}
#     try:
#         response = urequests.post(API_ENDPOINT, json=data)
#         print("Data sent:", response.text)
#         response.close()
#     except Exception as e:
#         print("Failed to send data:", e)

# # Main loop
# connect_wifi()
# I0 = 500  # Calibration: light intensity with no algae (set this experimentally)

# while True:
#     I = measure_light()
#     if I > 0:
#         OD = round(2 - (I0 / I), 2)  # Simplified Beer-Lambert approximation
#         print("Optical Density (OD):", OD)
#         send_data(OD)
#     time.sleep(10)  # Send every 10 seconds

# File: simulate_microalgae_iot.py

import random
import time
import requests

# Simulated Wi-Fi and API endpoint
API_ENDPOINT = "http://localhost:5000/data"

# Simulated light sensor function
def measure_light():
    # Simulate sensor reading (random values between 100-500)
    """
    Simulate a light sensor reading by generating a random integer between
    100 and 500, inclusive.

    Returns:
        int: Simulated light intensity value.
    """
    return random.randint(100, 500)

# Simulate sending data to IoT platform
def send_data(od_value):
    """
    Send the given optical density value to the IoT platform via the API.

    This function takes a single argument, the optical density value, and sends it
    to the IoT platform using the requests library. The API endpoint is defined
    globally as API_ENDPOINT.

    Args:
        od_value (int): The optical density value to send.

    Returns:
        None
    """
    data = {"optical_density": od_value}
    try:
        response = requests.post(API_ENDPOINT, json=data)
        print("Data sent:", response.status_code, response.text)
    except Exception as e:
        print("Failed to send data:", e)

# Main loop
I0 = 500  # Simulated blank intensity (calibration)

while True:
    I = measure_light()
    if I > 0:
        OD = round(2 - (I0 / I), 2)  # Simulated OD calculation
        print("Simulated Optical Density (OD):", OD)
        send_data(OD)
    time.sleep(5)  # Simulate 5-second intervals

