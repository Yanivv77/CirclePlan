# Generated by Django 3.0.7 on 2020-06-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200615_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
