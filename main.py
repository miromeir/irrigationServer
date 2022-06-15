
import os
import sys
from urllib.parse import urljoin, urlparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_api import FlaskAPI, status
from flask_cors import CORS
from redis_stuff import redis_device_on
from mqtt_stuff import mqtt
from app_config import app_config, after_request
from models import db, User
from custom_login_manager import login_manager
from views import main_views
import os

app = FlaskAPI(__name__)
CORS(app)
print("https://app.irrigation.cc", file=sys.stderr)
app.config.update(app_config)
db.app=app
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)
mqtt.app=app
mqtt.init_app(app)
db.create_all()
app.after_request_funcs.setdefault(None, []).append(after_request)

app.register_blueprint(main_views)

if __name__ == '__main__':
   app.run()