#!/bin/zsh
cd ..; source venv/bin/activate; cd first_django/
export $(xargs < dev.env) && python3 manage.py runserver