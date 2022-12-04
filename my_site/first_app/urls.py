from django.urls import path
from . import views

# this is a list of view routes
urlpatterns = [
    # path() connects a view function to a URL
    path('<int:num_page>/', views.num_page_view),
    path('<str:topic>/', views.news_view, name='topic_page')
]