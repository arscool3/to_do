docker build --tag python-django-3 .

docker run --publish 8000:8000 python-django-3
