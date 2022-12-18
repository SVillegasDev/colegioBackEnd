from django import forms
from app import models

formatoFecha = [
    '%d/%m/%Y %H:%M:%S',    
    '%d/%m/%Y %H:%M',      
    '%d/%m/%Y',            
    '%d/%m/%y %H:%M:%S',   
    '%d/%m/%y %H:%M',      
    '%d/%m/%y',   
    '%d-%m-%Y %H:%M:%S',   
    '%d-%m-%Y %H:%M',      
    '%d-%m-%Y',            
    '%d-%m-%y %H:%M:%S',   
    '%d-%m-%y %H:%M',      
    '%d-%m-%y'             
    ]

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = models.Profesor
        fields = '__all__'

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=45,required=True)

class AsignaturaForm(forms.Form):
    nombre = forms.CharField(max_length=45,required=True)

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=45,label='Nombre',required=True)
    apellidoPaterno = forms.CharField(max_length=45,label='Apellido paterno',required=True)
    apellidoMaterno = forms.CharField(max_length=45,label='Apellido materno',required=False)
    nacimiento = forms.DateTimeField(label='Fecha Nacimiento',required=True,input_formats=formatoFecha)

    ciudad = forms.CharField(max_length=45,label='Ciudad',required=True)
    calle = forms.CharField(max_length=45,label='Calle',required=True)
    numero = forms.CharField(max_length=45,label='Numero',required=False)

    institucion = forms.ModelMultipleChoiceField(queryset=models.Institucion.objects.all())
    curso = forms.ModelMultipleChoiceField(queryset=models.Curso.objects.all())
    password = forms.CharField(max_length=45,label='Contraseña',required=True)

