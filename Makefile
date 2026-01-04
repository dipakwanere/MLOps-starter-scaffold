install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

test:
	pytest tests/ --cov=src/ --cov-report=term-missing --verbose

format:
	black . *.py

all: install lint test format