# Generated by Django 4.0.4 on 2022-04-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_tacgia_namsinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='namphathanh',
            field=models.IntegerField(),
        ),
    ]
