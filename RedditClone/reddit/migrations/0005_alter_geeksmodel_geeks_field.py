# Generated by Django 4.0.3 on 2022-05-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0004_alter_geeksmodel_geeks_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='geeks_field',
            field=models.ImageField(blank=True, upload_to='geeksmodel_geeks_field'),
        ),
    ]
