from django.db import models
from .Giohang import Giohang
from .Sach import Sach

class Sanphamtronggio(models.Model):
  id = models.AutoField(primary_key=True)
  api_giohang = models.ForeignKey(Giohang, on_delete=models.CASCADE)
  api_sach = models.ForeignKey(Sach, on_delete=models.CASCADE)
  soluong = models.IntegerField(null=False, default=1)
  class Meta:
    unique_together = (("api_giohang", "api_sach"),)