# Generated by Django 2.0.4 on 2018-05-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180507_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner_photo',
            field=models.ImageField(upload_to='static/media', verbose_name='Image'),
        ),
    ]
