from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


# Create your views here.
def apresentacao_page_view(request):
    return render(request, 'portfolio/layout.html')


# Sobre
def sobre_page_view(request):
    return render(request, 'portfolio/sobre.html')


# Projetos
def projeto_page_view(request):
    return render(request, 'portfolio/projetos.html')


# Contacto
def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


# Licenciatura
def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


# blog
def blog_page_view(request):
    posts = Post.objects.all()

    return render(request, 'portfolio/blog.html', {'posts': posts})


# detail
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.Post)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'portfolio/post_detail.html', {'post': post, 'form': form})
