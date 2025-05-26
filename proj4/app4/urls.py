
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name = "home"),
    path('home/', views.homepage, name = "home"),
    path('studentlist/', views.studentlist, name = "studentlist"),
    path('courselist/', views.courselist, name = "courselist"),
    path('register/', views.register, name = "register"),
    path('enrollmentlist/', views.enrollmentlist, name = "enrollmentlist"),
]
