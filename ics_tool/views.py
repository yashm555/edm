# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.template import Context
import datetime
from django.http import HttpResponse
import re


def health(request):
    return HttpResponse("3")

#@login_required(login_url="login/")
def index(request):
    template_name = 'ics_tool/home.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDataForm(request.POST)
    if form.is_valid():

      results = 'Welcome'

      return render(request,'ics_tool/home.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})
