from django.urls import path
from . import views

urlpatterns = [
        path('api/test', views.test_strategy, name='test_strategy'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('register/', views.register_view, name='register'),
]
