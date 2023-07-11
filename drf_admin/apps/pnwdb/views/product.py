# -*- coding: utf-8 -*-
""" 
@author   : 
@software : vscode
@file     : urls.py
@create   : 2023/06/5 10:39
"""
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from drf_admin.utils.views import AdminViewSet
from pnwdb.models import Products
from pnwdb.serializers.product import ProductsSearchSerializer,ProductsSerializer


class ProductViewSet(AdminViewSet):
    """
    create:
    成品--新增

    成品新增, status: 201(成功), return: 新增成品信息

    destroy:
    成品--删除

    成品删除, status: 204(成功), return: None

    multiple_delete:
    成品--批量删除

    成品批量删除, status: 204(成功), return: None

    update:
    成品--修改

    成品修改, status: 200(成功), return: 修改后的成品信息

    partial_update:
    成品--局部修改(成品授权)

    成品局部修改, status: 200(成功), return: 修改后的成品信息

    list:
    成品--获取列表

    成品信息列表, status: 200(成功), return: 成品信息列表
    """
    # queryset = Products.objects.all()
    queryset = Products.objects.filter(state=0)
    serializer_class = ProductsSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'code')
    ordering_fields = ('id', 'update_time')

    def get_serializer_class(self):
        if self.action in ['retrieve','list']:
            return ProductsSearchSerializer
        else:
            return ProductsSerializer
    

    def create(self, request, *args, **kwargs):
        userId = request.user.id
        request.data['created_by'] = userId
        request.data['modify_by'] = userId
        return super().create(request,*args, **kwargs)

    def update(self, request, *args, **kwargs):
        # if self.get_object().name == 'admin':
        #     return Response(data={'detail': 'admin角色不可修改'}, status=status.HTTP_400_BAD_REQUEST)
        userId = request.user.id
        request.data['modify_by'] = userId
        return super().update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     if self.get_object().name == 'admin':
    #         return Response(data={'detail': 'admin角色不可删除'}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().destroy(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     if self.get_object().name == 'admin':
    #         return Response(data={'detail': 'admin角色, 默认拥有所有权限'}, status=status.HTTP_400_BAD_REQUEST)
    #     return super().partial_update(request, *args, **kwargs)

    # def multiple_delete(self, request, *args, **kwargs):
    #     delete_ids = request.data.get('ids')
    #     try:
    #         admin = Roles.objects.get(name='admin')
    #         if isinstance(delete_ids, list):
    #             if admin.id in delete_ids:
    #                 return Response(data={'detail': 'admin角色不可删除'}, status=status.HTTP_400_BAD_REQUEST)
    #     except Roles.DoesNotExist:
    #         pass
    #     return super().multiple_delete(request, *args, **kwargs)
