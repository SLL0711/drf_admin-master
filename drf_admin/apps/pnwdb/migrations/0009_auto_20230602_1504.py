# Generated by Django 2.2.27 on 2023-06-02 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pnwdb', '0008_auto_20230602_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assemblyproduct',
            options={'ordering': ['-id'], 'verbose_name': '装配产品关系表', 'verbose_name_plural': '装配产品关系表'},
        ),
        migrations.RemoveField(
            model_name='assemblyproduct',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='assemblyproduct',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='assemblyproduct',
            name='modify_by',
        ),
        migrations.RemoveField(
            model_name='assemblyproduct',
            name='state',
        ),
        migrations.RemoveField(
            model_name='assemblyproduct',
            name='update_time',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='purchasematerial',
        ),
        migrations.AlterField(
            model_name='assemblyproduct',
            name='assemblyorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnwdb.AssemblyOrder'),
        ),
        migrations.AlterModelTable(
            name='assemblyproduct',
            table='pnw_assembly_product',
        ),
        migrations.CreateModel(
            name='PurchaseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='原材料采购数量')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnwdb.Materials')),
                ('purchaseorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnwdb.PurchaseOrder')),
            ],
            options={
                'verbose_name': '采购原材料关系表',
                'verbose_name_plural': '采购原材料关系表',
                'db_table': 'pnw_purchase_material',
                'ordering': ['-id'],
            },
        ),
    ]
