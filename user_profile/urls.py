from django.urls import path

from . import views
from .views import UsersView, UserDetailView, CycleView, CycleDetailView, BoostListView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('cycles/', CycleView.as_view()),
    path('cycles/<int:pk>', CycleDetailView.as_view()),
    path('boosts/<int:mainCycle>', BoostListView.as_view()),
    path('buyBoost/', views.buy_boost, name='buyBoost'),
    path('set_main_cycle/', views.set_main_cycle, name='set_main_cycle'),
]
