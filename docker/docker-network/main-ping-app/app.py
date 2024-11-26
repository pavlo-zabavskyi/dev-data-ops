from flask import Flask, jsonify
import requests

app = Flask(__name__)

SECONDARY_APP_URL = 'http://secondary-app:8050'


@app.get('/')
def hello():
    return jsonify({
            "status": "success",
            "message": "Hi there! This is the Main App."
    }), 200


@app.get('/ping_secondary_app')
def ping_secondary_app():
    try:
        response = requests.get(SECONDARY_APP_URL)
        response.raise_for_status()

        return jsonify({
            "status": "success",
            "data": response.json()
        }), 200
    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
