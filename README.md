# python-dev-env
This is simple Python development environment that uses Flask, Flake8 and Black with hot-reload functionality built in Docker container

# Prerequisites
Install Docker

# Starting container
Build container with `docker compose build`
Start container with `docker compose up`

To run linting `docker compose run --rm app lint`
To format code `docker compose run --rm app format`

Test that the project is running by going to <http://localhost:5000>, if you see `Hello from Docker Compose!` in your browser, than it's running.
