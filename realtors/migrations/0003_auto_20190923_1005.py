# Generated by Django 2.2.5 on 2019-09-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_remove_realtor_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]