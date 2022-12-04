from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}
# Create your views here.
def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404("404 Generic Error")

# domain.com/first_app/0 -----> doain.com/first_app/sports
def num_page_view(request, num_page):
    topics_list = list(articles.keys()) # ['sports', 'finance', 'politics']
    topic = topics_list[num_page]
    
    return HttpResponseRedirect(reverse('topic_page', args=[topic]))