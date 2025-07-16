from django.shortcuts import render

def ideas_list(request) :
  return render(request, "ideas_list.html")