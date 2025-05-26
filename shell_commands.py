# Import the model
from myapp.models import Student

# -------------------------------
# CREATE
# -------------------------------

# Method 1: Instantiate and save
student1 = Student(name="Ananth", usn="4NI21CS001", sem=4)
student1.save()

# Method 2: Create directly
Student.objects.create(name="Chandan", usn="4NI21CS002", sem=4)

# -------------------------------
# READ
# -------------------------------

# Get all students
all_students = Student.objects.all()

# Filter students by sem
sem4_students = Student.objects.filter(sem=4)

# Get a student by ID
one_student = Student.objects.get(id=1)

# Get first student
first_student = Student.objects.first()

# Count number of students
count = Student.objects.count()

# -------------------------------
# UPDATE
# -------------------------------

# Method 1: Get and modify
s = Student.objects.get(usn="4NI21CS001")
s.name = "Ananth Prabhu"
s.sem = 5
s.save()

# Method 2: Bulk update using filter
Student.objects.filter(usn="4NI21CS002").update(sem=5)

# -------------------------------
# DELETE
# -------------------------------

# Method 1: Delete one object
s = Student.objects.get(usn="4NI21CS001")
s.delete()

# Method 2: Delete all students in 5th sem
Student.objects.filter(sem=5).delete()