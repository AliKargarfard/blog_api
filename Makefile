# ---- Constants ----
PROJECT_NAME = blog_api

# Makefile (سازگار با ویندوز)
init:
	docker-compose up -d --build

migrate:
	docker-compose exec web python manage.py migrate  # `winpty` برای ویندوز ضروری است

test:
	docker-compose exec web python manage.py test


# ---- Docker ----
# up:
# 	docker-compose up -d --build

down:
	docker-compose down

# ---- Django ----
# migrate:
# 	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

# ---- Testing ----
# test:
# 	docker-compose exec web pytest -xvs .

test-coverage:
	docker-compose exec web pytest --cov=. --cov-report html

# ---- Code Quality ----
lint:
	docker-compose exec web flake8 .
	docker-compose exec web black --check .
	docker-compose exec web mypy .

format:
	docker-compose exec web black .
	docker-compose exec web isort .

# ---- Utils ----
shell:
	docker-compose exec web python manage.py shell_plus --ipython

logs:
	docker-compose logs -f web