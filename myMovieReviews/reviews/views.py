from django.shortcuts import render
from .models import Review


def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})

def reviews_read(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'reviews_read.html', {'review': review})
# Create your views here.
