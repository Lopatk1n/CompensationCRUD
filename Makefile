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

run:
	uvicorn src.app.main:app --reload