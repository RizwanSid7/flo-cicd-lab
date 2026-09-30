from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "flo-cicd-lab",
        "environment": os.getenv("ENVIRONMENT", "local"),
        "version": os.getenv("APP_VERSION", "dev"),
        "message": "Hello from version 2"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)