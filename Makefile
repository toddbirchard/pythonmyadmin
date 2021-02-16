SRCPATH := $(shell pwd)
PROJECTNAME := $(shell basename $(CURDIR))
ENTRYPOINT := $(PROJECTNAME).ini

define HELP
Manage $(PROJECTNAME). Usage:

make run        - Run $(PROJECTNAME).
make restart    - Purge cache & reinstall modules.
make deploy     - Pull latest build and deploy to production.
make update     - Update pip dependencies via Python Poetry.
make format     - Format code with Python's `Black` library.
make lint       - Check code formatting with flake8
make clean      - Remove cached files and lock files.
endef
export HELP


.PHONY: run restart deploy update format lint clean help

requirements: .requirements.txt
env: .venv/bin/activate


.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)


all help:
	@echo "$$HELP"


.PHONY: run
run: env
	service $(PROJECTNAME) start


.PHONY: restart
restart: env
	service $(PROJECTNAME) stop
	make clean
	service $(PROJECTNAME) start
	service $(PROJECTNAME) status


.PHONY: deploy
deploy:
	make clean
	$(shell . ./deploy.sh)


.PHONY: update
update: deploy
	.venv/bin/python3 -m pip install -U pip
	poetry update
	poetry export -f requirements.txt --output requirements.txt --without-hashes


.PHONY: format
format: env
	$(shell . .venv/bin/activate && isort ./)
	$(shell . .venv/bin/activate && black ./)


.PHONY: lint
lint:
	flake8 ./app --count --select=E9,F63,F7,F82 --show-source --statistics


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'poetry.lock' -delete
	find . -name 'Pipefile.lock' -delete
	find . -name 'logs/*' -delete
	find . -name '.pytest_cache' -delete
	find . -name '.webassets-cache/*' -delete
	find . -name 'pythonmyadmin/static/.webassets-cache/*' -delete
	rm -rf pythonmyadmin/static/.webassets-cache