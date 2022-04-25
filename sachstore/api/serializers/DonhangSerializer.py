from rest_framework import serializers
from ..models.Donhang import Donhang

class DonhangSerializer(serializers.ModelSerializer):
  api_khachhang = serializers.IntegerField(required=False)
  diachi = serializers.CharField(max_length=300, required=True)
  sodienthoai = serializers.CharField(max_length=11, required=True)
  hoten = serializers.CharField(max_length=200, required=True)
  ngaydat = serializers.DateField(required=False)
  tongtien = serializers.FloatField(required=True)
  isThanhtoan = serializers.BooleanField(required=False)
  isHoanthanh = serializers.BooleanField(required=False)
  thongtinthanhtoan = serializers.IntegerField(required=False)
  class Meta:
    model = Donhang
    fields = ('__all__')