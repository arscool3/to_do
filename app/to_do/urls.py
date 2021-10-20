import time

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
   # path('', views.index, name = 'index')
    path('task/create/', TaskCreatView.as_view()),
    path('all/', TaskListView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name = 'auth_register')
]