"""colegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path("admin/", admin.site.urls),    
    path("panelAlumno/<int:id>",views.panelAlumno,name="panelAlumno"),
    path("panelCurso/",views.panelCurso,name='panelCurso'),    
    path("editarCurso/<int:id>",views.editarCurso,name='editarCurso'),
    path("borrarCurso/<int:id>",views.borrarCurso,name='borrarCurso'),
    path("panelAsignatura/",views.panelAsignatura,name='panelAsignatura'),
    path("editarAsignatura/<int:id>",views.editarAsignatura,name='editarAsignatura'),
    path("borrarAsignatura/<int:id>",views.borrarAsignatura,name='borrarAsignatura'),
    path("panelRegistroAlumno/",views.panelRegistroAlumno,name='panelRegistroAlumno'),
    path('panelAdministrador/', views.panelAdministrador),    
    path("profesores/",views.listaProfesor.as_view()),
    path("profesores/<int:pk>",views.listaProfesor.as_view()),
    #USER
    path("panelUser/",views.panelUser,name='panelUser'),
    path("user/", views.UserView.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
    #INSTITUCION
    path("panelInstitucion/",views.panelInstitucion,name='panelInstitucion'),
    path("institucion/", views.InstitucionView.as_view()),
    path("institucion/<int:pk>", views.InstitucionDetail.as_view()),
    #DIRECCION
    path("panelDireccion/",views.panelDireccion,name='panelDireccion'),
    path("direccion/", views.DireccionView.as_view()),
    path("direccion/<int:pk>", views.DireccionDetail.as_view()),
    #path("panelInstitucion/",views.panelInstitucion,name='panelInstitucion'),
    #path("eliminarDireccion/<int:id>",views.eliminarDireccion,name='eliminarDireccion'),
    #path("editarDireccion/<int:id>",views.editarDireccion,name='editarDireccion'),
    
]
