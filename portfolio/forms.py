from django import forms

from .models import Projeto, Tecnologia, Competencia, Formacao


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'conceitos_aplicados', 'data_realizacao', 'tecnologias', 'unidade_curricular']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'tipo', 'descricao', 'logo', 'website_oficial', 'portfolio']


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'descricao', 'nivel']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['titulo', 'instituicao', 'tipo', 'descricao', 'data_inicio', 'data_fim']