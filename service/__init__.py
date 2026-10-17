"""Flask app"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("service.config")

talisman = Talisman(app)
CORS(app)

# pylint: disable=wrong-import-position
from service import routes, models  # noqa: E402,F401

models.init_db(app)
