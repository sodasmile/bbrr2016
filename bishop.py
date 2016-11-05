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
    led_off(LED_L)
    led_off(LED_R)
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
        print "increase speed" + "success" if result==1 else "FAILED"

    if a=='-':
        print "mqtt: Decreasing speed by 10."
        enable_encoders()  # Enable wheel rotation sensor
        result=decrease_speed()
        print "decrease speed" + "success" if result==1 else "FAILED"

    elif a=='a':
        print "mqtt: Turning left"
        led_on(LED_L)
        left()  # Turn left

    elif a=='d':
        print "mqtt: Turning right"
        led_on(LED_R)
        right() # Turn Right

    elif a=='s':
        print "mqtt: Moving backwards"
        bwd()   # Move back

    elif a=='x':
        print "mqtt: Stopping"
        stop()  # Stop

    elif a=='ver':
        print "mqtt: Version"
        print "---------------------------\n|",
        ver=fw_ver()
        if ver==-1:
            print "| GoPiGo Not Found"
            print "---------------------------"
            exit()
        print "GoPiGo Found"
        print "| Firmware version:",ver
        print "| Battery voltage :",volt(),"V"
        print "---------------------------"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()