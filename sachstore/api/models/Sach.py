from django.db import models
from .Tacgia import Tacgia
from .Theloai import Theloai
from .Nhaxuatban import Nhaxuatban

class Sach(models.Model):
  id = models.AutoField(primary_key=True)
  hinhanh = models.CharField(max_length=1000, null=True)
  mota = models.CharField(max_length=5000, null=True)
  tensach = models.CharField(max_length=200, null=False)
  giasach = models.FloatField(null=False)
  namphathanh = models.IntegerField(null=True)
  soluong = models.IntegerField(null=False, default=0)
  api_tacgia = models.ForeignKey(Tacgia,on_delete=models.SET_NULL, null=True)
  api_theloai = models.ForeignKey(Theloai,on_delete=models.SET_NULL, null=True)
  api_nhaxuatban = models.ForeignKey(Nhaxuatban,on_delete=models.SET_NULL, null=True)


