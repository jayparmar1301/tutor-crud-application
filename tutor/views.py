from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse('Homepage')

def edit_tutor(request):
    return HttpResponse('Edit')

def delete_tutor(request):
    return HttpResponse('Delete')

def update_tutor(request):
    return HttpResponse('Update')