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

def salvar_dados_json():
    try:
        with open(DATABASE_JSON_FILE, "w", encoding="utf-8") as arquivo:
            json.dump(database, arquivo, indent=4, ensure_ascii=False)

            return True
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo JSON: {e}")
        return False

def fechar_chamado(database):
    print("Selecione o chamado a ser finalizado:")
    numero = int(input("Número do chamado: "))
    if 0 <= numero < len(database):
        database[numero]['status'] = 'Finalizado'
        print("Chamado finalizado com sucesso!")
    else:
        print("Número de chamado inválido.")

def exportar_chamados():
    print("Informe quais chamados deseja exportar:")
    print("1. Todos os chamados")
    print("2. Chamados abertos")
    
    # Adicionado tratamento para caso o usuário não digite um número
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida.")
        return

    match escolha:
        case 1:
            funcoes.exportar_chamados(database, "todos_chamados.json")
        case 2:
            funcoes.exportar_chamados_abertos(database, "chamados_abertos.json")
        case _:
            print("Opção inválida.")
    
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