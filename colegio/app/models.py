from django.db import models
from django.contrib.auth.models import User  


# Create your models here.
class Direccion(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    ciudad = models.CharField(max_length=45,null=False,default='')
    calle = models.CharField(max_length=45,null=False)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return self.ciudad + ", " + self.calle 

class Institucion(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    nombre = models.CharField(max_length=45,null=False,default='')
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.nombre

class User(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    username = models.CharField(max_length=45,null=False,default='')
    password = models.CharField(max_length=45,null=False,default='')
    nombre = models.CharField(max_length=45,null=False,default='')
    apellidoPaterno = models.CharField(max_length=45,null=False,default='')
    apellidoMaterno = models.CharField(max_length=45,null=True,default='')
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    nacimiento = models.DateTimeField(null=True)
    estado = models.BooleanField(null=False,default=True)
    institucion = models.ForeignKey(Institucion,on_delete=models.CASCADE,null=False,default='')

class Profesor(models.Model):
    id = models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE,null=False,default='')
    titulo = models.CharField(max_length=45,null=True,default='')
    puntuacion = models.CharField(max_length=45,null=True,default='')

class Curso(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    nombre = models.CharField(max_length=45,null=False,default='')

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    promedio = models.FloatField(null=False,default=7.0)

class Asignatura(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    nombre = models.CharField(max_length=45,null=False)

class Calificacion(models.Model):
    id = models.BigAutoField(auto_created=True,primary_key=True)
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False,default='')
    nota = models.FloatField(null=False,default='')


