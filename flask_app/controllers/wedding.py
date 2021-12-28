from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.guest import Guest
from flask_googlemaps import Map, GoogleMaps


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/rsvp')
def rsvp_form():
    return render_template('rsvp.html')


@app.route('/guest_rsvp', methods=["POST"])
def guest_rsvp():
    if request.form['attending'] == "accepts":
        attending = 1
    else:
        attending = 0
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "attending": attending,
        "number_of_guests": request.form['number_of_guests'],
        "message": request.form['message']
    }
    print(data)
    if Guest.validate_guest_info(data):
        new_guest = Guest.register_guest(data)
        return redirect("/rsvp/success")
    else:
        return redirect("/rsvp")


@app.route('/rsvp/success')
def rsvp_success():
    return render_template('rsvp_success.html')


@app.route('/details')
def details():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    return render_template('details.html', mymap=mymap, sndmap=sndmap)
