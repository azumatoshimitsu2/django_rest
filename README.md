docker-compose run web ./manage.py makemigrations
docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser
docker-compose run web ./manage.py collectstatic

docker-compose up -d

http://localhost:8000/api/sample/
http://localhost:8000/admin/

API ドキュメント
http://localhost:8000/api/docs/