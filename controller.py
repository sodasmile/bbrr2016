import sys  #Used for closing the running program
import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("bishop", 1883, 60)

topic="bishop"

while True:

    print "Enter the Command:",

    a=raw_input()   # Fetch the input from the terminal

    client.publish(topic, payload=a, qos=0, retain=False)

    if a=='w':
        print "mqtt: Moving forward"
    if a=='w1':
        print "mqtt: Moving forward one revolution"
    elif a=='a':
        print "mqtt: Turning left"
    elif a=='d':
        print "mqtt: Turning right"
    elif a=='s':
        print "mqtt: Moving backwards"
    elif a=='x':
        print "mqtt: Stopping"
    elif a=='z':
        print "Exiting"       # Exit
        sys.exit()
    else:
        print "Wrong Command, Please Enter Again"

    time.sleep(.1)