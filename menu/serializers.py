# movie_api/movies/serializers.py

from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu # 모델 설정
        fields = ('item','price','temp','size','sajin') # 필드 설정