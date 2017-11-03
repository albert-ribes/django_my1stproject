from django import forms

class PortScannerForm(forms.Form):
    #print("> INFO, forms.py: Class definition")
    host_selector=forms.CharField(label='Hosts', max_length=100)
    port_selector=forms.CharField(label='Ports', max_length=100)

    def save(self, commit=True):
        #print("> INFO, forms.py: save() method")
        hosts = self.cleaned_data.get('host_selector', None)
        ports = self.cleaned_data.get('port_selector', None)
        #print("> INFO, forms.py. Host: " + host + ", Ports: " + ports)
        # Take the right actions
        return(hosts, ports)

