from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import Chamado
from django.contrib.auth.decorators import login_required

from .models import Categoria

chamados = [
    {"id": 1, "laboratorio": "Lab 01", "problema": "Computador não liga", "prioridade": "Alta", "data_criacao": "2024-01-10 14:30"},
    {"id": 2, "laboratorio": "Lab 02", "problema": "Internet lenta", "prioridade": "Média", "data_criacao": "2024-01-11 09:15"},
    {"id": 3, "laboratorio": "Lab 03", "problema": "Impressora sem tinta", "prioridade": "Baixa", "data_criacao": "2024-01-12 11:45"},
]

categorias = [
    {"id": 1, "nome": "Hardware"},
    {"id": 2, "nome": "Software"},
    {"id": 3, "nome": "Rede"},
]

def home(request):
    return render(request, 'core/home.html')

def novo_chamado(request): 
    # 1. Se o usuário clicou no botão de enviar (POST)
    if request.method == "POST":
        # Capturamos os dados do formulário
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        # Salvamos na nossa "base de dados"
        print(f"Recebido: {laboratorio}, {descricao}, {prioridade}") 

        chamados.append({
            "id": len(chamados) + 1,
            "laboratorio": laboratorio,
            "descricao": descricao,
            "prioridade": prioridade
        })

        # 2. Redireciona de volta para a lista após salvar
        return redirect('/listar-chamados')

    # 3. Se o usuário apenas acessou a página (GET)
    return render(request, 'core/novo_chamado.html')
   

def fechar(request, id):
    for chamado in chamados:
        if chamado["id"] == id:
            chamados.remove(chamado)
            break
    
    return redirect('/listar')

def listar_chamados(request):
    return render(request, 'core/listar.html', {"chamados": chamados})




# Novas views para categorias

def listar_categorias(request):
    return render(request, 'core/listar_categorias.html', {"categorias": categorias})

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        categorias.append({
            "id": len(categorias) + 1,
            "nome": nome
        })
        # salvar meus dados
        return redirect('/listar-categorias')
    return render(request, 'core/nova_categoria.html')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == "POST":
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect('/lista_categorias')
    if request.method == "GET":
        return render(request, "core/editar_categoria.html", {"categoria": categoria})

def excluir_categoria(request, id):
    for categoria in categorias:
        if categoria["id"] == id:
            categorias.remove(categoria)
            break
    return redirect('/listar-categorias')