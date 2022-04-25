from django.db import models

class Nguoidung(models.Model):
  id = models.AutoField(primary_key=True)
  taikhoan = models.CharField(max_length=50, unique=True, null=False)
  hoten = models.CharField(max_length=100, null=False)
  matkhau = models.CharField(max_length=30, null=False)
  diachi = models.CharField(max_length=300, null=False)
  ngaysinh = models.DateField(null=True)
  email = models.CharField(max_length=100, null=True)
  sodienthoai = models.CharField(max_length=11, null=False)
  vaitro = models.CharField(max_length=50, default='khachhang', null=False)

class Admin(models.Model):
  api_nguoidung = models.OneToOneField(Nguoidung,on_delete=models.CASCADE,primary_key=True)
  
class Khachhang(models.Model):
  api_nguoidung = models.OneToOneField(Nguoidung,on_delete=models.CASCADE,primary_key=True)

class Nhanvien(models.Model):
  api_nguoidung = models.OneToOneField(Nguoidung,on_delete=models.CASCADE,primary_key=True)
