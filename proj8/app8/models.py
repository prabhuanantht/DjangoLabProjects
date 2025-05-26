from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    sem = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
