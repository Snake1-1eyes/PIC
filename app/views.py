from django.shortcuts import render


# Create your views here.
def index(request):
    info = [
        {
            'Init': 'фио',
            'GIP': 'Петров',
            'Comment_GIP': 'Коммент',
            'initiator': '2012-04-01'
        }
    ]
    return render(request, "index.html", {'info': info})