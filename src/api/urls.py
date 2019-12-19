from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import views

router = routers.SimpleRouter()
router.register('sample', views.SampleViewSet)

urlpatterns = [
    #すべてのアクション （⼀覧・詳細 ・登録・更新・⼀部更新・ 削除） をまとめて追加
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
] 

if settings.DEBUG:
    urlpatterns += [path('docs/', include_docs_urls(title='API ドキュメント'))] 

