release: python mysite/manage.py migrate
release: python mysite/manage.py makemigrations
web: gunicorn --chdir mysite mysite.wsgi