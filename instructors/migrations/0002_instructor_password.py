# Generated by Django 3.1.1 on 2020-09-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='password',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]
