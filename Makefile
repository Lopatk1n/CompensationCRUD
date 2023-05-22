mypy:
	python -m mypy src/ --ignore-missing-imports

ruff:
	ruff check src

black:
	black src --check

check: mypy ruff black

style:
	black src
	isort src

hooks:
	pre-commit install -t pre-commit

setup:
	sudo chown -R $(whoami) .

build:
	sudo docker compose up -d --build --force-recreate

migrate-from-csv:
	sudo docker compose exec backend python app/migrate_script.py
