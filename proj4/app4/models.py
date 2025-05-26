from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    credits = models.IntegerField()
    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    sem = models.IntegerField()
    enrollments = models.ManyToManyField(Course)
    def __str__(self):
        return f"{self.name} ({self.usn})"