from django.db import models

class Nhaxuatban(models.Model):
  id = models.AutoField(primary_key=True)
  tennhaxuatban = models.CharField(max_length=200, null=False)

