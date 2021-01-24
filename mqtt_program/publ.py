import paho.mqtt.publish as publish

#publish.single("ev/odasicakligi", "Bedava messenger",hostname="mqtt.eclipse.org")

publish.single("ev/odasicakligi", "Bedava messenger",hostname="127.0.0.1")
