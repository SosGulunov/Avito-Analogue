import random

from django.shortcuts import render
from .models import Ad, Person
from .form import PostForm

def home(request):
    r = random.randint(1, 15)
    numbers = []
    for i in range(random.randint(1, 5)):
        numbers.append(1)
    count = len(numbers)
    ad = Ad.objects.all()
    person = Person.objects.all()
    return render(request, 'front/index.html', {'ad': ad, 'person': person, 'random': r, 'randoma': numbers, 'count': count})


def add(request):
    form = PostForm()
    return render(request, "front/add.html",  {'form': form})

