from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('welcome/', views.welcome, name="welcome"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),

]
