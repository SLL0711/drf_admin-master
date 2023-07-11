# -*- coding: utf-8 -*-
""" 
@author   : 
@software : vscode
@file     : urls.py
@create   : 2023/06/5 10:39
"""
from django.urls import path, include

from pnwdb.views import product
from drf_admin.utils import routers

router = routers.AdminRouter()
router.register(r'products', product.ProductViewSet, basename="product")  # 成品信息管理
urlpatterns = [
    path('', include(router.urls)),
]
