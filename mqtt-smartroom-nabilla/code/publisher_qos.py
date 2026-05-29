import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)
client.loop_start()

msg0 = client.publish("smartroom/room1/qos", "Temperature 27 C - QoS 0", qos=0)
msg0.wait_for_publish()
print("Sent QoS 0")

msg1 = client.publish("smartroom/room1/qos", "Temperature 27 C - QoS 1", qos=1)
msg1.wait_for_publish()
print("Sent QoS 1")

msg2 = client.publish("smartroom/room1/qos", "Temperature 27 C - QoS 2", qos=2)
msg2.wait_for_publish()
print("Sent QoS 2")

client.loop_stop()
client.disconnect()