from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentRegistrationForm, CourseSelectionForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'student_list': students})

def courselist(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'course_list': courses})

def register(request):
    message = ""
    if request.method=="POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = Student(
                name = form.cleaned_data['name'],
                usn = form.cleaned_data['usn'],
                sem = form.cleaned_data['sem']
            )
            student.save()
            student.enrollments.set(form.cleaned_data['enrollments'])
            message = "Student registered and enrolled successfully"
    else:
        form = StudentRegistrationForm()
    return render(request, 'register.html', {'form':form, 'message':message})

def enrollmentlist(request):
    form = CourseSelectionForm(request.POST or None)
    selected_course = None
    student_list = None
    if request.method == "POST":
        if form.is_valid():
            selected_course = form.cleaned_data['course']
            student_list = Student.objects.filter(enrollments = selected_course)
    return render(request, 'enrollmentlist.html', {'form': form, 'course_name': selected_course, 'student_list': student_list})