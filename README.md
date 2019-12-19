docker-compose run web django-admin.py startproject mysite .

docker-compose run web ./manage.py makemigrations
docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser
docker-compose run web ./manage.py collectstatic

docker-compose up -d

mysite/settings.py
 STATIC_ROOT = '/static'

http://localhost:8000 

API ドキュメント
http://localhost:8000/api/docs/