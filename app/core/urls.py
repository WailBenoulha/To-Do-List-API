from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView,TaskView,get_false_status,get_true_status

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('task/',TaskView.as_view(),name='task'),
    path('task/true/',get_true_status,name='true-status'),
    path('task/false/',get_false_status,name='false-status'),
    path('task/<int:pk>/',TaskView.as_view(),name='task'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]