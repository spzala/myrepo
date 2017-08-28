from openpyxl import load_workbook
from flask import Flask
import json
import pika
import os
import threading
import requests
import sys

app = Flask(__name__)

channel_name = "ping"

base_url = "http://stock_price:8080/stockPrice/"

set_url = "http://stock_table_set:8080/"

def bounceBall(js):
	print ("Bouncing ball %s" % js)

def callback(ch, method, properties, body):
	symbol = str(body, 'utf-8')
	url = base_url + symbol
	print("Received ball %r" % body)
	resp = requests.get(url)
	status = resp.status_code
	if status == 200 or status == 304:
		print('status code: ', status)
		js = resp.json()
		print("Received response %r" % js)
		bounceBall(js)
	else:
		print('Error status code: ', status)
	sys.stdout.flush()

def consume():
	print('Consuming balls')
	host = os.getenv('QUEUE_HOST', 'localhost')
	print(host)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
	channel = connection.channel()

	channel.queue_declare(queue=channel_name)

	channel.basic_consume(callback,
    	                  queue=channel_name,
        	              no_ack=True)
	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()


def consumeBalls():
	print("Starting a thread")
	t = threading.Thread(target=consume)
	t.start()

@app.route("/process")
def processBalls():
	consumeBalls()
	return 'process'

@app.route('/')
def index():
    return 'Index Page'

print ("Welcome to Ping Pong")
if __name__ == '__main__':
    app.run(host='0.0.0.0')

