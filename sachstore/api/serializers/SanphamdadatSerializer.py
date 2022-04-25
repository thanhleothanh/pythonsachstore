from rest_framework import serializers
from ..models.Sanphamdadat import Sanphamdadat

class SanphamdadatSerializer(serializers.ModelSerializer):
  api_sach = serializers.IntegerField(required=True)
  api_donhang = serializers.IntegerField(required=False)
  soluong = serializers.IntegerField(required=True)
  giaban = serializers.FloatField(required=True)
  class Meta:
    model = Sanphamdadat
    fields = ('__all__')