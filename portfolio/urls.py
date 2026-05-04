## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('licenciaturas/', views.licenciaturas_view, name="licenciaturas"),
    
    path('unidadecurricular/<int:id>', views.unidade_curricular_view, name="unidade_curricular"),

    path('projetos/', views.projetos_view, name="projetos"),
    path('projetos/<int:id>/apagar/', views.apagar_projeto_view, name="apagar_projeto"),
    path('projetos/<int:id>/editar/', views.editar_projeto_view, name="editar_projeto"),
    path('projetos/criar/', views.criar_projeto_view, name="criar_projeto"),

    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('tecnologia/<int:id>', views.tecnologia_view, name="tecnologia"),
    path('tecnologia/<int:id>/editar/', views.editar_tecnologia_view, name="editar_tecnologia"),
    path('tecnologia/<int:id>/apagar/', views.apagar_tecnologia_view, name="apagar_tecnologia"),
    path('tecnologia/criar/', views.criar_tecnologia_view, name="criar_tecnologia"),

    path('tfcs/', views.tfcs_view, name="tfcs"),

    path('competencias/', views.competencias_view, name="competencias"),
    path('competencias/<int:id>/editar/', views.editar_competencia_view, name="editar_competencia"),
    path('competencias/<int:id>/apagar/', views.apagar_competencia_view, name="apagar_competencia"),
    path('competencias/criar/', views.criar_competencia_view, name="criar_competencia"),

    path('formacoes/', views.formacoes_view, name="formacoes"),
    path('formacoes/<int:id>/editar/', views.editar_formacao_view, name="editar_formacao"),
    path('formacoes/<int:id>/apagar/', views.apagar_formacao_view, name="apagar_formacao"),
    path('formacoes/criar/', views.criar_formacao_view, name="criar_formacao"),


    path('makingofs/', views.makingofs_view, name="makingofs"),
    path('makingofs/<int:id>', views.makingof_view, name="makingof"),

    path('contribuicoes/', views.contribuicoes_view, name="contribuicoes"),

    path('', views.landing_page_view, name="landing_page")
]