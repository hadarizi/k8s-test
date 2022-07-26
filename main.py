import os
import flask
from flask import Flask

app = Flask(__name__)
port = os.getenv('PORT')

@app.route("/health")
def health():
    return "service is healthy"

@app.route("/")
def root():
    return "200"

@app.route("/host_ip")
def ip():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address

if __name__ == "__main__":
    app.run(host='localhost',port=port,debug=True)
