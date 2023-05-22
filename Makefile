check:
	mypy src --strict
	ruff check src
	black src --check

style:
	black src