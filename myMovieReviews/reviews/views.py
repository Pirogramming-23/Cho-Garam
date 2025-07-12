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
    content=request.POST["content"],
    image_url=request.POST['image_url']
    
    )
    return redirect("/reviews/")
  return render(request, "reviews_create.html")

def reviews_update(request, pk):
    review = Review.objects.get(id=pk)

    if request.method == "POST":
        review.title = request.POST["title"]
        review.release=request.POST["release"]
        review.genre=request.POST["genre"]
        review.score=request.POST["score"]
        review.runtime=request.POST["runtime"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.content=request.POST["content"]
        review.image_url=request.POST['image_url']
        review.save()
        return redirect(f"/reviews/{pk}")

    context = {"review": review}
    return render(request, "reviews_update.html", context)


def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews/")
# Create your views here.
