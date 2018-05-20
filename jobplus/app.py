#-*- coding:utf-8 -*-

from flask import Flask
from jobplus.config import configs

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    return app
