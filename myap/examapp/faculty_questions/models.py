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



class Question(models.Model):
  

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    question_text = models.TextField()
    options = models.TextField()
    correct_answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'question'
        app_label= 'faculty_questions'
    def __str__(self):
        return self.question_text
    
