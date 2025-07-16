from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, IdeaStar
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def post_list(request):
    sort = request.GET.get("sort", "created")
    ideas = Post.objects.all()

    # 쿠키 기준 찜 상태 가져오기
    cookie_star_status = {}
    for idea in ideas:
        cookie_star_status[idea.pk] = request.COOKIES.get(f'star_{idea.pk}', 'off')

    # 찜순 정렬 우선 처리
    if sort == "star":
        ideas = sorted(
            ideas,
            key=lambda x: (cookie_star_status.get(x.pk) == "on", x.pk),
            reverse=True
        )
    elif sort == "interest":
        ideas = ideas.order_by("-interest")
    elif sort == "title":
        ideas = ideas.order_by("title")
    else:
        ideas = ideas.order_by("-created_at")

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        "posts": posts,
        "sort": sort,
        "cookie_star_status": cookie_star_status,
    }
    return render(request, "posts/posts_list.html", context)




@csrf_exempt
def toggle_star(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    star, created = IdeaStar.objects.get_or_create(session_key=session_key, post=post)

    if not created:
        star.delete()
        status = 'off'
    else:
        status = 'on'

    return JsonResponse({'status': status})
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
            return redirect('posts:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/posts_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    session_key = request.session.session_key
    if session_key:
        is_starred = IdeaStar.objects.filter(session_key=session_key, post=post).exists()
    else:
        is_starred = False

    context = {
        'post': post,
        'is_starred': is_starred,
    }
    return render(request, 'posts/posts_detail.html', context)

@csrf_exempt
def adjust_interest(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "plus":
            post.interest += 1
        elif action == "minus" and post.interest > 0:
            post.interest -= 1
        post.save()
        return JsonResponse({'interest': post.interest})
    
    return JsonResponse({'error': 'invalid request'}, status=400)

def get_or_create_cookie_id(request, response=None):
    cookie_id = request.COOKIES.get('ideastar_id')
    if not cookie_id:
        import uuid
        cookie_id = str(uuid.uuid4())
        if response:
            response.set_cookie('ideastar_id', cookie_id, max_age=60*60*24*30)  # 30일 유지
    return cookie_id

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect('posts:list')

    return redirect('posts:detail', pk=pk)