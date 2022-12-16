from django.shortcuts import render
from app.models import *
from .serializers import ProfesorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404



def panelAlumno(request,id):
    alumno = Alumno.objects.get(id=id)

    datos = {'alumno':alumno}
    return render(request,'panelAlumno.html',datos)


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