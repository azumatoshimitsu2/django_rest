from rest_framework import serializers
from .models import Sample

class SampleSerializer(serializers.ModelSerializer):
    """
    本モデル⽤シリアライザ
    """
    class Meta: #対象のモデルクラスを指定
        model = Sample# 利⽤ しないモデルのフィールドを指定
        exclude = ['created_at']