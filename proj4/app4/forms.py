from django import forms
from .models import Student, Course

class StudentRegistrationForm(forms.Form):
	name = forms.CharField(max_length=50)
	usn = forms.CharField(max_length=10)
	sem = forms.IntegerField()
	enrollments = forms.ModelMultipleChoiceField(
		queryset=Course.objects.all(),
		widget = forms.CheckboxSelectMultiple,
		label = "Select courses"
    )

class CourseSelectionForm(forms.Form):
	course = forms.ModelChoiceField(queryset=Course.objects.all(), label = "Select Course")