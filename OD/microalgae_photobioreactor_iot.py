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

