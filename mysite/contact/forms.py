from django import forms

from .models import Contact
from tinymce.widgets import TinyMCE

class ContactForm(forms.ModelForm):

    #message = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Contact
        fields = ('name', 'surname', 'phone', 'email', 'subject', 'message' ,)

