FROM python:3.5

RUN pip install flask
RUN pip install oauth2client

ENV FLASK_APP=server.py

RUN mkdir /web
WORKDIR /web

CMD flask run -h 0.0.0.0
