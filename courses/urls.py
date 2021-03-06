from django.urls import path
from . import  views

urlpatterns = [
    path('<int:id>', views.tutor_courses_homepage),
    
    path('add', views.add_course_page),
    path('add/new', views.add_new_course),

    path('edit/<int:id>', views.edit_course),
    path('edit/<int:id>/submit', views.update_course),

    path('delete/<int:id>', views.delete_course)
]
