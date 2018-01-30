# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from PIL import Image
import glob
image_list = []
for filename in glob.glob('static/text_narrate/*'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)

def index(request):
    return render(request,"home.html",{'l':image_list})
