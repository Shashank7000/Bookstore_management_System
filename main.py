from cmath import e
from flask import Flask

from lib.extensions import db, jwt
from routes import auth, book, user
from dotenv import load_dotenv
load_dotenv()


# -----------------------------------------------------------------------------------------------
# Initialize Flask App
# -----------------------------------------------------------------------------------------------

app = Flask(__name__)

# Print the database URI or file path
print('database created')
# -----------------------------------------------------------------------------------------------
# Load Config from Environment
# -----------------------------------------------------------------------------------------------

app.config.from_prefixed_env()

# -----------------------------------------------------------------------------------------------
# Initialize Extensions
# -----------------------------------------------------------------------------------------------

db.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()
# -----------------------------------------------------------------------------------------------
# Register Blueprints
# -----------------------------------------------------------------------------------------------

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(book, url_prefix="/book")

    # Run the application
app.run(debug=True)
