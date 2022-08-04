install:
	pipenv install

install-dev:
	pipenv install --dev

lint:
	pipenv run black .

test: 
	pipenv run coverage run --omit '*/virtualenvs/*' -m pytest

report: test
	pipenv run coverage report -m

export_python_env:
	export PYTHONWRITEBYTECODE=1
	export PYTHONUNBUFFERED=1

main: export_python_env
	pipenv run python main.py