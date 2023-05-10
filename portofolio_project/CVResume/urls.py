from django.urls import path
from . import views

urlpatterns = [
    path('CVResume', views.cv, name='cv')
]