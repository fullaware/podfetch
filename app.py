import psutil
import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    print(socket.gethostname())
    print(psutil.cpu_percent())
    print(psutil.virtual_memory())

    payload = {
        "hostname" : socket.gethostname(),
        "cpu" : psutil.cpu_percent(),
        "mem" : psutil.virtual_memory()
    }
    return render_template('index.html', results=payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
