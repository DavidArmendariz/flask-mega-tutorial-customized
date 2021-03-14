from flask import Flask

from config import DevelopmentConfig, TestingConfig, ProductionConfig


def create_app(environment="development"):
    app = Flask(__name__)
    set_app_config(app, environment)

    @app.route('/')
    def index():
        return "Hello world!"

    return app


def set_app_config(app, environment: str):
    config_object = None
    if environment == "development":
        config_object = DevelopmentConfig()
    if environment == "testing":
        config_object = TestingConfig()
    if environment == "production":
        config_object = ProductionConfig()
    if config_object:
        app.config.from_object(config_object)
