# Generated by Django 2.2.27 on 2023-06-02 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pnwdb', '0006_auto_20230602_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaseorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('created_by', models.IntegerField(null=True, verbose_name='创建人')),
                ('modify_by', models.IntegerField(null=True, verbose_name='修改人')),
                ('state', models.IntegerField(default=0, verbose_name='禁用状态')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='采购单号')),
                ('assemblyordername', models.CharField(max_length=50, verbose_name='装配单号')),
                ('purchaselevel', models.SmallIntegerField(choices=[(0, '重要'), (1, '一般'), (2, '紧急')], default=0, verbose_name='采购优先级')),
                ('arrivedate', models.DateField(blank=True, null=True, verbose_name='希望入库日期')),
                ('processor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_order_processor', to=settings.AUTH_USER_MODEL, verbose_name='处理人')),
                ('purchasematerial', models.ManyToManyField(blank=True, db_table='pnw_purchase_material', to='pnwdb.Materials', verbose_name='采购原材料关系表')),
                ('responsibleuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_order_responsibleuser', to=settings.AUTH_USER_MODEL, verbose_name='责任人')),
            ],
            options={
                'verbose_name': '采购单信息',
                'verbose_name_plural': '采购单信息',
                'db_table': 'pnw_purchase_order',
                'ordering': ['-id'],
            },
        ),
    ]
