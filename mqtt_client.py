import paho.mqtt.client as paho
import time
import serial
import matplotlib.pyplot as plt
import numpy as np

mqttc = paho.Client()
n = 0
X = []
Y = []
Z = []
t = []

start = time.time()
# Settings for connection
# TODO: revise host to your ip
host = "192.168.43.31"
topic = "Mbed"

# Callbacks
def on_connect(self, mosq, obj, rc):
      print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
      print(str(msg.payload))
      x = float(msg.payload[0:7])
      y = float(msg.payload[8:15])
      z = float(msg.payload[16:23])
      c = time.time() - start
      
      X.append(x)
      Y.append(y)
      Z.append(z)
      t.append(c)
      
      if (c >= 23):
            plt.plot(t, X, label="x-acc")
            plt.plot(t, Y, label="y-acc")
            plt.plot(t, Z, label="z-acc")
            plt.ylabel("acc value")
            plt.xlabel("timestamp")
            plt.title('Acceleration Plot')
            plt.legend(loc='upper right')
            plt.show() 
            mqttc.disconnect
      

def on_subscribe(mosq, obj, mid, granted_qos):
      print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
      print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

# Publish messages from Python
num = 0
"""while num != 5:
      ret = mqttc.publish(topic, "Message from Python!\n", qos=0)
      if (ret[0] != 0):
            print("Publish failed")
      mqttc.loop()
      time.sleep(1.5)
      num += 1"""

# Loop forever, receiving messages
mqttc.loop_forever()