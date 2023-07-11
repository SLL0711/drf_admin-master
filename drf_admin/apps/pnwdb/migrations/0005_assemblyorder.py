# Generated by Django 2.2.27 on 2023-06-02 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pnwdb', '0004_auto_20230602_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assemblyorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('created_by', models.IntegerField(null=True, verbose_name='创建人')),
                ('modify_by', models.IntegerField(null=True, verbose_name='修改人')),
                ('state', models.IntegerField(default=0, verbose_name='禁用状态')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='装配单号')),
                ('ordername', models.CharField(max_length=50, verbose_name='订单号')),
                ('assemblylevel', models.SmallIntegerField(choices=[(0, '重要'), (1, '一般'), (2, '紧急')], default=0, verbose_name='装配优先级')),
                ('time', models.DateField(blank=True, null=True, verbose_name='需求完成日期')),
                ('completetime', models.DateField(blank=True, null=True, verbose_name='预计装配完成时间')),
                ('assemblyproduct', models.ManyToManyField(blank=True, db_table='pnw_assemblyproduct', to='pnwdb.Products', verbose_name='装配产品关系表')),
                ('processor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assembly_order_processor', to=settings.AUTH_USER_MODEL, verbose_name='处理人')),
                ('responsibleuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assembly_order_responsibleuser', to=settings.AUTH_USER_MODEL, verbose_name='责任人')),
            ],
            options={
                'verbose_name': '装配单信息',
                'verbose_name_plural': '装配单信息',
                'db_table': 'pnw_assembly_order',
                'ordering': ['-id'],
            },
        ),
    ]
