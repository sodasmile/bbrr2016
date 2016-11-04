import sys  #Used for closing the running program
import paho.mqtt.client as mqtt
from gopigo import *    #Has the basic functions for controlling the GoPiGo Robot

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("bishop/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    a=msg.payload
    if a=='w':
        print "mqtt: Moving forward"
        fwd()   # Move forward

    if a=='w1':
        print "mqtt: Moving forward one revolution"
        enable_encoders()  # Enable wheel rotation sensor
        result=enc_tgt(1,1,18)   # Move forward

    if a=='+':
        print "mqtt: Increasing speed by 10."
        enable_encoders()  # Enable wheel rotation sensor
        result=increase_speed()
        print "increase speed" + result==1 ? "success" : "FAILED"

    if a=='-':
        print "mqtt: Decreasing speed by 10."
        enable_encoders()  # Enable wheel rotation sensor
        result=decrease_speed()
        print "decrease speed" + result==1 ? "success" : "FAILED"

    elif a=='a':
        print "mqtt: Turning left"
        left()  # Turn left

    elif a=='d':
        print "mqtt: Turning right"
        right() # Turn Right

    elif a=='s':
        print "mqtt: Moving backwards"
        bwd()   # Move back

    elif a=='x':
        print "mqtt: Stopping"
        stop()  # Stop


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()