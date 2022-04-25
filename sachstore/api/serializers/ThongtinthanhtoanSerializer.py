from rest_framework import serializers
from ..models.Thongtinthanhtoan import Thongtinthanhtoan

class ThongtinthanhtoanSerializer(serializers.ModelSerializer):
  thoidiemthanhtoan = serializers.DateField(required=False)
  class Meta:
    model = Thongtinthanhtoan
    fields = ('__all__')