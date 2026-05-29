import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)
client.loop_start()

# Temperature
client.publish(
    "smartroom/room1/temperature",
    "28 C"
)
print("Temperature sent")
time.sleep(1)

# Humidity
client.publish(
    "smartroom/room1/humidity",
    "65 %"
)
print("Humidity sent")
time.sleep(1)

# Light
client.publish(
    "smartroom/room1/light",
    "Bright"
)
print("Light sent")

time.sleep(1)

client.loop_stop()
client.disconnect()