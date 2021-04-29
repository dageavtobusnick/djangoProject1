from django.urls import path
from . import views
from .views import UsersView, UserDetailView

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name="login" ),
    path('logout/', views.user_logout),
    path('registration/', views.user_registration, name="registration"),
    path('users/',UsersView.as_view()),
    path('users/<int:pk>',UserDetailView.as_view()),
]
