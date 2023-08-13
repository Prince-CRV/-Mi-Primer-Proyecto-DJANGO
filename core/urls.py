from django.urls import path

from core.views import myfirstview, mysecondview

app_name = 'core'

urlpatterns = [
    path('uno/',myfirstview,name='vista1'),
    path('dos/',mysecondview,name='vista2')
]