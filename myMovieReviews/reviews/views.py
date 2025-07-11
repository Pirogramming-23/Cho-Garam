from django.shortcuts import render,HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def reviews_list(request):
    return render(request, "reviews_list.html")

# Create your views here.
