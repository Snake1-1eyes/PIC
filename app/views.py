from django.shortcuts import render
from .models import Site

# Create your views here.
def index(request):
    site = Site()
    info = site.get_data()
    return render(request, "index.html", {'info': info})