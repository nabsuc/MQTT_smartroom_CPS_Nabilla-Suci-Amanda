import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to broker")

    client.subscribe("smartroom/room1/temperature")
    client.subscribe("smartroom/room1/humidity")
    client.subscribe("smartroom/room1/light")

    print("Subscribed to multiple topics")

def on_message(client, userdata, msg):
    print("--------------------")
    print(f"Topic   : {msg.topic}")
    print(f"Message : {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()