# Generated by Django 4.0.4 on 2022-04-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='taikhoan',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
