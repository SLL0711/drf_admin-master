# Generated by Django 2.2.27 on 2023-06-01 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0006_roles_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='modify_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modify_roles', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_roles', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
    ]