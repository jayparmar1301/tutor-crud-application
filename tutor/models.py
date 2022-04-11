from django.db import models

# This is model related to tutor information
class Tutor_Info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tutor_skills = models.CharField(max_length=250, null=True)
    tutor_exp = models.IntegerField(blank=True, null=True)

