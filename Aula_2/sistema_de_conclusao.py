while True:
    print("\n--- HELP DESK TÉCNICO ---")
    print("1. Novo Chamado")
    print("2. Listar Chamados")
    print("3. Finalizar Chamado")
    print("0. Sair")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        l = input("Laboratório: ")
        d = input("Descrição do problema: ")
        p = int(input("Prioridade (1-10): "))
        abrir_chamado(l, d, p)
    elif opcao == "2":
        print("\n--- TODOS OS CHAMADOS ---")
        for c in database:
            print(f"[{c['status']}] Lab: {c['lab']} - {c['descricao']} (Prioridade: {c['prioridade']})")
    # elif opcao == "3":
    #     print()
    elif opcao == "0":
        print("Desligamento sistema...")
        break