FROM python:3.8-slim

WORKDIR /api-flask

COPY resources/ util/ application.py requirements.txt /api-flask/
COPY resources/ /api-flask/resources/
COPY util/ /api-flask/util/
COPY application.py requirements.txt  /api-flask/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "gunicorn application:app -b 0.0.0.0:$APPPORT -w 2"]
