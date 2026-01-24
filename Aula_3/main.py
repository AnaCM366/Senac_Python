from unittest import case
from funcoes import fechar_chamado
from funcoes import *
import funcoes

while True:
    print("\n--- HELP DESK TÉCNICO ---")
    print("1. Novo Chamado")
    print("2. Listar Chamados")
    print("3. Finalizar Chamado")
    print("0. Sair")

    opcao = int(input("Escolha uma ação: "))
    match opcao:
        case 1:
            l = input("Laboratório: ")
            d = input("Descrição do problema: ")
            p = int(input("Prioridade (1-10): "))
            abrir_chamado(l, d, p)

        case 2:
            listar_chamados(database)

        case 3:
            fechar_chamado(database)

        case 0:
            print("Desligamento sistema...")
            break