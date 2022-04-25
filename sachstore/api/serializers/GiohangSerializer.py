from rest_framework import serializers
from ..models.Giohang import Giohang

class GiohangSerializer(serializers.ModelSerializer):
  api_khachhang = serializers.IntegerField(required=True)
  tongtien = serializers.FloatField(required=False)
  class Meta:
    model = Giohang
    fields = ('__all__')