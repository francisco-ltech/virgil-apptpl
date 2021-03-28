
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
	make build_utilities 
	make install_utilities
	python -m pytest tests

unit_test:
	make build_utilities 
	make install_utilities
	python -m pytest tests/unit

api:
	python src/api/delta_endpoint.py

build_utilities:
	python .\src\utilities\setup.py develop

install_utilities:
	pip install .\src\utilities\

databricks_deploy_dev:
	make test
	dbfs --profile my_app rm dbfs:/virgil/utilities/utilities-0.1.0-py2.py3-none-any.whl
	dbfs --profile my_app cp .\src\utilities\dist\utilities-0.1.0-py2.py3-none-any.whl dbfs:/virgil/utilities/utilities-0.1.0-py2.py3-none-any.whl
	databricks workspace --profile my_app import_dir -o .\src\jobs\ /Users/`git config user.email | awk '{print tolower($0)}'`/src/jobs

databricks_deploy:
	make test
	dbfs --profile my_app rm dbfs:/virgil/utilities/utilities-0.1.0-py2.py3-none-any.whl
	dbfs --profile my_app cp .\src\utilities\dist\utilities-0.1.0-py2.py3-none-any.whl dbfs:/virgil/utilities/utilities-0.1.0-py2.py3-none-any.whl
	databricks workspace --profile my_app import_dir -o .\src\jobs\ /src/jobs/
	databricks libraries install --profile my_app --cluster-id 0313-200944-fin685 --whl dbfs:/virgil/utilities/utilities-0.1.0-py2.py3-none-any.whl
	

all: install lint test
