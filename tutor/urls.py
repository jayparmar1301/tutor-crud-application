from django.urls import path
from . import  views

urlpatterns = [
    path('', views.homepage),
    path('edit', views.edit_tutor),
    path('delete', views.delete_tutor),
    path('update', views.update_tutor)
]
