from django.urls import path
from reviews.views import * 

urlpatterns = [
    path('', reviews_list),
    path("<int:pk>/", reviews_read),
]
