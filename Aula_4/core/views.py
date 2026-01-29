from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello, world!</h1><p>Meu primeiro Django está online.</p>")

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]

def listar(request):
    return render(request, "core/listar.html", {"chamados": chamados})

def criar(request, lab, problema, prioridade):
    # Criando o dicionário e adicionando à lista
    novo = {
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
    }
    chamados.append(novo)

    return HttpResponse(f"<h1>Chamado para o {lab} criado com sucesso!</h1> <br> <a href='/'>Voltar</a>")