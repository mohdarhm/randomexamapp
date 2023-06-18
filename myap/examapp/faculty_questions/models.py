from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission




class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'

class Concept(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'concept'

