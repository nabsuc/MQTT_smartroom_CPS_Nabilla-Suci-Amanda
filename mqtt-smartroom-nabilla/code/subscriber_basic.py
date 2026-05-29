import paho.mqtt.client as mqtt

# Fungsi saat berhasil connect ke broker
def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to broker")
    client.subscribe("smartroom/room1/temperature")

# Fungsi saat menerima pesan
def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}")
    print(f"Message: {msg.payload.decode()}")

# Membuat client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Menghubungkan callback
client.on_connect = on_connect
client.on_message = on_message

# Connect ke broker lokal
client.connect("localhost", 1883, 60)

# Menunggu pesan terus menerus
client.loop_forever()