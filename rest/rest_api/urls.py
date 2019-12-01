from django.urls import path
from rest_api import views as api_views

urlpatterns = [
    #本モデルの取得（⼀覧） ・登録  
    path('rest_api/books/', api_views.BookListCreateAPIView.as_view()),
    #本モデルの取得（詳細） ・更新・⼀部更新・削除
    path('rest_api/books/<pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    ] 
