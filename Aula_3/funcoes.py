database = []

def abrir_chamado(lab, descricao, prioridade):
    if prioridade < 1 or prioridade > 10:
        print("Erro: A prioridade deve ser entre 1 e 10.")
        return False
    
    chamado = {
        "lab": lab,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto",
        "status": "Finalizado"
    }

    database.append(chamado)
    print("Chamado aberto com sucesso!")
    return True

def listar_chamados(database):
    print("\n--- TODOS OS CHAMADOS ---")
    for c in database:
        print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")

def fechar_chamado(database):
    print("Selecione o chamado a ser finalizado:")
    numero = int(input("Número do chamado: "))
    if 0 <= numero < len(database):
        database[numero]['status'] = 'Finalizado'
        print("Chamado finalizado com sucesso!")
    else:
        print("Número de chamado inválido.")

        #Outra forma de fazer a função fechar_chamado
# def fechar_chamado:
# idx = int(input("Qual o indice do chamado a ser fechado? "))
# if 0 <= idx < len(database):
#     database[idx]["status"] = "Finalizado"
#     print("Chamado finalizado com sucesso!")
# else:
#     print("Índice inválido.")

# def listar_chamados(database):
#     if not database
#     print("Nenhum chamado encontrado.")
#     return