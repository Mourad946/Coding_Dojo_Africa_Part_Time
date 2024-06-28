from flask import Flask

app = Flask(__name__)

# Example of registering a route within this file, if needed
@app.route('/')
def home():
    return "Hello, Flask!"

# Import controllers to register routes from other files
from flask_app.controllers import user

# If using blueprints, register them here
# app.register_blueprint(user.bp)
