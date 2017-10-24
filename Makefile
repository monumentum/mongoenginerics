.PHONY: install lint


install:
	pip install -r requirements-dev.txt

lint:
	flake8