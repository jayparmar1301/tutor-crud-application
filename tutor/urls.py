from django.urls import path
from . import  views

urlpatterns = [
    path('', views.homepage),
    
    path('add', views.add_tutor_page),
    path('add/tutor', views.add_tutor),

    path('edit/<int:id>', views.edit_tutor),
    path('edit/<int:id>/submit', views.update_tutor),

    path('delete', views.delete_tutor)
]
