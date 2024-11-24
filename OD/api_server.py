from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive optical density data
@app.route('/data', methods=['POST'])
def receive_data():
    try:
        # Parse incoming JSON data
        data = request.json
        od_value = data.get('optical_density')
        
        if od_value is not None:
            print(f"Received OD value: {od_value}")
            # Here, you can process or store the data (e.g., save to a database)
            return jsonify({"message": "Data received successfully"}), 200
        else:
            return jsonify({"error": "Invalid data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
