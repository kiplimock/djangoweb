from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')

def variable(request):

    context = {
        'first_name': 'Cedric', 
        'last_name': 'Kiplimo',
        'my_list': [1,2,3],
        'some_dict': {'a': 1, 'b': 2, 'c': 3}
    }
    return render(request, 'my_app/variable.html', context=context)