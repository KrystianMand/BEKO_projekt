import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db(app):
    import webapp.models

    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_ip = os.getenv('POSTGRES_IP')
    postgres_port = os.getenv('POSTGRES_PORT')
    postgres_database_name = os.getenv('POSTGRES_DATABASE_NAME')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{postgres_user}:{postgres_password}@{postgres_ip}:{postgres_port}/{postgres_database_name}"
    db.init_app(app)
    migrate = Migrate(app, db)