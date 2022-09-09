import os
import threading

from flask import Flask
from pyngrok import ngrok

os.environ["FLASK_ENV"] = "development"
flask_host = os.environ["FLASK_RUN_HOST"]
flask_port = os.environ["FLASK_RUN_PORT"]
ngrok.set_auth_token(os.environ["FLASK_PORT"])
app = Flask(__name__)
public_url = ngrok.connect(flask_port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, flask_port))

flask_threads = []
app.config["BASE_URL"] = public_url


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def start_server():
    flask_threads.append(threading.Thread(target=app.run, kwargs={"use_reloader": False}).start())


def shut_down_all():
    for flask_thread in flask_threads:
        flask_thread.killed = True
