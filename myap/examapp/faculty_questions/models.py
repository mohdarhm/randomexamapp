from django.db import models

# Create your models here.

class Concept(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    using='forfacultydata'

    class Meta:
        db_table='concept'

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    using='forfacultydata'
    class Meta:
        db_table='subject'