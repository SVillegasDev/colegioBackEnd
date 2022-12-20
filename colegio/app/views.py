from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from .serializers import ProfesorSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from datetime import datetime

formatosFecha = ['%d/%m/%Y %H:%M:%S','%d/%m/%Y %H:%M','%d/%m/%Y','%d/%m/%y %H:%M:%S','%d/%m/%y %H:%M','%d/%m/%y','%d-%m-%Y %H:%M:%S','%d-%m-%Y %H:%M','%d-%m-%Y','%d-%m-%y %H:%M:%S','%d-%m-%y %H:%M','%d-%m-%y']

def formatFecha(fecha):
    newFecha = None
    for f in formatosFecha:
        try:
            newFecha = datetime.strptime(fecha,f)
            break
        except:
            continue
    if(newFecha != None):
        return newFecha
    
def panelAlumno(request,id):
    alumno = AlumnoForm()
    datos = {'form':alumno}
    return render(request,'panelAlumno.html',datos)

def panelRegistroAlumno(request):
    formAlumno = AlumnoForm()
    alumnos = Alumno.objects.all()
    if request.method == 'POST':
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            nombre = formAlumno['nombre'].value()
            apellidoPaterno = formAlumno['apellidoPaterno'].value()
            apellidoMaterno = formAlumno['apellidoMaterno'].value()
            fecha = formAlumno['nacimiento'].value()
            nacimiento = formatFecha(fecha)
            ciudad = formAlumno['ciudad'].value()
            calle = formAlumno['calle'].value()
            numero = formAlumno['numero'].value()
            institucionForm = formAlumno['institucion'].value()
            cursoForm = formAlumno['curso'].value()
            password = formAlumno['password'].value()
            curso = Curso.objects.get(id=cursoForm[0])
            institucion = Institucion.objects.get(id=institucionForm[0])
            direccion = Direccion()
            direccion.ciudad = ciudad
            direccion.calle = calle
            if numero.isnumeric():
                direccion.numero = numero
            direccion.save()
            direcciones = Direccion.objects.all()
            direccion = direcciones[len(direcciones)-1]

            usuario = User()
            usuario.username = nombre.strip()[0] + apellidoPaterno.strip() + fecha[3:5]
            usuario.password = password
            usuario.nombre = nombre
            usuario.apellidoPaterno = apellidoPaterno
            usuario.apellidoMaterno = apellidoMaterno
            usuario.direccion = direccion
            usuario.nacimiento = nacimiento
            usuario.institucion = institucion
            usuario.save()

            usuarios = User.objects.all()
            usuario = usuarios[len(usuarios) -1]
            alumno = Alumno()
            alumno.id = usuario
            alumno.curso = curso
            alumno.save()
            print("Usuario almacenado correctamente")

    datos = {'forms':formAlumno,'alumnos':alumnos}
    return render(request,'alumno/panelRegistroAlumno.html',datos)

def panelCurso(request):
    formCurso = CursoForm()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        curso = Curso()
        if( len(nombre) > 0 ):
            curso.nombre = nombre
            respuesta = curso.save()
            curso = Curso.objects.all()
    datos = {'form':formCurso,'cursos':cursos}
    return render(request,'curso/panelCurso.html',datos)

def editarCurso(**id):
    curso = Curso.objects.get(id=id)
    print(curso.nombre)

def borrarCurso(**id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('../panelCurso')

def panelAsignatura(request):
    formAsignatura = AsignaturaForm()
    asignaturas = Asignatura.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nombre = ((nombre).upper()).strip()
        asignatura = Asignatura()
        if( len(nombre) > 0 ):
            asignatura.nombre = nombre
            asignatura.save()
    datos = {'form':formAsignatura,'asignaturas':asignaturas}
    return render(request,'asignatura/panelAsignatura.html',datos)

def editarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    print(asignatura.nombre)

def borrarAsignatura(**kwargs):
    asignatura = Asignatura.objects.get(id=kwargs['id'])
    asignatura.delete()
    return redirect('../panelAsignatura')

def panelCalificacion(request):
    formCalificaciones = CalificacionForm()
    datos = {'forms':formCalificaciones}
    try:
        action = request.POST['action']
        if action == 'cursoAlumnos':
            data = []
            for alum in Alumno.objects.all():
                if(str(alum.curso.id) == request.POST['id']):
                    data.append({'id':alum.id.id,'nombre':alum.id.nombre,'apellidoPaterno':alum.id.apellidoPaterno,'apellidoMaterno':alum.id.apellidoMaterno,'promedio':alum.promedio})
            return JsonResponse(data,safe=False)
        else:
           print("ha ocurrido un error")  
    except Exception as e:
        print("error\n---> "+str(e))
    return render(request,'calificacion/panelCalificacion.html',datos)

def panelAdministrador(request):
    return render(request, 'panelAdministrador.html')


class listaProfesor(APIView):
    def get(self, request):
        profesor = Profesor.objects.all()
        serializer = ProfesorSerializer(profesor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfesorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleProfesor(APIView):
    def get_object(self, pk):
        try:
            return Profesor.objects.get(pk=pk)
        except Profesor.DoesNotExist:
            return Http404
    def get(self, request, pk):
        profesor = self.get_object(pk)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(self, request, pk):
    profesor = self.get_object(pk)
    profesor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)