# Generated by Django 2.2.27 on 2023-06-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_roles_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roles',
            name='department',
        ),
    ]
