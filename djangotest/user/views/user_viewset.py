from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.serializers.user_serializer import UserSerializer

@extend_schema_view(
    list=extend_schema(tags=['Пользователи']),
    retrieve=extend_schema(tags=['Пользователи']),
    create=extend_schema(tags=['Пользователи']),
    update=extend_schema(tags=['Пользователи']),
    partial_update=extend_schema(tags=['Пользователи']),
    destroy=extend_schema(tags=['Пользователи']),
)
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]