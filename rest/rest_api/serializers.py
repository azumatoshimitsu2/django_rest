from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    本モデル⽤シリアライザ
    """
    class Meta: #対象のモデルクラスを指定
        model = Book# 利⽤ しないモデルのフィールドを指定
        exclude = ['created_at']