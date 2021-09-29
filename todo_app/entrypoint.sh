#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=development

gunicorn --bind 0.0.0.0:$PORT --chdir /srv/www/todo_app/ app:app
