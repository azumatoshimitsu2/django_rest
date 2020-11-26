最初の起動（Nuxt のアプリをつくっていない場合）
docker-compose up -d db
docker-compose up -d --build
docker-compose run web django-admin.py startproject mysite .

docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser --username admin --email admin@localhost

docker exec -it nuxt /bin/bash
yarn create nuxt-app front
//インタラクティブなアプリの設定が始まるので設定
exit

./nuxt/front/nuxt.config.js
に↓を追加
  server: {
    port: 3000,
    host: '0.0.0.0',  
  },

docker-compose.yml
の↓のコメントアウト2箇所を解除
# command: >
#   /bin/bash -c 'cd front && yarn dev'

#- front

./django/api/settings.py
ALLOWED_HOSTS = []
↓に下記変え
ALLOWED_HOSTS = ["localhost","django"]

↓一番下に追加
STATIC_URL = '/static/'
STATIC_ROOT = '/static'

# 許可するオリジン
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]
# レスポンスを公開する
CORS_ALLOW_CREDENTIALS = True

docker-compose down
docker-compose run web ./manage.py collectstatic
docker-compose up -d --build


最初の起動（Nuxt のアプリが既にある場合）
docker-compose up -d db
docker-compose up -d --build
docker-compose run web django-admin.py startproject mysite .

docker-compose run web ./manage.py migrate
docker-compose run web ./manage.py createsuperuser --username admin --email admin@localhost

//処理に時間がかかって止まるのでインストールは事前に行う
docker-compose run web /bin/bash -c 'cd front && yarn install'

docker-compose down
docker-compose run web ./manage.py collectstatic
docker-compose up -d --build