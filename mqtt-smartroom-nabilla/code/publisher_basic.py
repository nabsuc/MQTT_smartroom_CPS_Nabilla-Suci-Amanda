import paho.mqtt.client as mqtt
import time

# Membuat client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Connect ke broker
client.connect("localhost", 1883, 60)

# Data yang akan dikirim
temperature = "27 C"

# Publish pesan
client.publish(
    "smartroom/room1/temperature",
    temperature
)

print("Message sent:", temperature)

# Delay kecil agar publish selesai
time.sleep(1)

# Disconnect
client.disconnect()