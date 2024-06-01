from django.urls import path
from .import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

"app/model_viewtype"
"recipes/recipe_detail.html"

urlpatterns = [
    path("", views.RecipeListView.as_view(), name = "recipes-home"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name = "recipes-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name = "recipes-create"), 
    #by naming convention, this automatically links to recipe_form.html
    path("recipe/<int:pk>/update/", views.RecipeUpdateView.as_view(), name = "recipes-update"),
    path("recipe/<int:pk>/delete/", views.RecipeDeleteView.as_view(), name = "recipes-delete"),
    path("about/", views.about, name = "recipes-about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)