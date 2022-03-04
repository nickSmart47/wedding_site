from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from .settings import settings
import logging



app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.secret_key = settings["secret_key"]

app.config['GOOGLE_MAPS_KEY'] = settings["GOOGLE_MAPS_KEY"]

GoogleMaps(app, key=settings["GOOGLE_MAPS_KEY"])

