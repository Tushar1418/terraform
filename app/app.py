from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Python app on EKS! Image: {os.environ.get('IMAGE_TAG', 'unknown')}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
