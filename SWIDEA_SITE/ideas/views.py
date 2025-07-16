from django.shortcuts import render
from .models import Idea

def ideas_list(request, *args, **kwagrs) :
    ideas = Idea.objects.all()
    context = {
        "ideas" : ideas
    }
    return render(request, "ideas_list.html")