from rest_framework import serializers
from .models import MenuItem, Category, Rating
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

class RatingSerializer (serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField( 
        queryset=User.objects.all(), 
        default=serializers.CurrentUserDefault() 
    )
    
    class Meta():
        model = Rating
        fields = ['user', 'menutitem_id', 'rating']

    validator = [
        UniqueTogetherValidator(
            queryset = Rating.objects.all(), 
            fields = ['user', 'menutitem_id']
        )
    ]
    extra_kwargs = {
        'rating':{'min_value':0, 'max_value':5},
    }
