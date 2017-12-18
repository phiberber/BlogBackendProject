# _*_ coding: utf-8 _*_
__author__ = 'LennonChin'
__date__ = '2017/12/2 12:56'

from rest_framework import serializers

from .models import AlbumInfo, AlbumPhoto
from material.serializers import SingleLevelCategorySerializer, TagSerializer


class AlbumDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumPhoto
        fields = "__all__"


class AlbumDetailInfoSerializer(serializers.ModelSerializer):
    category = SingleLevelCategorySerializer()
    # pictures = AlbumDetailSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = AlbumInfo
        fields = "__all__"


class AlbumBaseInfoSerializer(serializers.ModelSerializer):
    category = SingleLevelCategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = AlbumInfo
        fields = "__all__"
