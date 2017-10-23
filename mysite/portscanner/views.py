from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import PortScannerForm

def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PortScannerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            host,ports = form.save(commit=True)
            data= {'host': host, 'ports': ports}
            print("> INFO, views.py. Host: " + data['host'] + ", Ports: " + data['ports'])
            # redirect to a new URL:
            return render (request, 'portscanner/results.html', data)
            #return HttpResponseRedirect('portscanner/results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PortScannerForm()

    return render(request, 'portscanner/get_data.html', {'form': form})

"""def results(request):
    return render(request, 'portscanner/results.html', )"""
