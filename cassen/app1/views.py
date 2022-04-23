from django.shortcuts import render
from . models import Db
# Create your views here.


def index(request):
    content = Db.objects.all()
    res = []
    for c in content:
        res.append(str(c.id) + ' ' + c.content)
    return render(request, 'index.html', {"content": res})