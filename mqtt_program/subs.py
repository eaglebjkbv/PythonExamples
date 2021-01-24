import paho.mqtt.subscribe as subscribe


def on_message_print(client, userdata, message):
    print("Topic :%s  Mesaj: %s" % (message.topic, message.payload))


#subscribe.callback(on_message_print, "ev/odasicakligi",hostname="mqtt.eclipse.org")

subscribe.callback(on_message_print, "ev/odasicakligi",hostname="127.0.0.1")
