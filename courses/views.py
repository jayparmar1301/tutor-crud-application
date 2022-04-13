from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Course_Info
from tutor.models import Tutor_Info

def tutor_courses_homepage(request, id):
    tutor = Tutor_Info.objects.get(id=id)
    courses = Course_Info.objects.filter(tutor_id=tutor.id)
    return render(request, 'tutor_courses.html', context = {'courses': courses, 'tutor_id': id})

def add_course_page(request):
    tutor_id = request.GET.get('id')
    return render(request, 'add_course.html', context={'tutor_id': tutor_id})

def add_new_course(request):
    tutor_id = request.GET.get('tutor_id')
    tutor = Tutor_Info.objects.get(id=tutor_id)
    course_name = request.GET.get('course_name')
    course_duration = request.GET.get('course_duration')
    course_description = request.GET.get('course_description')
    Course_Info.objects.create(course_name = course_name,
                                course_duration = course_duration,
                                course_description = course_description,
                                tutor_id = tutor)

    return redirect(f'/courses/{tutor_id}')