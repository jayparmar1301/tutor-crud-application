from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Course_Info
from tutor.models import Tutor_Info

def tutor_courses_homepage(request, id):
    tutor = Tutor_Info.objects.get(id=id)
    courses = Course_Info.objects.filter(tutor_id=tutor.id)
    return render(request, 'tutor_courses.html', context = {'courses': courses})
