# Generated by Django 3.1.1 on 2020-10-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20201007_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='absence_reason',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
