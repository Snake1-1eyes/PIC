from django.shortcuts import render
from .models import Table1

# Create your views here.
def index(request):
    # info = [
    #     {
    #         'Init': 'фио',
    #         'GIP': 'Петров',
    #         'Comment_GIP': 'Коммент',
    #         'initiator': '2012-04-01'
    #     }
    # ]
    info = Table1.objects.all()
    return render(request, "index.html", {'info': info})