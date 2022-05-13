from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Student

@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')

@login_required(login_url='/')
def addStudent(request):
    return render(request, 'Hod/addStudent.html')

@login_required(login_url='/')
def viewStudents(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request, 'Hod/viewStudents.html', context)

@login_required(login_url='/')
def timeTable(request):
    return render(request, 'Hod/timeTable.html')