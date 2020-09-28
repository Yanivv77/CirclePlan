# Generated by Django 3.1.1 on 2020-09-27 11:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0006_auto_20200926_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='observations',
            new_name='description',
        ),
        migrations.AddField(
            model_name='member',
            name='id_number',
            field=models.CharField(default=' ', max_length=9, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 9', regex='^.{9}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='circle',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='instructor',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Instructor'}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
