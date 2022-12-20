from rest_framework import serializers  
from app.models import *

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):

    direccion = DireccionSerializer(read_only=False,many=False)

    class Meta:
        model = Institucion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    direccion = DireccionSerializer(read_only=False,many=False)
    institucion = InstitucionSerializer(read_only=False,many=False)

    class Meta:
        model = User
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):

    id = UserSerializer(read_only=False,many=False)

    class Meta:
        model = Profesor
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):

    id = UserSerializer(read_only=False,many=False)
    curso = CursoSerializer(read_only=False,many=False)

    class Meta:
        model = Alumno
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asignatura
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calificacion
        fields = '__all__'    





