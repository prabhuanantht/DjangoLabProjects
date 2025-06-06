from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = "listview.html"
    context_object_name = "students"

class StudentDetailView(DetailView):
    model = Student
    template_name = "detailview.html"
    context_object_name = "student"