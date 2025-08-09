# Dockerfile (Multi-stage)
# --- مرحله توسعه ---
FROM python:3.12-slim as dev

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install black flake8 mypy  # ابزارهای کیفیت کد

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# --- مرحله تولید ---
# FROM python:3.12-slim as prod
# WORKDIR /app
# COPY --from=dev /app /app
# COPY --from=dev /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_api.wsgi"]