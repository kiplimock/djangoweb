from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')

def variable(request):

    context = {
        'first_name': 'Cedric', 
        'last_name': 'Kiplimo',
        'my_list': [1,2,3],
        'user_logged_in': False,
    }
    return render(request, 'my_app/variable.html', context=context)