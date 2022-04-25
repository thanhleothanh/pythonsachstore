from django.db import models

class Thongtinthanhtoan(models.Model):
  id = models.AutoField(primary_key=True)
  thoigianthanhtoan = models.DateTimeField(auto_now_add=True, blank=True)