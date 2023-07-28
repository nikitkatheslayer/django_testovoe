from django.urls import path

from rest_framework.routers import DefaultRouter

from user.views.current_user_viewset import CurrentUserAPIView
from user.views.user_viewset import UserModelViewSet

app_name = 'user'

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('current_user/', CurrentUserAPIView.as_view(), name='current_user'),
]

urlpatterns += router.urls