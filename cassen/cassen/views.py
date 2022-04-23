from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST


@require_GET
def get(request):
    return render(request, '1.html')


@require_POST
def post(request):
    return render(request, '1.html')