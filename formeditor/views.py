from django.shortcuts import render, get_object_or_404
from .models import Post, Video
from django.utils import timezone
from .forms import PostForm, CkEditorForm
from django.views import generic
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
        videos = Video.objects.all()
        return render(request, 'formeditor/post_list.html', {'posts': posts, 'videos': videos,})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all()
    return render(request, 'formeditor/post_detail.html', {'post': post, 'posts': posts,})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'formeditor/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'formeditor/post_edit.html', {'form': form})

class CkEditorFormView(generic.FormView):
    form_class = CkEditorForm
    template_name = 'formeditor/form.html'
