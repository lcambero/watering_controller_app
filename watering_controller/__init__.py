from flask import Flask

app = Flask(__name__)

wc = None

from watering_controller import routes