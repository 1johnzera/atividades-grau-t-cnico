nome_usuario = input("Insira o seu usuario: ")
senha_usuario = input("Insira a sua senha: ")

while nome_usuario == senha_usuario:
    print("Você não pode utilizar as mesmas credenciais no usuario e senha.")

    nome_usuario = input("Insira o usuario novamente: ")
    senha_usuario = input("Insia a senha novamente: ")