from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'surname', 'phone', 'email', 'subject', 'message' ,)

