from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    dur  = models.PositiveIntegerField()
    cred = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    sem = models.PositiveIntegerField()
    date = models.DateField(null = True)
    courses = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name
    
