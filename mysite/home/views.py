from django.shortcuts import render
from .forms import InputForm
from .models import Survey
from django.http import HttpResponseRedirect
from random import *
from distutils import util

def index(request):

    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            question1 = form.cleaned_data["heard_of_cryptocurrency"]
            question2 = form.cleaned_data["purchased_cryptocurrency"]
            question3 = form.cleaned_data["consider_valid"]
            question4 = form.cleaned_data["advertisement_as_monetization"]
            intensity = form.cleaned_data["mining_intensity"]
            is_m = bool(util.strtobool(request.POST.get("is_m")))
            question5 = form.cleaned_data["performance_hits"]
            question6 = form.cleaned_data["experience"]
            question7 = form.cleaned_data["consider_solution"]
            question8 = form.cleaned_data["sex"]
            question9 = form.cleaned_data["age"]
            question10 = form.cleaned_data["country"]

            survey = Survey()

            survey.heard_of_cryptocurrency = question1
            survey.purchased_cryptocurrency = question2
            survey.consider_valid = question3
            survey.advertisement_as_monetization = question4
            survey.mining_intensity = intensity
            survey.is_mobile = is_m
            survey.performance_hits = question5
            survey.experience = question6
            survey.consider_solution = question7
            survey.sex = question8
            survey.age = question9
            survey.country = question10

            survey.save()
            return HttpResponseRedirect('/')
    else:
        form = InputForm(initial={'mining_intensity': randint(0,2)})
        return render(request, 'index.html', {'form': form})


