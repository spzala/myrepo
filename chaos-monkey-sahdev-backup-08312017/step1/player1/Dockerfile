FROM python:latest

WORKDIR /usr/src/app

EXPOSE 32340
RUN pip install flask
RUN pip install openpyxl
RUN pip install pika
RUN pip install python-rest-client
RUN pip install requests
COPY src/ /usr/src/app

CMD ["python", "start_game.py"]
