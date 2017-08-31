import pp_queue
import sys
import message
import os
import time

queue_name = os.environ['QUEUE_NAME']
other_queue = os.environ['OTHER_QUEUE_NAME']

def throw_ball(ball):
	message.send ("Throwing ball %s" % ball)

	channel.basic_publish(exchange='',
    	                  routing_key=other_queue,
        	              body=ball)

def transformBall(body):
	ball = body.decode('utf-8')
	name, count = ball.split("-", 1)
	count += 1
	return name + "-" + count

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	message.send ("I received a %s ball" % body)
	ball = transformBall(body)
	sys.stdout.flush ()
	time.sleep(1)
	throw_ball(body)

print("I'm " + queue_name)

# Init message
message.init ()

message.send ("Hello. I am " + queue_name)

# Init other queue

connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=other_queue)


# Init queue
pp_queue.consume(queue_name, callback)

