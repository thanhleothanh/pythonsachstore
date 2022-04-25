# pythonsachstore

Cài đặt cấu hình local mysql database trong settings.py (đoạn dưới đây)
Điền vào các fields (--tendatabase--, --taikhoan--, --matkhau--)
Cứ tạo 1 database mới rồi điền tên vào --tendatabase--

import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': '--tendatabase--',
'USER': '--taikhoan--',
'PASSWORD': '--matkhau--',
'HOST': 'localhost',
'PORT': '3306',
}
}

Tạo virtualenv rồi pip install các packages trong env đấy, chạy project trong env đấy!

packages cần thiết trong requirements.txt
