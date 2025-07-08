import json

# Carrega os usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Salva os usuários no arquivo JSON
def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

# Cadastra um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    sexo = input("Sexo (M/F): ")
    senha = input("Senha (mínimo 4 caracteres): ")
    tipo = input("Tipo de usuário (Paciente ou Funcionario): ").strip().capitalize()

# Validação da senha e tipo de cadastro
    if len(senha) < 4:
        print("Erro: a senha deve ter no mínimo 4 caracteres.")
        return
    if tipo not in ["Paciente", "Funcionario"]:
        print("Erro: o tipo de usuário deve ser 'Paciente' ou 'Funcionario'.")
        return
    
    usuarios = carregar_usuarios()

    # Verifica se já existe alguém com o mesmo CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: já existe um usuário com esse CPF.")
            return

    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "sexo": sexo,
        "senha": senha,
        "tipo": tipo
    }
    # Se for funcionário, perguntar se é médico
    if tipo == "Funcionario":
        eh_medico = input("Deseja cadastrar este funcionário como médico? (s/n): ").strip().lower()
        if eh_medico == "s":
            crm = input("Digite o CRM (ex: SC-123456): ").strip().upper()
            # Pergunta a especialidade, valida para não ser vazia
            especialidade = input("Informe a especialidade médica: ").strip()
            if not especialidade:
                print("Erro: especialidade não pode ser vazia.")
                return
            # Validação simples do formato do CRM
            if not crm or "-" not in crm or not crm.split("-")[1].isdigit():
                print("Erro: CRM inválido. Deve seguir o formato UF-123456.")
                return

            # Verifica se já existe esse CRM cadastrado
            for usuario in usuarios:
                if usuario.get("crm") == crm:
                    print("Erro: já existe um médico com esse CRM.")
                    return



            novo_usuario["eh_medico"] = True
            novo_usuario["crm"] = crm
            novo_usuario["especialidade"] = especialidade
        else:
            novo_usuario["eh_medico"] = False
            
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

# Faz login de um usuário
def login():
    print("\n--- Login ---")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            print(f"\nBem-vindo(a), {usuario['nome']}! ({usuario['tipo']})")
            if usuario["tipo"] == "Funcionario":
                print("Acesso administrativo concedido.")
            else:
                print("Acesso de paciente.")
            return True

    print("CPF ou senha incorretos.")
    return False
