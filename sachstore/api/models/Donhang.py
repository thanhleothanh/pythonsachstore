from django.db import models

from .Nguoidung import Khachhang
from .Thongtinthanhtoan import Thongtinthanhtoan

class Donhang(models.Model):
  id = models.AutoField(primary_key=True)
  api_khachhang = models.ForeignKey(Khachhang, on_delete=models.SET_NULL, null=True)
  diachi = models.CharField(max_length=300, null=False)
  sodienthoai = models.CharField(max_length=11, null=False)
  hoten = models.CharField(max_length=200, null=False)
  ngaydat = models.DateTimeField(auto_now_add=True, blank=True)
  tongtien = models.FloatField(null=False)
  isThanhtoan = models.BooleanField(null=False, default=False)
  isHoanthanh = models.BooleanField(null=False, default=False)
  thongtinthanhtoan = models.OneToOneField(Thongtinthanhtoan, on_delete=models.SET_NULL, null=True)