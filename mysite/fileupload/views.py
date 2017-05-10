from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Document
from django.shortcuts import get_object_or_404

def fileupload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('file_saved', pk=form.pk)
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/fileupload.html', {
        'form': form
    })


def fileupload_old(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('saved')
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/fileupload.html', {'form': form})

def file_saved(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'fileupload/file_saved.html', {'document': document})

