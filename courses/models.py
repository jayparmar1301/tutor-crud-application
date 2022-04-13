from django.db import models
from tutor.models import Tutor_Info

class Course_Info(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=250)
    course_duration = models.IntegerField(blank=True, null=True)
    tutor_id = models.ForeignKey(Tutor_Info, on_delete=models.CASCADE)

