from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        "recipes": recipes,
    }
    return render(request, "recipes/home.html", context)

def about(request):
    context = {
        "title": "About page",
    }
    return render(request, "recipes/about.html", context)

class RecipeListView(ListView):
    model = models.Recipe #the default name is object, meaning that the html file cannot read any of contents from 'Object'
    template_name =  "recipes/home.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = "recipes/recipe_detail.html"

class RecipeCreateView(CreateView):
    model = models.Recipe
    fields = ["title", "ingredients", "steps", "img"]
    
    #this automatically submits the data to the database 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(UpdateView):
    model = models.Recipe
    fields = ["title", "ingredients", "steps", "img"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class RecipeDeleteView(DeleteView):
    model = models.Recipe
    success_url = reverse_lazy("recipes-home")
    #the success_url links to the page when the recipe is "successfully deleted"
    