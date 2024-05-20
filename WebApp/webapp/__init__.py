from flask import Flask
from webapp import pages
from webapp.database import init_db

import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_prefixed_env()
    init_db(app)

    app.register_blueprint(pages.bp)

    return app
