from django.shortcuts import render


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

