.PHONY: up down build lint format shell

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

lint:
	docker-compose run --rm app lint

format:
	docker-compose run --rm app format

shell:
	docker-compose run --rm app /bin/bash