FROM python:3.8.9-alpine3.13
WORKDIR root/first_django
COPY my_app root/first_django/my_app
COPY my_polls root/first_django/my_polls
COPY templates root/first_django/templates
COPY manage.py root/first_django/manage.py
COPY wait-for-it.sh root/first_django/wait-for-it.sh

COPY requirements.txt root/first_django/requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && apk add bash
RUN chmod +x root/first_django/wait-for-it.sh && pip install -r root/first_django/requirements.txt