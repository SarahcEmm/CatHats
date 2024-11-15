from django.shortcuts import render
from.models import Cat
from django.http import HttpResponse
def article_list(request):
    dog = Cat.objects.all().order_by('date')
    return render(request, 'catarticles/article_list.html', {'dog': dog})

def article_details(request, slug):
    dog = Cat.objects.get(slug=slug)
    return render(request, 'catarticles/article_detail.html', {'article': dog})
