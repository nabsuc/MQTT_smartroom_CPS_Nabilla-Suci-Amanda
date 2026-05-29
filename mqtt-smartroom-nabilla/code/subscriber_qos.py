import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to broker")
    client.subscribe("smartroom/room1/qos", qos=2)
    print("Subscribed to topic: smartroom/room1/qos")

def on_message(client, userdata, msg):
    print("--------------------")
    print(f"Topic   : {msg.topic}")
    print(f"QoS     : {msg.qos}")
    print(f"Message : {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()