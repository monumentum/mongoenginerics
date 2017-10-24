.PHONY: install lint test


install:
	pip install -r requirements-dev.txt

lint:
	flake8

test:
	coverage run --source=mongoenginerics -m unittest discover -s tests/