from django.shortcuts import render
from django.views.generic import ListView

from core.models import Category


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }

    return render(request, 'category/category_list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    # def get_queryset(self):
    #     return Category.objects.filter(name__startswith='L')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
