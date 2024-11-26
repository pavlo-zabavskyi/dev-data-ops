from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def hello():
    return jsonify({
            "status": "success",
            "message": "Hi there! This is the Main App."
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)
