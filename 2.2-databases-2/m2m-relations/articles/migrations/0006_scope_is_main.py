# Generated by Django 5.1.4 on 2024-12-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
