from django.shortcuts import render
from.models import Cat

def article_list(request):
    dog = Cat.objects.all().order_by('date')
    return render(request, 'catarticles/article_list.html', {'dog': dog})
