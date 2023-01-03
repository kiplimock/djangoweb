from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100,
#                                 widget=forms.TextInput(attrs={'class':'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
#                                 label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'e.g., john.doe@domain.com'}))
#     review = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),
#                              label='Leave us your thoughts here')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = "__all__"
        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'stars': 'Rating'
        }
        error_messages = {
            'stars': {
                'min_value':"Yo! Min value is 1",
                'max_value':"Yo! Yo! Max value is 5"
            }
        }