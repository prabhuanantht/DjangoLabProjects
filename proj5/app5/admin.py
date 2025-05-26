from django.contrib import admin
from .models import Student, Course
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'usn', 'sem',)
    search_fields = ('name', 'usn',)
    list_filter = ('sem',) 
    ordering= ('name',)
    date_hierarchy = 'date'
    filter_vertical = ('courses',) # for many to many fields only

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'dur', 'cred')
    search_fields = ('name',)
    list_filter = ('dur',)
    ordering = ('cred',)
    # raw_id_fields = ('course',) #for foreign keys only

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)