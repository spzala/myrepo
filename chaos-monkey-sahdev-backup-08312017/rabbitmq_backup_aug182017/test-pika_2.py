#!/usr/bin/env python
import pika

# this queue is the destination queue
credentials = pika.PlainCredentials('admin', 'secretpassword')
parameters = pika.ConnectionParameters('127.0.0.1')
connection = pika.BlockingConnection(parameters)
print " connection created"
