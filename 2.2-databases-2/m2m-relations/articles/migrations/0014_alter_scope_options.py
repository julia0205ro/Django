# Generated by Django 5.1.4 on 2024-12-13 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_scope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag'], 'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематика статьи'},
        ),
    ]
