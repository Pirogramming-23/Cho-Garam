from django.urls import path
from .views import *

urlpatterns = [
	path('', ideas_list ),
]