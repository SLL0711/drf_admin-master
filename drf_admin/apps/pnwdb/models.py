from django.db import models
from drf_admin.utils.models import BaseModel


class Accounts(BaseModel):
    """客户信息"""

    name = models.CharField(max_length=50, unique=True, verbose_name="客户名称")
    telephone1 = models.CharField(max_length=11, null=False, blank=False, default=None, verbose_name='手机号码1')
    telephone2 = models.CharField(max_length=11, null=False, blank=False, default=None, verbose_name='手机号码2')
    email = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name='邮箱')
    address = models.CharField(max_length=200, null=False, blank=False, default=None, verbose_name='地址')
    opportunitys = models.ManyToManyField('Products', db_table='pnw_opportunity', blank=True,
                                   verbose_name='客户意向表')
    
    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='account_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='account_created_by')

    objects = models.Manager()

    # 模型对象字符串表示
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_accounts'
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Products(BaseModel):
    """成品信息"""
    
    name = models.CharField(max_length=50, unique=True, verbose_name="成品名称")
    code = models.CharField(max_length=50,unique=True, null=True, blank=True, default=None, verbose_name='编码')
    price = models.FloatField('产品价格', blank=True, null=True)
    sellprice = models.FloatField('产品售价', blank=True, null=True)
    materials = models.ManyToManyField('Materials', db_table='pnw_product_to_material', blank=True,
                                   verbose_name='产品原材料关系表')
    
    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='product_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='product_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_product'
        verbose_name = '成品信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Materials(BaseModel):
    """原材料信息"""

    name = models.CharField(max_length=50, unique=True, verbose_name="原材料名称")
    code = models.CharField(max_length=50,unique=True, null=True, blank=True, default=None, verbose_name='编码')
    price = models.FloatField('单价', blank=True, null=True)
    vendor = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name='厂商')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='material_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='material_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_material'
        verbose_name = '原材料信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Warehouses(BaseModel):
    """仓库信息"""

    warehouse_category_choice = (
        (0, '成品仓'),
        (1, '原材料仓'),
    )

    name = models.CharField(max_length=50, unique=True, verbose_name="仓库名称")
    category = models.SmallIntegerField(choices=warehouse_category_choice, default=0, verbose_name='仓库类型')
    telephone1 = models.CharField(max_length=11, null=False, blank=False, default=None, verbose_name='联系方式1')
    telephone2 = models.CharField(max_length=11, null=False, blank=False, default=None, verbose_name='联系方式2')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='warehouse_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='warehouse_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_warehouses'
        verbose_name = '仓库信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Inventory_prdt(BaseModel):
    """成品库存信息"""

    count = models.IntegerField(null=False,blank=False,verbose_name='剩余数量')
    inbound = models.IntegerField(null=False,blank=False,verbose_name='待入库数量')
    outbound = models.IntegerField(null=False,blank=False,verbose_name='待出库数量')
    product = models.ForeignKey('Products', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='成品')
    warehouse = models.ForeignKey('Warehouses', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='仓库')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='inventory_prdt_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='inventory_prdt_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_inventory_prdt'
        verbose_name = '成品库存信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Inventory_mtrl(BaseModel):
    """原材料库存信息"""

    count = models.IntegerField(null=False,blank=False,verbose_name='剩余数量')
    inbound = models.IntegerField(null=False,blank=False,verbose_name='待入库数量')
    outbound = models.IntegerField(null=False,blank=False,verbose_name='待出库数量')
    material = models.ForeignKey('Materials', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='原材料')
    warehouse = models.ForeignKey('Warehouses', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='仓库')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='inventory_mtrl_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='inventory_mtrl_created_by')
    
    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_inventory_mtrl'
        verbose_name = '原材料库存信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Inventoryrecord_prdt(BaseModel):
    """成品出入库记录"""

    inventory_direction_choice = (
        (0, '入库'),
        (1, '出库'),
    )
    
    name = models.CharField(max_length=50, unique=True, verbose_name="出入库编号")
    material = models.ForeignKey('Products', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='成品')
    warehouse = models.ForeignKey('Warehouses', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='仓库')
    ordername = models.CharField(max_length=50, unique=False,null=True,blank=True, verbose_name="订单号")
    assemblyname = models.CharField(max_length=50, unique=False,null=True,blank=True, verbose_name="装配单号")
    count = models.IntegerField(null=False,blank=False,verbose_name='数量')
    direction = models.SmallIntegerField(choices=inventory_direction_choice, default=0, verbose_name='出入库')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='inventoryrecord_prdt_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='inventoryrecord_prdt_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_inventoryrecord_prdt'
        verbose_name = '成品出入库记录'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Inventoryrecord_mtrl(BaseModel):
    """原材料出入库记录"""

    inventory_direction_choice = (
        (0, '入库'),
        (1, '出库'),
    )
    
    name = models.CharField(max_length=50, unique=True, verbose_name="出入库编号")
    material = models.ForeignKey('Materials', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='原材料')
    warehouse = models.ForeignKey('Warehouses', null=True, blank=True, on_delete=models.SET_NULL,
                                           verbose_name='仓库')
    purchasername = models.CharField(max_length=50, unique=False,null=True,blank=True, verbose_name="采购单号")
    assemblyname = models.CharField(max_length=50, unique=False,null=True,blank=True, verbose_name="装配单号")
    count = models.IntegerField(null=False,blank=False,verbose_name='数量')
    direction = models.SmallIntegerField(choices=inventory_direction_choice, default=0, verbose_name='出入库')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='inventoryrecord_mtrl_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='inventoryrecord_mtrl_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_inventoryrecord_mtrl'
        verbose_name = '原材料出入库记录'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class Order(BaseModel):
    """订单信息"""

    inventory_direction_choice = (
        (0, '入库'),
        (1, '出库'),
    )

    order_deliver_status_choice = (
        (0, '待发货'),
        (1, '已发货'),
        (2, '中止'),
        (3, '超时'),
        (4, '其他'),
    )

    order_status_choice = (
        (0, '装配中'),
        (1, '采购中'),
        (2, '其他'),
    )
    
    deliver_level_choice = (
        (0, '重要'),
        (1, '一般'),
        (2, '紧急'),
    )

    payway_choice = (
        (0, '现金'),
        (1, '微信'),
        (2, '支付宝'),
        (3, '信用卡'),
        (4, '其他'),
    )
    
    name = models.CharField(max_length=50, unique=True, verbose_name="订单号")
    price = models.FloatField('订单总价', blank=True, null=True)
    account = models.ForeignKey('Accounts', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="下单客户")
    address = models.CharField(max_length=200, null=False, blank=False, default=None, verbose_name='收货地址')
    status = models.SmallIntegerField(choices=order_deliver_status_choice, default=0, verbose_name='发货状态')
    innerstatus = models.SmallIntegerField(choices=order_status_choice, default=0, verbose_name='内部状态')
    deliverlevel = models.SmallIntegerField(choices=deliver_level_choice, default=0, verbose_name='发货优先级')
    processor = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="处理人",related_name='processor')
    responsibleuser = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="责任人",related_name='responsibleuser')
    logistics = models.CharField(max_length=50, verbose_name="物流单号")
    deliverdate = models.DateField(null=True, blank=True, verbose_name="预估交付日期")
    isgather = models.BooleanField(verbose_name='是否已全部回款')
    receivedmoney = models.FloatField('已收金额', blank=True, null=True)
    payway = models.SmallIntegerField(choices=payway_choice, default=0, verbose_name='支付方式')
    ticketnumber = models.CharField(max_length=50, unique=False, verbose_name="发票号")

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='order_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='order_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_order'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class AssemblyOrder(BaseModel):
    """装配单信息"""

    assembly_level_choice = (
        (0, '重要'),
        (1, '一般'),
        (2, '紧急'),
    )
    
    name = models.CharField(max_length=50, unique=True, verbose_name='装配单号')
    ordername = models.CharField(max_length=50, unique=False, verbose_name='订单号')
    assemblylevel = models.SmallIntegerField(choices=assembly_level_choice, default=0, verbose_name='装配优先级')
    time = models.DateField(null=True, blank=True, verbose_name="需求完成日期")
    completetime = models.DateField(null=True, blank=True, verbose_name="预计装配完成时间")
    processor = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="处理人",related_name='assembly_order_processor')
    responsibleuser = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="责任人",related_name='assembly_order_responsibleuser')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='assemblyorder_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='assemblyorder_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_assembly_order'
        verbose_name = '装配单信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class AssemblyProduct(models.Model):
    """装配产品关系表"""

    assemblyorder = models.ForeignKey('AssemblyOrder', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    count = models.IntegerField(null=False,blank=False,verbose_name='产品装配数量')

    class Meta:
        db_table = 'pnw_assembly_to_product'
        verbose_name = '装配产品关系表'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class PurchaseOrder(BaseModel):
    """采购单信息"""

    purchase_level_choice = (
        (0, '重要'),
        (1, '一般'),
        (2, '紧急'),
    )

    
    name = models.CharField(max_length=50, unique=True, verbose_name='采购单号')
    assemblyordername = models.CharField(max_length=50, unique=False, verbose_name='装配单号')
    purchaselevel = models.SmallIntegerField(choices=purchase_level_choice, default=0, verbose_name='采购优先级')
    arrivedate = models.DateField(null=True, blank=True, verbose_name="希望入库日期")
    processor = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="处理人",related_name='purchase_order_processor')
    responsibleuser = models.ForeignKey('oauth.Users', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="责任人",related_name='purchase_order_responsibleuser')

    modify_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='修改人',related_name='purchaseorder_modify_by')
    created_by = models.ForeignKey(to='oauth.Users', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='创建人',related_name='purchaseorder_created_by')

    # 初始化管理器
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pnw_purchase_order'
        verbose_name = '采购单信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列


class PurchaseMaterial(models.Model):
    """采购原材料关系表"""

    purchaseorder = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE)
    material = models.ForeignKey('Materials', on_delete=models.CASCADE)
    count = models.IntegerField(null=False,blank=False,verbose_name='原材料采购数量')

    class Meta:
        db_table = 'pnw_purchase_to_material'
        verbose_name = '采购原材料关系表'
        verbose_name_plural = verbose_name
        ordering = ['-id']  #默认降序排列