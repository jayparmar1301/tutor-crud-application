from django.urls import path
from . import  views

urlpatterns = [
    path('', views.homepage),
    path('add', views.add_tutor_page),
    path('add/tutor', views.add_tutor),
    path('add/tutor/id={id}', views.edit_tutor),
    path('delete', views.delete_tutor),
    path('update', views.update_tutor)
]
