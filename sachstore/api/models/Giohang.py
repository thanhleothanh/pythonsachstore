from django.db import models

from .Nguoidung import Khachhang

class Giohang(models.Model):
  id = models.AutoField(primary_key=True)
  api_khachhang = models.OneToOneField(Khachhang,on_delete=models.CASCADE)
  tongtien = models.FloatField(null=True, default=0)


