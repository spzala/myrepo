import pp_queue
import sys
import message
import os
import time
import redis

CACHE='cache-redis.ping-pong.svc.cluster.local'
#CACHE='localhost'


queue_name = os.environ['QUEUE_NAME']
other_queue = os.environ['OTHER_QUEUE_NAME']

key = queue_name

welcome_message = "I'm " +queue_name + " in Game-5"

red = 0

def throw_ball(ball):
	message.send ("Deleting key " + key)
	red.delete(key)

	message.send ("Throwing ball %s" % ball)

	channel.basic_publish(exchange='',
    	                  routing_key=other_queue,
        	              body=ball)

def callback(ch, method, properties, body):
	print ("Received a message %s" % body)
	sys.stdout.flush ()
	message.send ("I received a %s ball" % body)

	# Store in cache
	message.send ("Storing key " + key)
	red.set(key, body)

	# Sleep a second
	time.sleep(1)

	# Throw the ball
	throw_ball(body)

def initCache():
	print ("Initializing cache")
	global red
	red = redis.StrictRedis(host=CACHE, password='ping_pong')

def checkCache():
	value = red.get(key)
	if value is None:
		print ("Nothing in the cache")
		message.send ("Nothing found in the cache")
	else:
		# Cleans the cache
		print ("Found a lost ball %r " % value)
		message.send ("Found a lost ball %r " % value)

		throw_ball(value)

print(welcome_message)

# Init message
message.init ()

message.send (welcome_message)

# Init other queue
connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=other_queue)

# Init cache
initCache()

# Check cache
checkCache()

# Init queue
pp_queue.consume(queue_name, callback)

