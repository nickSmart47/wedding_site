from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

app.secret_key = "We're getting married! Finally!!"

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDQoVuyT4niuC5N5aor2ydw2r8YqeQmFs8"

GoogleMaps(app, key="AIzaSyDQoVuyT4niuC5N5aor2ydw2r8YqeQmFs8")