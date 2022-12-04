from django.urls import path
from . import views

# this is a list of view routes
urlpatterns = [
    # path() connects a view function to a URL
    path('', views.simple_view) # domain.com/first_app
]