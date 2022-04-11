from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Tutor_Info

def homepage(request):
    tutor_info = Tutor_Info.objects.all()
    return render(request, 'homepage.html', context = {'tutors': tutor_info})

def add_tutor(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    tutor_skills = request.GET.get('tutor_skills')
    tutor_exp = request.GET.get('tutor_exp')
    Tutor_Info.objects.create(first_name=first_name,
                            last_name = last_name,
                            email = email,
                            tutor_skills = tutor_skills,
                            tutor_exp = tutor_exp)

    return redirect('/tutor')

def add_tutor_page(request):
    return render(request, 'add_tutor.html')

def edit_tutor(request):
    return HttpResponse('Edit')

def delete_tutor(request):
    return HttpResponse('Delete')

def update_tutor(request):
    return HttpResponse('Update')