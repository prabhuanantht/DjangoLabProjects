from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    lang = models.TextField()
    dur = models.PositiveIntegerField()
    def __str__(self):
        return self.name