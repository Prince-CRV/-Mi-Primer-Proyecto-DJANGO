from django.urls import path
from core.views.category.views import category_list
#from core.views import myfirstview
 

app_name = 'core'

urlpatterns = [
    #path('home/',myfirstview,name='home'),
    path('category/list/',category_list,name='category_list')
]