from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from portscanner.scripts.test import portscan

from .forms import PortScannerForm

def get_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PortScannerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            hosts_str,ports_str = form.save(commit=True)
            hosts=hosts_str.replace(" ", "").split(",")
            ports=ports_str.replace(" ", "").split(",")
            results=portscan(hosts, ports)
            #res= {'results': results}
            #print(res)
            print(results)
            #redirect to a new URL:
            return render (request, 'portscanner/results.html', {'results' : results, 'hosts' : hosts, 'ports': ports})
            #return HttpResponseRedirect('portscanner/results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PortScannerForm()
    return render(request, 'portscanner/get_data.html', {'form': form})

"""def results(request):
    return render(request, 'portscanner/results.html', )"""
