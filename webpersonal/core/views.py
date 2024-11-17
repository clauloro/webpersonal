from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
html_base = """
 <h1>Mi Web Personal</h1>
 <ul>
 <li><a href="/">Portada</a></li>
 <li><a href="/about/">Acerca de</a></li>
 <li><a href="/contact/">Contacto</a></li>
 </ul>
"""
def home(request):
 return render(request, "core/home.html")

def about(request):
 return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def portfolio(request):
    return render(request, "core/portfolio.html")





