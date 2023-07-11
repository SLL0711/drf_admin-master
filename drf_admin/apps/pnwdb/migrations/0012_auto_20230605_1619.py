# Generated by Django 2.2.27 on 2023-06-05 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pnwdb', '0011_auto_20230605_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='assemblyorder',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='assemblyproduct',
            name='assemblyorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnwdb.AssemblyOrder'),
        ),
        migrations.AlterField(
            model_name='inventory_mtrl',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='inventory_prdt',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='inventoryrecord_mtrl',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='inventoryrecord_prdt',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='order',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='products',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='purchasematerial',
            name='purchaseorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pnwdb.PurchaseOrder'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='warehouses',
            name='modify_by',
            field=models.IntegerField(default=0, null=True, verbose_name='修改人'),
        ),
    ]