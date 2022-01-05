from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import logging

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.secret_key = "We're getting married! Finally!!"

app.config['GOOGLE_MAPS_KEY'] = "AIzaSyDQoVuyT4niuC5N5aor2ydw2r8YqeQmFs8"

GoogleMaps(app, key="AIzaSyDQoVuyT4niuC5N5aor2ydw2r8YqeQmFs8")