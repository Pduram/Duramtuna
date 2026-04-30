#menu inicial
def buscar_linha(Arquivo_de_usuario, usuario_senha):
    for login in Arquivo_de_usuario:
         Arquivo.open("Arquivo_de_usuario.txt","r")
cadastro = []
while True:
    print("DURAMTUNA")
    print("- cadastro")
    print("- login")
    opcao = input("Digite a opção desejada: ")

    if opcao == "cadastro":
        usuario_senha = []
        email = input("Por favor, digite o seu email: ")
        senha = input("Perfeito! Agora crie uma senha: ")
        usuario_senha.append(email)
        usuario_senha.append(senha)
        cadastro.append(usuario_senha)
        #abre o arquivo, salva a lista usuario_senha e fecha o arquivo
        Arquivo = open("Arquivo_de_usuario.txt", "w")
        Arquivo.write(f"{usuario_senha[0]}\t{usuario_senha[1]}\n")
        Arquivo.close()
    elif opcao == "login":
        email = input("Digite o email cadastrado: ")
        senha = input("Boa! Agora digite a sua senha: ")
        #define uma função para ler cada linha do arquivo
        if buscar_linha == usuario_senha:
            #abre arquivo de filmes
            print("filmes")
        else:
            print("Tente outra vez")

#menu de filmes
print("arquivo de filmes")