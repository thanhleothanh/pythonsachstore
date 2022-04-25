from rest_framework import serializers
from ..models.Sanphamtronggio import Sanphamtronggio

class SanphamtronggioSerializer(serializers.ModelSerializer):
  api_sach = serializers.IntegerField(required=True)
  soluong = serializers.IntegerField(required=True)
  class Meta:
    model = Sanphamtronggio
    fields = ('api_sach', 'soluong')