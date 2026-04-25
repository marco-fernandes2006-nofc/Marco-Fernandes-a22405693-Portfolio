## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('licenciaturas/', views.licenciaturas_view, name="licenciaturas"),
    path('', views.licenciaturas_view),   #  rota que abre diretamente a página das licenciaturas
    
    path('unidadecurricular/<int:id>', views.unidade_curricular_view, name="unidade_curricular"),

    path('projetos/', views.projetos_view, name="projetos"),

    path('tecnologia/<int:id>', views.tecnologia_view, name="tecnologia"),

    path('tfcs/', views.tfcs_view, name="tfcs"),

    path('competencias/', views.competencias_view, name="competencias"),

    path('formacoes/', views.formacoes_view, name="formacoes"),

    path('makingofs/', views.makingofs_view, name="makingofs"),

    path('makingofs/<int:id>', views.makingof_view, name="makingof"),

    path('contribuicoes/', views.contribuicoes_view, name="contribuicoes"),
]