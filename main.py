from funcoes import cadastrar_usuario, login

def menu_inicial():
    while True:
        print("\n===== Clínica Médica - Sistema Inicial =====")
        print("1. Cadastrar novo usuário")
        print("2. Fazer login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            sucesso = login()
            if sucesso:
                print("Login bem-sucedido. (menu principal do sistema)")
        elif opcao == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_inicial()
