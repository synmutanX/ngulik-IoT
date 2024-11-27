import csv, time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive optical density data
@app.route('/data', methods=['POST'])
def receive_data():
    """
    Receive optical density data via a POST request and perform necessary processing.

    This endpoint expects a JSON payload with an 'optical_density' key. The optical density
    value is extracted, logged, and stored in a CSV file with a timestamp. If the data is
    invalid or missing, an appropriate error message is returned.

    Returns:
        Response: A JSON response indicating the success or failure of the data reception.
            - 200: Data received successfully.
            - 400: Invalid data.
            - 500: Server error.
    """
    try:
        # Parse incoming JSON data
        data = request.json
        od_value = data.get('optical_density')
        
        if od_value is not None:
            print(f"Received OD value: {od_value}")
            # Here, you can process or store the data (e.g., save to a database)
            # Save to CSV
            with open('od_data.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([time.time(), od_value]) # Save timestamp and OD value
            return jsonify({"message": "Data received successfully"}), 200
        else:
            return jsonify({"error": "Invalid data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
