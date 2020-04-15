FROM python:3.7

RUN pip install Flask gunicorn
RUN pip install mysql-connector-python

WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --blind :$PORT --workers 1 --threads 8 app:app