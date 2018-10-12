# -*- coding: utf-8 -*-
"""
Created on October 8, 2018


@author: Eduardo

"""
import paho.mqtt.client as mqtt

_client = None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def initialize_comm(server):
    global _client
    _client = mqtt.Client()
    _client.connect(server)
    _client.on_connect = on_connect
    _client.loop_start()

def send(topic, message):
    if _client is not None:
        _client.publish(topic, payload=message, qos=0) 
