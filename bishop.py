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
    a=a.tolower()
    if a=='w':
        print "mqtt: Moving forward"
        fwd()   # Move forward

    if a=='w1':
        print "mqtt: Moving forward one revolution"
        enc_tgt(1,1,18)   # Move forward

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

client.connect("192.168.1.57", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


print "Basic example for the GoPiGo Robot control"

while True:

    print "Enter the Command:",

    a=raw_input()   # Fetch the input from the terminal
    a=a.tolower()

    if a=='w':

        fwd()   # Move forward

    elif a=='a':

        left()  # Turn left

    elif a=='d':

        right() # Turn Right

    elif a=='s':

        bwd()   # Move back

    elif a=='x':

        stop()  # Stop

    elif a=='z':

        print "Exiting"       # Exit

        sys.exit()

    else:

        print "Wrong Command, Please Enter Again"

    time.sleep(.1)