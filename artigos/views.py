from django.shortcuts import render, redirect
from .models import Artigo, Comentario
from django.contrib.auth.decorators import login_required
from .forms import ArtigoForm

def is_autor(artigo, user):
    return artigo.autor.id == user.id

def artigos_view(request):

    artigos = Artigo.objects.all()

    return render(request, "artigos/artigos.html", {"artigos": artigos})

def artigo_view(request, id):

    artigo = Artigo.objects.get(id=id)

    autor = is_autor(artigo, request.user)

    return render(request, "artigos/artigo.html", {'artigo': artigo, 'autor': autor})

@login_required
def editar_artigo_view(request, id):
    
    artigo = Artigo.objects.get(id=id)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            artigo = form.save()

            return redirect('artigo', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)

    return render(request, 'artigos/editar_artigo.html', {'form': form})

@login_required
def criar_artigo_view(request):
    
    if request.method == 'POST':
        form = ArtigoForm(request.POST)

        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()

            return redirect('artigo', id=artigo.id)
    else:
        form = ArtigoForm()
    
    return render(request, "artigos/criar_artigo.html", {'form': form})

@login_required
def apagar_artigo(request, id):

    artigo = Artigo.objects.get(id=id)

    artigo.delete()

    return redirect('artigos')

@login_required
def like_artigo_view(request, id):

    artigo = Artigo.objects.get(id=id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    return redirect('artigo', id=id)

@login_required
def criar_comentario_view(request, id):

    artigo = Artigo.objects.get(id=id)

    if request.method == 'POST':
        texto = request.POST.get('texto')

        Comentario.objects.create(
            texto=texto, 
            autor=request.user, 
            artigo=artigo
        )
        
    return redirect('artigo', id=id)
