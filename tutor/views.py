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

def edit_tutor(request, id):
    id_id = id
    tutor = Tutor_Info.objects.get(id=id_id)
    return render(request, 'edit_tutor.html', context = {'tutor': tutor})

def delete_tutor(request):
    return HttpResponse('Delete')

def update_tutor(request, id):
    tutor = Tutor_Info.objects.get(id=id)
    tutor.first_name = request.GET.get('first_name') if request.GET.get('first_name')!= None else tutor.first_name
    tutor.last_name = request.GET.get('last_name') if request.GET.get('last_name')!= None else tutor.last_name
    tutor.email = request.GET.get('email') if request.GET.get('email')!= None else tutor.email
    tutor.tutor_skills = request.GET.get('tutor_skills') if request.GET.get('tutor_skills') else tutor.tutor_skills
    tutor.tutor_exp = request.GET.get('tutor_exp') if request.GET.get('tutor_exp') else tutor.tutor.exp
    tutor.save()
    return redirect('/tutor')
