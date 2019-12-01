from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(views.APIView):
    """
    本モデルの取得（⼀覧） ・登録API クラス
    """
    def get(self, request, * args, ** kwargs):
        """
        本モデルの取得（⼀覧） API に対応するハンドラメソッド
        """
        #モデルオブジェクトの⼀ 覧を取得
        book_list = Book.objects.all()# シリアライザオブジェクトを作成
        serializer = BookSerializer(instance = book_list, many = True)# レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request, * args, ** kwargs):
        """
        本モデルの登録API に対応するハンドラメソッド
        """
        #シリアライザオブジェクトを作成
        serializer = BookSerializer(data = request.data)# バリデーション
        serializer.is_valid(raise_exception = True)# モデルオブジェクトを登録
        serializer.save()# レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_201_CREATED)

class BookRetrieveUpdateDestroyAPIView(views.APIView):
    """
    本モデルの取得（詳細） ・更新・⼀部更新・削除API クラス
    """
    def get(self, request, pk, * args, ** kwargs):
        """
        本モデルの取得（詳細） API に対応するハンドラメソッド
        """
        #モデルオブジェクトを取得
        book = get_object_or_404(Book, pk = pk)

        #シリアライザオブジェクトを作成 
        serializer = BookSerializer(instance=book) 
        #レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        """
        本モデルの更新API に対応するハンドラメソッド
        """
        #モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)  #シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)  
        #バリデーション
        serializer.is_valid(raise_exception=True)  #モデルオブジェクトを更新
        serializer.save()  
        #レスポンスオブジェクトを返す  
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request, pk, *args, **kwargs):
        """本モデルの⼀部更新API に対応するハンドラメソッド""" 
        #モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)  #シリアライザオブジェクトを作成  serializer = BookSerializer(instance=book, data=request.data, partial=True)  #バリデーション  serializer.is_valid(raise_exception=True)  #モデルオブジェクトを⼀部更新  serializer.save()  #レスポンスオブジェクトを返す  return Response(serializer.data, status.HTTP_200_OK)  def delete(self, request, pk, *args, **kwargs):  """本モデルの削除API に対応するハンドラメソッド"""  #モデルオブジェクトを取得  book = get_object_or_404(Book, pk=pk)  #モデルオブジェクトを削除  book.delete()  #レスポンスオブジェクトを返す  return Response(status=status.HTTP_204_NO_CONTENT) 

