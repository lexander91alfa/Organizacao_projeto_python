all:
	@echo "Scripts para facilitar a vida"

install:
	@pip install -r requiriments_dev.txt

format:
	@blue cesar/*.py
	@blue tests/*.py
	@isort cesar/*.py
	@isort tests/*.py

lint:
	@blue --check cesar/*.py
	@blue --check tests/*.py
	@isort --check cesar/*.py
	@isort --check tests/*.py
	@prospector --no-autodetect cesar/*.py
	@prospector --no-autodetect tests/*.py

test:
	@pytest -V

sec:
	@pip-audit