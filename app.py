import psutil
import socket
from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

if "MSG" in os.environ :
    my_message = os.environ['MSG']

    print(f"\nToday's message : {my_message}\n")
else:
    print(f"Loading .env file...\n")
    my_message = os.getenv['MSG']



app = Flask(__name__)


@app.route('/')
def home():
    print(socket.gethostname())
    print(psutil.cpu_percent())
    print(psutil.virtual_memory().percent)

    payload = {
        "hostname" : socket.gethostname(),
        "cpu" : psutil.cpu_percent(),
        "mem" : psutil.virtual_memory().percent,
        "message" : my_message
    }
    return render_template('index.html', results=payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
