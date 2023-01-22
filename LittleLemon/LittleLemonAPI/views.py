from django.shortcuts import render, get_object_or_404
from .models import *
from .serializer import *
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework.response import Response

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def AddItem(request):
    pass

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data["username"]
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
            return Response({"message" : "User added to manager group"})
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
            return Response({"message" : "User deleted from manager group"})
    if request.method == 'GET':
        managers = Group.objects.get(name="Manager")
        users = managers.user_set.all()
        user_list = [user.username for user in users]
        return Response({"Managers": user_list})
    return Response({"message" : "error"}, status.HTTP_400_BAD_REQUEST)