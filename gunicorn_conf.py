command = '/home/username/agrement/venv/bin/gunicorn'
pythonpath = '/home/username/agrement'
bind = '0.0.0.0:8100'
workers = 3
user = 'username'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=contract.settings'
