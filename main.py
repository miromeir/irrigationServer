from flask_api import FlaskAPI
from flask_cors import CORS
import mqtt_stuff
import config
import models
import custom_login_manager
from views import main_views

app = FlaskAPI(__name__)
CORS(app)

config_items = [models, config, custom_login_manager, mqtt_stuff]
for config_item in config_items:
   config_funcs = [f for f in config_item.__dict__.values() if hasattr(f, "__config_item__")]
   for f in config_funcs:
      f(app)

app.register_blueprint(main_views)

if __name__ == '__main__':
   app.run()