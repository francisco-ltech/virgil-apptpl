
setup:
	conda create --name env 
	conda activate env 

install:
	pip install --upgrade pip &&\
	pip install --user -r requirements.txt

lint:
	python -m pip install flake8
	flake8 .

test:
	python -m pytest tests

api:
	python src/api/delta_endpoint.py

all: install lint test
