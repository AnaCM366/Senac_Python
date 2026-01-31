from django.http import HttpResponse
from django.shortcuts import render

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]
def home(request):
    return render(request, "core/home.html")

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

def novo_chamado(request):
    return render(request, "core/novoChamado.html")