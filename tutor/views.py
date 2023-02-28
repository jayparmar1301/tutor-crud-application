from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Tutor_Info
from django.core.exceptions import ObjectDoesNotExist

def homepage(request):
    tutor_info = Tutor_Info.objects.all()
    return render(request, 'homepage.html', context = {'tutors': tutor_info})

def add_tutor(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    tutor_skills = request.GET.get('tutor_skills')
    tutor_exp = request.GET.get('tutor_exp')
    try:
        Tutor_Info.objects.create(first_name=first_name,
                                last_name = last_name,
                                email = email,
                                tutor_skills = tutor_skills,
                                tutor_exp = tutor_exp)
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return redirect('/tutor')

def add_tutor_page(request):
    return render(request, 'add_tutor.html')

def edit_tutor(request, id):
    try:
        tutor = Tutor_Info.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No tutor with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return render(request, 'edit_tutor.html', context = {'tutor': tutor})

def delete_tutor(request, id):
    try:
        tutor = Tutor_Info.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No tutor with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    tutor.delete()
    return redirect('/tutor')

def update_tutor(request, id):
    try:
        tutor = Tutor_Info.objects.get(id=id)
        tutor.first_name = request.GET.get('first_name') if request.GET.get('first_name') is not None else tutor.first_name
        tutor.last_name = request.GET.get('last_name') if request.GET.get('last_name') is not None else tutor.last_name
        tutor.tutor_skills = request.GET.get('tutor_skills') if request.GET.get('tutor_skills') else tutor.tutor_skills
        tutor.tutor_exp = request.GET.get('tutor_exp') if request.GET.get('tutor_exp') else tutor.tutor.exp
        tutor.save()
    except ObjectDoesNotExist:
        return render(request, 'exception_page.html', context = {'error':  'No tutor with this info' })
    except Exception as ex:
        return render(request, 'exception_page.html', context = {'error':  ex })

    return redirect('/tutor')
