from flask import Flask, jsonify
import requests

app = Flask(__name__)

MAIN_APP_URL = 'http://main-app:8050'


@app.get('/')
def hello():
    return jsonify({
            "status": "success",
            "message": "Hi there! This is the Secondary App."
    }), 200


@app.get('/ping_main_app')
def ping_secondary_app():
    try:
        response = requests.get(MAIN_APP_URL)
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
