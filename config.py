######################
# Application Config #
######################
import os

from config_init import config_item

if os.environ.get("ENV") == "DEV":
  app_config = {
      'SECRET_KEY': 'secret-key-goes-here',
      'SQLALCHEMY_DATABASE_URI': 'postgresql://miro:kUjh5rvx@127.0.0.1:5432/flask_db',
      'REMEMBER_COOKIE_DOMAIN': ".irrigation.cc",
      'MQTT_BROKER_URL': '127.0.0.1',
      'MQTT_BROKER_PORT': 1883,
  }
else:
  app_config = {
      'SECRET_KEY': 'secret-key-goes-here',
      'SQLALCHEMY_DATABASE_URI': 'postgresql://miromeir:kUjh5rvx@database-1.cgkckwgsr4d3.us-east-1.rds.amazonaws.com:5432',
      'REMEMBER_COOKIE_DOMAIN': ".irrigation.cc",
      'MQTT_BROKER_URL': '127.0.0.1',
      'MQTT_BROKER_PORT': 1883,
  }

def after_request(response):
  response.headers.add("Access-Control-Allow-Headers", "content-type, Content-type, Content-Type")
  response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
  response.headers.add("Access-Control-Expose-Headers", "*")
  if os.environ.get("ENV") == "DEV":
    response.headers.add('Access-Control-Allow-Origin', "https://app.irrigation.cc:3000")
  else:
    response.headers.add('Access-Control-Allow-Origin', "https://app.irrigation.cc")
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  
  return response

@config_item
def config(app):
  app.config.update(app_config)
  app.after_request_funcs.setdefault(None, []).append(after_request)