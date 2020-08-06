from django import forms

from .models import Recommendation


class ContactForm(forms.Form):
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Votre nom *'}))
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Votre prénom *'}))
    companyName = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nom de votre entreprise'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Votre adresse mail *'}))
    messageObject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Objet de votre message *'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Votre message *'}))


class RecommendationForm(forms.ModelForm):

    class Meta:
        model = Recommendation
        fields = ['lastname', 'firstname', 'companyname', 'mail', 'message']
        widgets = {
            'lastname': forms.TextInput(attrs={'placeholder': 'Votre nom *'}),
            'firstname': forms.TextInput(attrs={'placeholder': 'Votre prénom *'}),
            'companyname': forms.TextInput(attrs={'placeholder': 'Nom de votre entreprise'}),
            'mail': forms.EmailInput(attrs={'placeholder': 'Votre adresse mail'}),
            'message': forms.Textarea(attrs={'placeholder': 'Votre message *'}),
        }
