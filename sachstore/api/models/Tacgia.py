from django.db import models

class Tacgia(models.Model):
  id = models.AutoField(primary_key=True)
  tentacgia = models.CharField(max_length=200, null=False)
  diachi = models.CharField(max_length=500, null=True)
  namsinh = models.IntegerField(null=True)

