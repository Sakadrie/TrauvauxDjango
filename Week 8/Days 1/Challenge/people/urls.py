
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.people, name="people"),
    path('people_one/<int:id>', views.people_one, name="people_one"),
]


