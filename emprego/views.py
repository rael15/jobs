from datetime import time

from django.shortcuts import render, redirect
from emprego.models import Empregos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.views.generic import RedirectView

# Create your views here.

def index(request):
    return redirect('/empregos/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def novo_emprego(request):
    id_emprego = request.GET.get('id')
    dados = {}
    if id_emprego:
        dados['emprego'] = Empregos.objects.get(id=id_emprego)
    return render(request, 'novo_emprego.html', dados)

def submit_emprego(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        empresa = request.POST.get('empresa')
        descricao = request.POST.get('descricao')
        data_emprego = request.POST.get('data_emprego')
        usuario = request.user
        id_emprego = request.POST.get('id_emprego')
        if id_emprego: #alteração
            Empregos.objects.filter(id=id_emprego).update(titulo=titulo,
                                                         empresa=empresa,
                                                         descricao=descricao,
                                                         data_emprego=data_emprego)

        else: #inclusão
            Empregos.objects.create(titulo=titulo,
                                    descricao=descricao,
                                    data_emprego=data_emprego,
                                    usuario=usuario)

    return redirect('/')

@login_required(login_url='/login')
def lista_empregos(request):
    # usuario = request.user  #(filtrar pelo usuario)
    # empregos = Empregos.objects.filter(usuario=usuario) #(filtrar pelo usuario)
    empregos = Empregos.objects.all()
    dados = {'empregos': empregos}
    return render(request, 'empregos.html', dados)

@login_required(login_url='/login')
def delete_emprego(request, id_emprego):
    usuario = request.user
    empregos = Empregos.objects.get(id=id_emprego)
    if usuario == empregos.usuario:
        empregos.delete()
    return redirect('/')
