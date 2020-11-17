最初の起動
docker-compose up -d --build
docker-compose run web django-admin.py startproject api .

docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser --username admin --email admin@localhost

docker exec -it nuxt /bin/bash
yarn create nuxt-app front
exit

./nuxt/front/nuxt.config.js
に↓を追加
  server: {
    port: 3000,
    host: '0.0.0.0',  
  },

docker-compose.yml
の↓のコメントアウトを解除
# command: >
#   bash -c 'cd front &&
#   yarn dev'

docker-compose down
docker-compose run web ./manage.py collectstatic
docker-compose up -d --build
