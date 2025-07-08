from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname":  socket.gethostname(),
        "message": "cicd",
        "deployed_on": "k8s",
        "env": "${{values.app_env}}",
        "app_name": "${{values.app_name}}"
    })

@app.route('/api/v1/health')

def health():
    return jsonify({
        "status": "up"
    }), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")
