from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from .utils.db import db

app = Flask(__name__)

# configuracion de conexion
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/arcade'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# agregamos la base de datos a la app
db.init_app(app)

# Protecion de csrf a la app
csrf = CSRFProtect()

# Y las migraciones
migrate = Migrate()

# Siempre las migraciones dejar fuera de funcion create_app
migrate.init_app(app, db)

from .views import page, auth


def create_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_blueprint(page)
    return app