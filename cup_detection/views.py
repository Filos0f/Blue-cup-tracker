from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from cup_detection.detector import do_detection
import glob
import os
# Create your views here.

def index(request):
	return render(request, 'cup_detection/index.html')

