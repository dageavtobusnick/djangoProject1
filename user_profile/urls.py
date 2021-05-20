from django.urls import path

from . import views
from .views import UsersView, UserDetailView,CycleView,CycleDetailView

urlpatterns = [
    path('click/', views.call_click, name='click'),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('cycles/', CycleView.as_view()),
    path('cycles/<int:pk>', CycleDetailView.as_view()),
]
