# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os, json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .forms import InputForm
from models import UniversityFinder

# Create your views here.
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # career = form.cleaned_data['career']
            # region = form.cleaned_data['region']
            # gender = form.cleaned_data['gender']
            # edu_level = form.cleaned_data['education_level']
            #
            # schools = get_schools(career, region, gender, edu_level)
            # if edu_level == '1':
            #     school_level = "A levels"
            # else:
            #     school_level = "O levels"
            # redirect to a new URL:
            return render(request, 'index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        3
        #queryset1 = Acseeyear2017Subjectperformance.objects.filter(subjectname = "Chemistry").filter()
        #queryset2 = Acseeyear2017Subjectperformance.objects.filter(subjectname = "Biology").filter
        #stories = queryset1 | queryset2
        #print stories.distinct().order_by('schoolcode')
        form = InputForm(label_suffix="  ")
        return render(request, 'index.html', {'form': form})
