from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/update/', views.post_update, name='update'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('<int:pk>/adjust_interest/', views.adjust_interest, name='adjust_interest'),
    path('<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('<int:pk>/delete/', views.post_delete, name='delete'),
]
