from django.urls import path
from . import views as api_views

urlpatterns = [
    #本モデルの取得（⼀覧） ・登録  
    # path('books/', api_views.BookListCreateAPIView),
    #本モデルの取得（詳細） ・更新・⼀部更新・削除
    #path('books/<pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    ] 

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    #すべてのアクション （⼀覧・詳細 ・登録・更新・⼀部更新・ 削除） をまとめて追加
    path('api/', include(router.urls)),
] 

