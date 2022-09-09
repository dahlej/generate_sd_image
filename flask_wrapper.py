from flask import Flask
from pyngrok import ngrok
import os


class FlaskNgrok(object):
    def __init__(self, name):
        self.app = Flask(name)
        self.url = None

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.app.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator

    def run(self, port=5000):
        self.shut_down_all_tunnels()
        ngrok.set_auth_token(os.environ["NGROK_AUTH_TOKEN"])
        self.url = ngrok.connect(port).public_url
        self.app.run()

    def shut_down_all_tunnels(self):
        tunnels = ngrok.get_tunnels()
        for t in tunnels:
            ngrok.disconnect(t.public_url)
# class EndPointAction(object):
#     def __init__(self, action):
#         self.action = action
#         self.response = Response(status=200, headers={})
#
#     def __call__(self, *args):`
#         self.action()
#         return self.response
#
#
# class FlaskAppWrapper(object):
#     app = None
#
#     def __init__(self, name):
#         self.flask_host = None
#         self.flask_port = None
#         self.app = Flask(name)
#         ngrok.set_auth_token(os.environ["NGROK_AUTH_TOKEN"])
#
#     def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
#         self.app.add_url_rule(endpoint, endpoint_name, EndPointAction(handler))
#
#     def run(self):
#         self.app.run()
#         self.flask_port = os.environ["FLASK_RUN_PORT"]
#         self.flask_host = os.environ["FLASK_RUN_HOST"]
#         public_url = ngrok.connect(self.flask_port).public_url
#         print(" * ngrok tunnel \"{}\" -> \"{}:{}/\"".format(public_url, self.flask_host, self.flask_port))
#
#     def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
#         self.app.add_url_rule(endpoint, endpoint_name, EndPointAction(handler))

# import os
# import threading
#
# from flask import Flask
# from pyngrok import ngrok
#
# os.environ["FLASK_ENV"] = "development"
# flask_port = os.environ["FLASK_RUN_PORT"]
# ngrok.set_auth_token(os.environ["NGROK_AUTH_TOKEN"])
# public_url = ngrok.connect(flask_port).public_url
# print(" * ngrok tunnel \"{}\" -> \"{}:{}/\"".format(public_url, flask_host, flask_port))
#
#
# def create_app():
#     app = Flask(__name__)
#     app.config["BASE_URL"] = public_url
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# def shut_down_all():
#     for flask_thread in flask_threads:
#         flask_thread.killed = True
