from flask_mqtt import Mqtt
from redis_stuff import redis_device_on

mqtt = Mqtt()
# Mqtt:
@mqtt.on_message()
def on_message(client, userdata, msg):
   topic = msg.topic
   payload = msg.payload
   if "/on" in topic:
      splitted = topic.split("/")
      device_topic = splitted[0]
      val = str(payload)[2:-1]
      redis_device_on.set(device_topic, val)
