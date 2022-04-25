from django.db import models
from .Donhang import Donhang
from .Sach import Sach

class Sanphamdadat(models.Model):
  id = models.AutoField(primary_key=True)
  api_donhang = models.ForeignKey(Donhang, on_delete=models.CASCADE)
  api_sach = models.ForeignKey(Sach, on_delete=models.SET_NULL, null=True)
  soluong = models.IntegerField(null=False, default=1)
  giaban = models.FloatField(null=False)
  class Meta:
    unique_together = (("api_donhang", "api_sach"),)