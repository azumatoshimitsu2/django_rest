from django.urls import path, include
from . import views as api_views
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    #すべてのアクション （⼀覧・詳細 ・登録・更新・⼀部更新・ 削除） をまとめて追加
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
] 

