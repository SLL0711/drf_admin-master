# Generated by Django 2.2.27 on 2023-06-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20230605_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='cabinets',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='cabinets',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
    ]
