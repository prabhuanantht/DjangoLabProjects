from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table

# Create your views here.
def home(request):
    return render(request, 'layout.html')

def studentlist(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})

def csvdownload(request):
    students = Student.objects.all()
    resp = HttpResponse(content_type = 'text/csv')
    resp['Content-Disposition'] = 'attachment; filename = "students.csv"'
    writer = csv.writer(resp)
    writer.writerow(['Student Name', 'Student USN', 'Student Sem'])
    for student in students:
        writer.writerow([student.name, student.usn, student.sem])
    return resp

def pdfdownload(request):
    students = Student.objects.all()
    resp = HttpResponse(content_type = 'application/pdf')
    resp['Content-Disposition'] = 'attachment; filename = "students.pdf"'
    pdf = SimpleDocTemplate(resp, pagesize=A4)
    table_data = [['Student Name', 'Student USN', 'Student Sem']]
    for student in students:
        table_data.append([student.name, student.usn, student.sem])
    table = Table(table_data)
    pdf.build([table])
    return resp