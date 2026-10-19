from flask import Flask
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

LOG_DIR = Path("/app/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

@app.route("/")
def home():
    msg = f"접속 시간: {datetime.now().isoformat()}\n"
    with open(LOG_DIR / "access.log", "a") as f:
        f.write(msg)
    return msg

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)