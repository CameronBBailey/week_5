from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .donate.routes import donate


app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(donate)



app.config.from_object(Config)

