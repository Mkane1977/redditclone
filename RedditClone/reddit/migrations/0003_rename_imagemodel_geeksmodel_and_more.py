# Generated by Django 4.0.3 on 2022-04-17 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0002_imagemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageModel',
            new_name='GeeksModel',
        ),
        migrations.RenameField(
            model_name='geeksmodel',
            old_name='Image_field',
            new_name='geeks_field',
        ),
    ]