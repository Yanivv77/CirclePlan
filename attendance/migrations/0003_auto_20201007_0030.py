# Generated by Django 3.1.1 on 2020-10-06 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20201004_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='absence_reason',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='id_number',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='nomatch', message='Id length has to be 9', regex='^.{9}$')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Phone length has to be 10', regex='^.{10}$')]),
        ),
    ]