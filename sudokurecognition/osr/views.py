from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

from . import forms
from osr.models import SudokuModel

import cv2
from PIL import Image

# Create your views here.

def success(request):
    return render(request, 'osr/success.html')

def sudokuform(request):

    if request.method == 'POST':
        form = forms.SudokuForm(request.POST, request.FILES)
        if form.is_valid():
            #form.name = form.cleaned_data['name']
            form.save(commit=True)
            #printtext()
            img_url = request.build_absolute_uri('/media/') + "board_border.jpg"
            return render(request, 'osr/success.html', {'image': img_url})
    else:
        form = forms.SudokuForm()

    return render(request, 'osr/sudoku-form.html', {'form': form})

def handle_uploaded_file(f):
    with open('image.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
