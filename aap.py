from flask import Flask
import socket
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/name')
def name():
    return 'ITD Devops'
@app.route('/ip')
def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) 
    return ip_address
if __name__ == '__main__':
    app.run()
