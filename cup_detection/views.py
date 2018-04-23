from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import glob
import os
# Create your views here.

def index(request):
	return render(request, 'cup_detection/index.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        images_list = glob.glob('cup_detection/static/images/pics/*')

        return render(request, 'cup_detection/index.html', {
            'uploaded_file_url': uploaded_file_url,
            'images_list' : images_list
        })
    return render(request, 'cup_detection/index.html')

