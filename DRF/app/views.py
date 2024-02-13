from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination    
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

