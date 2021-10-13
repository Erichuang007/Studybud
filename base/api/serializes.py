# 把一个python对象转变成一个json对象才能在views 里作为response参数 return
from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'