from django.shortcuts import render
from .models import *

def licenciaturas_view(request):
    
    licenciaturas = Licenciatura.objects.all()

    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def unidade_curricular_view(request, id):

    unidade_curricular = UnidadeCurricular.objects.get(id=id)

    return render(request, 'portfolio/unidade_curricular.html', {'unidade_curricular': unidade_curricular})

def projetos_view(request):

    projetos = Projeto.objects.all()

    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tecnologia_view(request, id):

    tecnologia = Tecnologia.objects.get(id=id)

    return render(request, 'portfolio/tecnologia.html', {'tecnologia': tecnologia})

def tfcs_view(request):

    tfcs = TFC.objects.all()

    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):

    competencias = Competencia.objects.all()

    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):

    formacoes = Formacao.objects.all()

    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def makingofs_view(request):

    makingofs = MakingOf.objects.all()

    return render(request, 'portfolio/makingofs.html', {'makingofs': makingofs})

def makingof_view(request, id):

    makingof = MakingOf.objects.get(id=id)

    return render(request, 'portfolio/makingof.html', {'makingof': makingof})

def contribuicoes_view(request):

    contribuicoes = ContribuicaoOpenSource.objects.all()

    return render(request, 'portfolio/contribuicoes.html', {'contribuicoes': contribuicoes})