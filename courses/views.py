from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Course_Info
from tutor.models import Tutor_Info
from django.core.exceptions import  ObjectDoesNotExist

def tutor_courses_homepage(request, id):
    try:
        tutor = Tutor_Info.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No Tutor info found' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    courses = Course_Info.objects.filter(tutor_id=tutor.id)
    return render(request, 'tutor_courses.html', context = {'courses': courses, 'tutor': tutor})

def add_course_page(request):
    tutor_id = request.GET.get('id')
    return render(request, 'add_course.html', context={'tutor_id': tutor_id})

def add_new_course(request):
    tutor_id = request.GET.get('tutor_id')
    tutor = Tutor_Info.objects.get(id=tutor_id)
    course_name = request.GET.get('course_name')
    course_duration = request.GET.get('course_duration')
    course_description = request.GET.get('course_description')
    try:
        Course_Info.objects.create(course_name = course_name,
                                    course_duration = course_duration,
                                    course_description = course_description,
                                    tutor_id = tutor)
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return redirect(f'/courses/{tutor_id}')

def edit_course(request, id):
    try:
        course = Course_Info.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No course found with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return render(request, 'edit_course_info.html', context = { 'course': course })

def update_course(request, id):
    try:
        course = Course_Info.objects.get(id=id)
        course.course_name = request.GET.get('course_name') if request.GET.get('course_name') is not None else course.course_name
        course.course_duration = request.GET.get('course_duration') if request.GET.get('course_duration') else course.course_duration
        course.course_description = request.GET.get('course_description') if request.GET.get('course_description') else course.course_description
        course.save()
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No course found with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return redirect(f'/courses/{course.tutor_id.id}')

def delete_course(request, id):
    try:
        course = Course_Info.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No course found with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    tutor_id = course.tutor_id.id
    course.delete()
    return redirect(f'/courses/{tutor_id}')
