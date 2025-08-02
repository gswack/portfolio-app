from flask import Flask, request
import logging 
import datetime 

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    timestamp = datetime.datetime.now().isoformat()
    client_ip = request.remote_addr
    logging.info(f"Received request from {client_ip} at {timestamp}")
    return "Hello, this is my devops app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
