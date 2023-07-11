# -*- coding: utf-8 -*-
"""
@author   : 
@github   : https://github.com/tianpangji
@software : PyCharm
@file     : roles.py
@create   : 2020/7/22 21:30
"""
from rest_framework import serializers

from pnwdb.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    """
    成品管理序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    # created_by_name = serializers.ReadOnlyField(source='created_by.username')

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    # def create(self, validated_data):
    #     return super().create(validated_data)

    class Meta:
        model = Products
        fields = ['id', 'name', 'code', 'price','sellprice','materials', 'create_time','update_time','state','created_by','modify_by']#,'created_by_name']
        extra_kwargs =  {
            'created_by':{
                'write_only':True
            },
            'modify_by':{
                'write_only':True
            }
        }

class ProductsSearchSerializer(serializers.ModelSerializer):
    """
    成品查询序列化器
    """
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')
    modify_by = serializers.ReadOnlyField(source='modify_by.username')

    class Meta:
        model = Products
        fields = ['id', 'name', 'code', 'price','sellprice','materials', 'create_time','update_time','state','created_by','modify_by']
        extra_kwargs =  {
            # 'permissions': {
            #     'read_only': True,
            # },
        }