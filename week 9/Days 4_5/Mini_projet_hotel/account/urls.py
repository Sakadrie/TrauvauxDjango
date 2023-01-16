
from django.urls import path
from . import views
urlpatterns = [
    path('visitor/sign', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout')
]