from django.urls import path


# views(url for home page)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
