mypy:
	mypy src --strict

ruff:
	ruff check src

black:
	black src --check

check: mypy ruff black

style:
	black src

hooks:
	pre-commit install -t pre-commit

setup:
	sudo chown -R $(whoami) .

run:
	uvicorn src.app.main:app --reload

build:
	sudo docker build -t app .
