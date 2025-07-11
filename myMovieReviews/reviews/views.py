from django.shortcuts import render, redirect
from .models import Review


def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})

def reviews_read(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'reviews_read.html', {'review': review})

def reviews_create(request): 
  if request.method == "POST" :
    Review.objects.create(
    title=request.POST["title"],
    release=request.POST["release"],
    genre=request.POST["genre"],
    score=request.POST["score"],
    runtime=request.POST["runtime"],
    director=request.POST["director"],
    actor=request.POST["actor"],
    content=request.POST["content"]
    )
    return redirect("/reviews/")
  return render(request, "reviews_create.html")


def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews/")
# Create your views here.
