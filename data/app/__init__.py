from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

# __name__ = data
app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('logs/data.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# config session in app
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SESSION_PERMANENT'] = False  # Sessions won't expire on browser close
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)  # Session timeout

# Configure JWT settings
# # app.config['JWT_SECRET_KEY'] = 'ABC123ABC123'  # Replace with your secret key
# # jwt = JWTManager(app)

from . import routes

