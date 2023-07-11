# Generated by Django 2.2.27 on 2023-06-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20230605_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='permissions',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='permissions',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='created_by',
            field=models.IntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='modify_by',
            field=models.IntegerField(null=True, verbose_name='修改人'),
        ),
    ]