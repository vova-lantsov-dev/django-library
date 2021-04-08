FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ARG PASS
ENV DJANGO_SUPERUSER_PASSWORD=${PASS}
RUN python manage.py migrate --noinput && \
    python manage.py createsuperuser --username admin --email contact@vova-lantsov.dev --noinput