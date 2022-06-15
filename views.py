from flask import Blueprint, make_response, request
from flask_api import status
from models import User
from flask_login import current_user, login_required, login_user, logout_user
from models import db
from mqtt_stuff import mqtt
from redis_stuff import redis_device_on
from time import time

main_views = Blueprint("main_views", __name__)
@main_views.route('/login',methods=['POST'])
def login():
   name = request.data['name']
   password = request.data['password']
   user = User.query.filter_by(name=name).first()
   if user and user.password == password:
      login_user(user=User.query.first(), remember=True)
      # raise(Exception())
      response = make_response()
      return response
   else:
      return "Failed", status.HTTP_400_BAD_REQUEST

@main_views.route('/logout')
def logout():
   logout_user()
   return "logged out"  

@main_views.route('/registertopic', methods=['GET'])
def registerTopic():
   user = request.args.get('name')
   password = request.args.get('password')
   topic = request.args.get('topic')

   usr = db.session.query(User).filter_by(name=user).first()
   if usr and usr.password == password:
      usr.topic = topic
      db.session.add(usr)
      db.session.commit()
      return "success"
   
   else:
      return "fail, bad user/password", status.HTTP_400_BAD_REQUEST

@main_views.route('/sendcommand', methods=['GET'])
@login_required
def sendcommand():
   command = request.args.get('command')
   val = request.args.get('val')
   topic = current_user.topic
   
   if command == 'on':
      current_status = redis_device_on.get(topic)
      
      # If no change is needed, return
      if str(current_status) == str(val):
         return "ok"
      
      # Subscribe to <topic>/on, publish command to device and wait on its redis status
      mqtt.subscribe(topic=topic+"/on")
      mqtt.publish(topic=topic, payload="0")

      timeout = time() + 3
      while redis_device_on.get(topic) == current_status and time()<timeout:
         pass
      
      mqtt.unsubscribe(topic=topic+"/on")
      if redis_device_on.get(topic) == current_status:
         return "offline", 400


      return redis_device_on.get(topic), 200
   
   return "poblem with command", 400
   
@main_views.route('/devicestatus', methods=['GET'])
@login_required
def devicestatus():
    topic = current_user.topic
    if not topic:
        return "No topic assigned to user", 400
    
    redis_device_on.set(topic, "pending")
    mqtt.subscribe(topic="{}/on".format(topic))
    mqtt.publish(topic=topic, payload="1")
    
    timeout = time() + 3
    while redis_device_on.get(topic) not in [b"on",b"off"] and time()<timeout:
        pass

    mqtt.unsubscribe(topic="{}/on".format(topic))
    if redis_device_on.get(topic) == "pending":
         return "offline", 400

    return redis_device_on.get(topic), 200
    
@main_views.route('/start')
def start():
   if current_user.is_authenticated:
      return str(current_user.password)
   return "You are not logged in!"
# @main_views.route('/')
# def hello_world():
#    student = Students.query.filter_by(name='miro').first()
#    return jsonify({"student":str(student)})
