from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView , TemplateView




#Home Screen
class HomeListView(TemplateView):
    template_name = 'home.html'