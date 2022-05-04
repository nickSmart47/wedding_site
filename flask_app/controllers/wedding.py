from flask_app import app
from flask import url_for, render_template, redirect, request, session, flash
from flask_app.models.guest import Guest
from flask_googlemaps import Map, GoogleMaps


@app.route('/')
def index():
    return render_template("index.html")

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
    if Guest.validate_guest_info(data):
        new_guest = Guest.register_guest(data)
        return redirect("/rsvp/success")
    else:
        return redirect(url_for('index', _anchor='rsvp'))


@app.route('/rsvp/success')
def rsvp_success():
    return render_template('rsvp_success.html')



