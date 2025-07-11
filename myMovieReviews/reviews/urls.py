from django.urls import path
from reviews.views import * 

urlpatterns = [
    path('', reviews_list, name='reviews_list'),
    path("<int:pk>/", reviews_read),
    path("create/", reviews_create),
    path("<int:pk>/delete/", reviews_delete),
    path("<int:pk>/update/", reviews_update),
]
