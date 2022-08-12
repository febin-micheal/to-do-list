from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<pk>', views.home, name='home'),
    path('view/', views.list_view, name='list_view'),
    path('create/', views.create, name='create'),
    path('edit/<pk>', views.edit, name='edit'),
    path('update/<pk>', views.update, name='update'),
    path('delete/<pk>', views.delete, name='delete'),
]
