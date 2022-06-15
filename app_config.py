######################
# Application Config #
######################
import os

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
  response.headers.add('Access-Control-Allow-Origin', "app.irrigation.cc")
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  
  return response