from django.http import HttpResponse

def home_view(requst):
    return HttpResponse("Home Page")