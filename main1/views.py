from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main1/index.html', { 'title': 'Главаня страница сайта', 'tasks': tasks  })

def about(request):
    return render(request,'main1/about.html')


def create(request):
    return render(request,'main1/create.html')