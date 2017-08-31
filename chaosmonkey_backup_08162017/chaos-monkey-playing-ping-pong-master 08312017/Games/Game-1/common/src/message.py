import pp_queue
import socket

MESSAGE_QUEUE = 'message'

messageConnection = 0
messageChannel = 0

def init ():
	global messageConnection
	global messageChannel

	messageConnection = pp_queue.connect()
	messageChannel = messageConnection.channel()
	messageChannel.queue_declare(queue=MESSAGE_QUEUE)

def send (message):
	hostname = socket.gethostname()
	print ("Sending message " + message + " from hostname " + hostname + 
		" to queue " + MESSAGE_QUEUE)

	m = hostname + ": " + message

	messageChannel.basic_publish(exchange='',
                      routing_key=MESSAGE_QUEUE,
                      body=m)


def close ():
	messageConnection.close()

