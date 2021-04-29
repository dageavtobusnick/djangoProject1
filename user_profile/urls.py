from django.urls import path

from . import views
from .views import UsersView, UserDetailView, ClickView, ClickGetView

urlpatterns = [
    path('', views.index, name='index'),
    path('click/', views.callClick, name='click'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout),
    path('registration/', views.user_registration, name="registration"),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('clicker', views.click),
    path('clicker/<name>', ClickView.as_view()),
    path('clicker/get/<name>', ClickGetView.as_view())
]
