# Generated by Django 2.2.27 on 2023-06-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20230602_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='created_by',
            field=models.IntegerField(default=0, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='cabinets',
            name='created_by',
            field=models.IntegerField(default=0, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='created_by',
            field=models.IntegerField(default=0, null=True, verbose_name='创建人'),
        ),
    ]