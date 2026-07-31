from . import views
from django.urls import path
urlpatterns = [
    path('', views.post_list, name ='post_list'),
    path('create/', views.post_create, name ='post_create'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register, name='register'),
] 