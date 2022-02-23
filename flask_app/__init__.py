from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import logging


import config


app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.secret_key = config.config["secret_key"]

app.config['GOOGLE_MAPS_KEY'] = config.config["GOOGLE_MAPS_KEY"]

GoogleMaps(app, key=config.config["GOOGLE_MAPS_KEY"])

