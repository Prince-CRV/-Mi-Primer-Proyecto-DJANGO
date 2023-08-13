from django.urls import path

from core.views import myfirstview


urlpatterns = [
    path('uno/',myfirstview),
    path('dos/',myfirstview)
]