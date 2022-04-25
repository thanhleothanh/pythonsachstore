from rest_framework import serializers
from ..models.Nguoidung import Nguoidung

class NguoidungSerializer(serializers.ModelSerializer):
  taikhoan = serializers.CharField(max_length=50, required=True)
  hoten = serializers.CharField(max_length=100, required=True)
  matkhau = serializers.CharField(max_length=30, required=True)
  diachi = serializers.CharField(max_length=300, required=False)
  ngaysinh = serializers.CharField(max_length=100, required=False)
  email = serializers.CharField(max_length=200, required=False)
  sodienthoai = serializers.CharField(max_length=200, required=False)
  vaitro = serializers.CharField(max_length=200, required=False)
  class Meta:
    model = Nguoidung
    fields = ('__all__')