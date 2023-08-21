from django.urls import path

from core.view.category.views import *
#from core.views import myfirstview


app_name = 'core'

urlpatterns = [
    #path('home/',myfirstview,name='home'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]