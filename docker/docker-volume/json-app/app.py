from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

JSON_FILE_PATH = '/tmp/test.json'

if not os.path.exists(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump({}, f)

@app.get('/json')
def read_json():
    try:
        with open(JSON_FILE_PATH, 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.post('/json')
def write_json():
    try:
        new_data = request.get_json()

        if not new_data:
            return jsonify({"error": "Invalid JSON data"}), 400

        with open(JSON_FILE_PATH, 'r+') as f:
            data = json.load(f)  # Load existing data
            data.update(new_data)  # Update with new data
            f.seek(0)  # Move the pointer to the beginning
            json.dump(data, f, indent=4)  # Write updated data back to the file
            f.truncate()  # Remove any remaining old content

        return jsonify({"message": "Data written successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
