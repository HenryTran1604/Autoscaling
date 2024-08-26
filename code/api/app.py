from flask import request, jsonify
from __init__ import app
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)
@app.route("/get")
def home():
    return jsonify({"123": "456"})

@app.route("/stress")
def stress():
    cnt = 0
    for i in range(500000):
        cnt += 1
    return jsonify({'cnt': cnt})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)