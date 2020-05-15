from tkinter import Entry

from django.urls import path
from django.views.generic import ListView
from .models import Customer
from . import views

class EntryList(ListView):
    queryset = Entry.objects.filter(point__isnull=False)

urlpatterns = [
    path("", views.index, name="Home"),
    path('map/', EntryList.as_view()),
]
