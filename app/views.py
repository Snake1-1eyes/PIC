from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    info = [
        {
            'Init': 'фио',
            'GIP': f'Петров',
            'Comment_GIP': f'Коммент',
            'initiator': f'2012-04-01'
        }
    ]
    return render(request, "index.html", {'info': info})