from django.urls import path, include
from . import views

urlpatterns = [
    path('artigos/', views.artigos_view, name='artigos'),
    path('artigos/<int:id>/', views.artigo_view, name='artigo'),
    path('artigos/<int:id>/editar', views.editar_artigo_view, name='editar_artigo'),
    path('artigos/<int:id>/apagar', views.apagar_artigo, name='apagar_artigo'),
    path('artigos/criar', views.criar_artigo_view, name='criar_artigo'),
    path('artigos/<int:id>/like', views.like_artigo_view, name='like_artigo'),
    path('artigos/<int:id>/comentar', views.criar_comentario_view, name='comentar')
]