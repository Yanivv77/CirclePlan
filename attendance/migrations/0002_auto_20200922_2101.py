# Generated by Django 3.1.1 on 2020-09-22 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Instructor', to=settings.AUTH_USER_MODEL),
        ),
    ]