from rest_framework import serializers
from ..models.Sach import Sach

class SachSerializer(serializers.ModelSerializer):
  hinhanh = serializers.CharField(required=False)
  tensach = serializers.CharField(required=True)
  mota = serializers.CharField(required=False)
  giasach = serializers.FloatField(required=True)
  soluong = serializers.IntegerField(required=True)
  namphathanh = serializers.IntegerField(required=False)
  api_tacgia = serializers.IntegerField(required=False)
  api_nhaxuatban = serializers.IntegerField(required=False)
  api_theloai = serializers.IntegerField(required=False)
  class Meta:
    model = Sach
    fields = ('__all__')