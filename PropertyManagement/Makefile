
#work
virtualenv:
	virtualenv venv
	
requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	pytest -vvv

uninstall:
	pip uninstall -r requirements.txt

all:
	install lint test format





