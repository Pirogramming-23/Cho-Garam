from django.shortcuts import render, get_object_or_404,redirect
from .models import Idea

def ideas_list(request):
    ideas = Idea.objects.all()
    context = {
        "ideas": ideas
    }
    return render(request, "ideas_list.html", context)  # context 빠졌던 부분 추가

def ideas_read(request, pk):
    idea = get_object_or_404(Idea, id=pk)  # 변수명 통일: idea (단수)
    context = {
        "idea": idea
    }
    return render(request, "ideas_read.html", context)  # context도 수정


def ideas_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        interest = request.POST.get('interest')
        devtool = request.POST.get('devtool')

        image = request.FILES.get('image')  # ★ 이 부분 반드시 request.FILES 사용

        Idea.objects.create(
            title=title,
            content=content,
            interest=interest,
            devtool=devtool,
            image=image
        )
        return redirect('/ideas/')
    else:
        return render(request, 'ideas_create.html')
    

def ideas_update(request, pk):
    idea = get_object_or_404(Idea, id=pk)

    if request.method == "POST":
        idea.title = request.POST.get("title")
        idea.content = request.POST.get("content")
        idea.interest = request.POST.get("interest")
        idea.devtool = request.POST.get("devtool")

        if 'image' in request.FILES:
            idea.image = request.FILES['image']

        idea.save()
        return redirect(f"/ideas/{pk}/")

    context = {"idea": idea}
    return render(request, "ideas_update.html", context)


def ideas_delete(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/ideas/")