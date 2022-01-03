from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Guest:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.attending = data['attending']
        self.number_of_guests = data['number_of_guests']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_guest(cls, data):
        query = "INSERT INTO guests (first_name, last_name, email, attending, number_of_guests, message) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(attending)s, %(number_of_guests)s, %(message)s);"
        result = connectToMySQL(
            "wedding_site_schema").query_db(query, data)
        return result

    @classmethod
    def get_guest_by_email(cls, data):
        query = "SELECT * FROM guests WHERE email = %(email)s"
        result = connectToMySQL(
            "wedding_site_schema").query_db(query, data)
        if len(result) == 0:
            return None
        return (cls(result[0]))

    @classmethod
    def get_all_guests(cls):
        query = "SELECT * FROM guests"
        results = connectToMySQL("wedding_site_schema").query_db(query)
        return results

    @classmethod
    def delete_guest(cls, data):
        query = "DELETE FROM guests WHERE id = %(id)s"
        result = connectToMySQL("wedding_site_schema").query_db(query, data)

    @staticmethod
    def validate_guest_info(data):
        is_valid = True

        if len(data['first_name']) < 3 or not data['first_name'].isalpha():
            is_valid = False
            flash("Please enter a First Name")

        if len(data['last_name']) < 3 or not data['last_name'].isalpha():
            is_valid = False
            flash("Please enter a Last Name")

        if len(data['email']) == 0:
            is_valid = False
            flash("Please enter a valid email address")
        elif not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email address")
            is_valid = False
        else:
            if Guest.get_guest_by_email(data) != None:
                is_valid = False
                flash("Email address has already been used to RSVP.")

        if data['attending'] != 0 and data['attending'] != 1:
            print(f'current attending value is {data["attending"]}')
            is_valid = False
            flash("Please select 'Accepts' or 'Regretfully declines' to confirm your attendance status")

        return is_valid
