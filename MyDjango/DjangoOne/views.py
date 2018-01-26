from django.shortcuts import render
from random import randint


def home(request):
    num_list = [randint(500, 2000), randint(500, 2000), randint(500, 2000)]
    print(num_list)
    template_context = {
        "num_list": num_list
    }
    return render(request, 'home.html', context=template_context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')
