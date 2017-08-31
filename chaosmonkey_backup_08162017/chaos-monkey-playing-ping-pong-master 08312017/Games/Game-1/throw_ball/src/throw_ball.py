import pp_queue
import message

QUEUE = 'ping'
BALL = 'white-0'

message.init ()

connection = pp_queue.connect()
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

message.send ("Throwing ball " + BALL)

channel.basic_publish(exchange='',
                      routing_key=QUEUE,
                      body=BALL)

print("Ball thrown")
message.close()
connection.close()