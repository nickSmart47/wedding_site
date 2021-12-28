from flask_app import app
from flask_app.controllers import wedding, admin

if __name__ == '__main__':
    app.run(debug=True)