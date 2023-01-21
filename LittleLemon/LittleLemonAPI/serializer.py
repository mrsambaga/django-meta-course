from rest_framework import serializers
from .models import MenuItem, Category
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta():
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']
        extra_kwargs = {
            'key':{'min_value':2}, 
            'inventory':{'min_value':0}
        }
