from django.urls import path
from .views import *

urlpatterns = [
	path('', ideas_list ),
    path("<int:pk>/", ideas_read),
    path("create/", ideas_create),
    path("<int:pk>/update/", ideas_update),
    path("<int:pk>/delete/", ideas_delete),
]
