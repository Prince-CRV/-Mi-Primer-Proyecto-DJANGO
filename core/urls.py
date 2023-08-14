from django.urls import path

from core.view.category.views import *
#from core.views import myfirstview
 

app_name = 'core'

urlpatterns = [
    #path('home/',myfirstview,name='home'),
    path('category/list/', CategoryListView.as_view(), name='category_list')
]