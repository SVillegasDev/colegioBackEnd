from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=20,default='')
    apellido = models.CharField(max_length=20,default='')
    curso = models.CharField(max_length=30,default='')
    userName = models.CharField(max_length=30,default='')
    password = models.CharField(max_length=50,default='')

class Profesor(models.Model):
    nombre = models.CharField(max_length=20,default='')
    apellido = models.CharField(max_length=20,default='')
    titulo = models.CharField(max_length=30,default='')
    userName = models.CharField(max_length=30,default='')
    password = models.CharField(max_length=50,default='')
