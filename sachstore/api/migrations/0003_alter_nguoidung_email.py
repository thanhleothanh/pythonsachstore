# Generated by Django 4.0.4 on 2022-04-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_nguoidung_taikhoan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]