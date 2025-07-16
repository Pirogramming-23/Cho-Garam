from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    sort = request.GET.get("sort", "created")
    ideas = Post.objects.all()

    if sort == "interest":
        ideas = ideas.order_by("-interest")
    elif sort == "title":
        ideas = ideas.order_by("title")
    else:
        ideas = ideas.order_by("-created_at")

    paginator = Paginator(ideas, 4)  # 한 페이지당 4개
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        "posts": posts,
        "sort": sort,
    }
    return render(request, "posts/posts_list.html", context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    return render(request, 'posts/posts_create.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/posts_update.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/posts_detail.html', {'post': post})