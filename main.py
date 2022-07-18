import os
import sys

from flask import Flask
import socket

app = Flask(__name__)
port = os.getenv('PORT', 5000)

@app.route("/health")
def health():
    return "service is healthy"

@app.route("/")
def root():
    return "200"

@app.route("/host_ip")
def ip():
    return([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                       [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                         [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# @app.route("/port")
# def port
#     print('Port is:', port)


if __name__ == "__main__":
    app.run(host='localhost',port=port)
