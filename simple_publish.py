import paho.mqtt.client as mqtt
import random
import time
from datetime import date, datetime
import json

client=mqtt.Client("temperature")
client.connect("broker.hivemq.com", 1883)

while True:
  #Temperature sensor
  Temperature=random.randint(5,30)
  status=True #it will tell us if the sensor is On or Off
  day=date.today()    #date function call
  clock=datetime.now()  #time function calls
  time_time=datetime.time(clock)    #exact time step
  data=[Temperature,status,str(day),str(time_time)]    #store all data into
  data_encoded=json.dumps(data)    #encode array 'data' into json data format
  client.publish("cartrax/temperature_sensor/data", data_encoded)  #publish data

  #pirint message with data, time and date to check if it is published
  print("Just published: id- " + str(Temperature) + "; status- " +str(status), \
        "  to topic: 'cartrax/temperature_sensor/data' \n")
  time.sleep(3) #publish new entry between 3 and 10 seconds