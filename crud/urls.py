from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="crud-home"),
    path('', views.home, name="crud-home"),
    path('update/<int:pk>/', views.update, name='crud-update'),
    path('delete/<int:pk>/', views.delete, name='crud-delete')
]