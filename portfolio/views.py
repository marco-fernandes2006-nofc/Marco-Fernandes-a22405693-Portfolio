from django.shortcuts import render, redirect
from .models import *
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required

# ======================
# LICENCIATURA
# ======================
def licenciaturas_view(request):
    
    licenciaturas = Licenciatura.objects.all()

    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

# ======================
# UNIDADE CURRICULAR
# ======================
def unidade_curricular_view(request, id):

    unidade_curricular = UnidadeCurricular.objects.get(id=id)

    return render(request, 'portfolio/unidade_curricular.html', {'unidade_curricular': unidade_curricular})

# ======================
# PROJETO
# ======================
def projetos_view(request):

    projetos = Projeto.objects.all()

    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

@login_required
def editar_projeto_view(request, id) :

    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def criar_projeto_view(request):

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save()
            return redirect('projeto', id=projeto.id)
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/criar_projeto.html', {'form': form})

@login_required
def apagar_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)
    projeto.delete()
    return redirect('projetos')

# ======================
# TECNOLOGIA
# ======================

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias, 'gestor': is_gestor(request.user)})

def tecnologia_view(request, id):

    tecnologia = Tecnologia.objects.get(id=id)

    return render(request, 'portfolio/tecnologia.html', {'tecnologia': tecnologia, 'gestor': is_gestor(request.user)})

@login_required
def editar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologia', id=id)
    else:
        form = TecnologiaForm(instance=tecnologia)
    
    return render(request, 'portfolio/editar_tecnologia.html', {'form':form, 'tecnologia':tecnologia})

@login_required
def criar_tecnologia_view(request):
    
    if request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            tecnologia = form.save()
            return redirect('tecnologia', id=tecnologia.id)
    else:
        form = TecnologiaForm()
    
    return render(request, 'portfolio/criar_tecnologia.html', {'form':form})

@login_required
def apagar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    tecnologia.delete()
    return redirect('tecnologias')

# ======================
# TFCs
# ======================
def tfcs_view(request):

    tfcs = TFC.objects.all()

    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

# ======================
# COMPETÊNCIAS
# ======================
def competencias_view(request):

    competencias = Competencia.objects.all()

    return render(request, 'portfolio/competencias.html', {'competencias': competencias, 'gestor': is_gestor(request.user)})

@login_required
def editar_competencia_view(request, id):
    
    competencia = Competencia.objects.get(id=id)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    
    return render(request, 'portfolio/editar_competencia.html', {'form': form, 'competencia': competencia})

@login_required
def criar_competencia_view(request):
    
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()

    return render(request, 'portfolio/criar_competencia.html', {'form': form})

@login_required
def apagar_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    competencia.delete()
    return redirect('competencias')

# ======================
# FORMAÇÕES
# ======================
def formacoes_view(request):

    formacoes = Formacao.objects.all()

    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes, 'gestor': is_gestor(request.user)})

@login_required
def editar_formacao_view(request, id):
    
    formacao = Formacao.objects.get(id=id)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portfolio/editar_formacao.html', {'form': form, 'formacao': formacao})

@login_required
def criar_formacao_view(request):

    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()
    
    return render(request, 'portfolio/criar_formacao.html', {'form': form})

@login_required
def apagar_formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)
    formacao.delete()
    return redirect('formacoes')

# ======================
# MAKING OFs
# ======================
def makingofs_view(request):

    makingofs = MakingOf.objects.all()

    return render(request, 'portfolio/makingofs.html', {'makingofs': makingofs})

def makingof_view(request, id):

    makingof = MakingOf.objects.get(id=id)

    return render(request, 'portfolio/makingof.html', {'makingof': makingof})

# ======================
# CONTRIBUIÇÕES OPEN SOURCE
# ======================
def contribuicoes_view(request):

    contribuicoes = ContribuicaoOpenSource.objects.all()

    return render(request, 'portfolio/contribuicoes.html', {'contribuicoes': contribuicoes})

# ======================
# LANDING PAGE
# ======================
def landing_page_view(request):
    
    tecnologias = [ tec for tec in Tecnologia.objects.all() if tec.portfolio ]
    makingofs = [ makingof for makingof in MakingOf.objects.all() if makingof.portfolio ]

    conteudo = {
        'tecnologias': tecnologias,
        'makingofs': makingofs,
        'markdown1': """
# Sobre esta Aplicação

## Modelação

""",
        'markdown2': """
## Tecnologias

""",
        'markdown3': """
## Repositório Github

[Repositório](https://github.com/marco-fernandes2006-nofc/Marco-Fernandes-a22405693-Portfolio)

## Making-OFs

"""
        
    }
    
    return render(request, 'portfolio/landing_page.html', {'conteudo': conteudo})

# ======================
# UTILS
# ======================

def is_gestor(user):
    return user.groups.filter(name="gestor").exists()