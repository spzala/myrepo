FROM python:latest

WORKDIR /usr/src/app

RUN pip install pika

COPY src/ /usr/src/app

CMD ./startgame.sh && echo hello && sleep 600
