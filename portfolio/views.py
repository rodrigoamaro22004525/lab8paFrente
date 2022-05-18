from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

import portfolio
from .models import Post
from .models import Portfolio
from .forms import PortfolioForm


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


# Blog
def blog_page_view(request):
    return render(request, 'portfolio/post_list.html')


def novo_portfolio_view(request):
    form = PortfolioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}

    return render(request, 'portfolio/novo.html', context)


def edita_portfolio_view(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form, 'portfolio_id': portfolio_id}
    return render(request, 'portfolio/editar.html', context)


def apaga_portfolio_view(request, portfolio_id):
    Portfolio.objects.get(id=portfolio_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = '{% url portfolio:blog %}'


class PostDetail(generic.DetailView):
    model = Post
    template_name = '{% url portfolio:blog_detail %}'
