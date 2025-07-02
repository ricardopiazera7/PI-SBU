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
    senha = input("Senha: ")

    usuarios = carregar_usuarios()

    # Verifica se já existe alguém com o mesmo CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: já existe um usuário com esse CPF.")
            return

    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "senha": senha
    }

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
            print(f"Bem-vindo(a), {usuario['nome']}!")
            return True

    print("CPF ou senha incorretos.")
    return False
