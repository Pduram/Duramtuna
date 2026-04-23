#menu inicial
while True:
    print("DURAMTUNA")
    print("- cadastro")
    print("- login")
    opcao = input("Digite a opção desejada: ")

    if opcao == "cadastro":
        email = input("Por favor, digite o seu email: ")
        #salva a email o arquivo
        senha = input("Perfeito! Agora crie uma senha: ")
        #armazena senha no arquivo    
    elif opcao == "login":
        email = input("Digite o email cadastrado: ")
        #procura o email digitado no arquivo
        if email == "salvo":
            senha = input("Boa! Agora digite a sua senha: ")
            if senha == "password":
                break
            #arquivo de filmes
            else:
                print("Tente outra vez")

#menu de filmes
print("arquivo de filmes")