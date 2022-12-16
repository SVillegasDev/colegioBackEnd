from django.shortcuts import render
from app.models import *
from .forms import ProfesorForm

def index(request):
    return render(request, 'index.html')

def panelAlumno(request,id):
    alumno = Alumno.objects.get(id=id)

    datos = {'alumno':alumno}
    return render(request,'panelAlumno.html',datos)

def agregarProfesor(request):



    data = {
        'form': ProfesorForm
    }

    if request.method == "POST":
        formulario = ProfesorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
        else:
            data["form"] = formulario

    return render(request, 'profesor/agregar.html', data)

