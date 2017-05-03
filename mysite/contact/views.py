from django.shortcuts import render

# Create your views here.
from .forms import ContactForm
from django.shortcuts import redirect
from .models import Contact
from django.utils import timezone
from django.shortcuts import get_object_or_404

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.created_date = timezone.now()
            message.save()
            return redirect('saved', pk=message.pk)
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form}) 

def saved(request, pk):
    message = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/saved.html', {'message': message})

