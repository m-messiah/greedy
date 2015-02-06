.PHONY: maketrans compiletrans migrate

maketrans:
	PATH=/usr/local/opt/gettext/bin/:$(PATH) ./manage.py makemessages -a

compiletrans:
	PATH=/usr/local/opt/gettext/bin/:$(PATH) ./manage.py compilemessages

migrate:
	./manage.py makemigrations
	./manage.py migrate

