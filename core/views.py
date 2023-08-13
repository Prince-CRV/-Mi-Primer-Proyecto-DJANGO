from core.models import Category, Product
from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    date = {
        'name': 'Prince',
        'categories': Category.objects.all()
    }
    #return JsonResponse(date)
    return render(request, 'index.html', date)

def mysecondview(request):
    date = {
        'name': 'Prince',
        'products': Product.objects.all()
    }
    return render(request, 'second.html', date)