from django.db import models

class Theloai(models.Model):
  id = models.AutoField(primary_key=True)
  tentheloai = models.CharField(max_length=200, null=False)

