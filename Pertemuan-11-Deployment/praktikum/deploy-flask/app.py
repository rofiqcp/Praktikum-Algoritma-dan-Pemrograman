import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET", "dev-only-not-for-production")


def app_name():
    return os.getenv("APP_NAME", "Praktikum Deployment")


@app.get("/")
def home():
    return f"{app_name()} — service aktif"


@app.get("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "service": app_name(),
            "environment": os.getenv("APP_ENV", "development"),
        }
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
