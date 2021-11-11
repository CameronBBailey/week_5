from flask import Flask
from flask import Flask
from config import Config
from .site.routes import site
from .donate.routes import donate
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma 
from flask_cors import CORS
from Main_Package_Folder.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(donate)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
login_manager.login_view = 'auth.signin'
migrate = Migrate(app, root_db)

CORS(app)

app.json_encoder = JSONEncoder

