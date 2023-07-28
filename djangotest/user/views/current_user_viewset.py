from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from user.serializers.user_serializer import UserSerializer


class CurrentUserAPIView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    @extend_schema(
        summary='Получение авторизованного пользователя',
        tags=['Пользователи'],
        responses=UserSerializer,
    )
    def get(self, request):
        serialized = UserSerializer(request.user)
        return Response(serialized.data)