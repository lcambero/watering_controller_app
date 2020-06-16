from flask import Flask
from flask_cors import CORS
import json
from watering_controller.controller import WateringController

CONFIG_FILE_PATH = 'config.json'

app = Flask(__name__)
CORS(app)

with open(CONFIG_FILE_PATH) as f:
    config = json.load(f)

wc = WateringController(config)

from watering_controller import routes