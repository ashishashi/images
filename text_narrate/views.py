# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import glob
def index(request):
	image_list = []
	for filename in glob.glob('text_narrate/media/*.jpg'): #assuming gif
	    #im=Image.open(filename)
	    filename=filename[19:]
	    image_list.append(filename)

	return render (request,'home.html',{'image_list':image_list})
	#return render(home.html,{'image_list':filename})

