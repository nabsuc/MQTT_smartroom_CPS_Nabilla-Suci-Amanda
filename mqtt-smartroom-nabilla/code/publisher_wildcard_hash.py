import paho.mqtt.client as mqtt
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect("localhost", 1883, 60)
client.loop_start()

client.publish(
    "smartroom/room1/temperature",
    "Room 1 Temperature: 28 C"
)
print("Temperature sent")
time.sleep(1)

client.publish(
    "smartroom/room1/humidity",
    "Room 1 Humidity: 65 %"
)
print("Humidity sent")
time.sleep(1)

client.publish(
    "smartroom/room1/light",
    "Room 1 Light: Bright"
)
print("Light sent")
time.sleep(1)

client.publish(
    "smartroom/room2/temperature",
    "Room 2 Temperature: 30 C"
)
print("Room 2 temperature sent")

time.sleep(1)

client.loop_stop()
client.disconnect()