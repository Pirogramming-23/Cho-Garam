from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/update/', views.post_update, name='update'),
    path('<int:pk>/', views.post_detail, name='detail'),
]
