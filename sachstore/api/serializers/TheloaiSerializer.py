from rest_framework import serializers
from ..models.Theloai import Theloai

class TheloaiSerializer(serializers.ModelSerializer):
  tentheloai = serializers.CharField(max_length=200, required=True)
  class Meta:
    model = Theloai
    fields = ('__all__')