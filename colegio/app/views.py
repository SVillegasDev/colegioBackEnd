from django.shortcuts import render 
from app.models import *

def panelAlumno(request,id):
    alumno = Alumno.objects.get(id=id)

    datos = {'alumno':alumno}
    return render(request,'panelAlumno.html',datos)