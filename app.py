# Flask is a small web framework
from flask import Flask
import logging
# Automatically exposes metrics at /metrics (used in Module 8)
from prometheus_flask_exporter import PrometheusMetrics

# Show time and severity in log lines
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
metrics = PrometheusMetrics(app)   # adds /metrics endpoint

@app.route("/")
def home():
    logging.info("Home page requested")
    return "Hello, DevOps Team: CI CD"

@app.route("/health")
def health():
    # Monitoring tools call this to check the app is alive
    return {"status": "ok"}, 200

# A plain function so we can show a simple unit test
def add(a, b):
    return a + b

if __name__ == "__main__":
    # 0.0.0.0 = reachable from outside a container
    app.run(host="0.0.0.0", port=5000)
