#!/bin/bash
source /home/username/agrement/venv/bin/activate
exec gunicorn -c "/home/username/agrement/gunicorn_conf.py" contract.wsgi
