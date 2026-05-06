#cria o arquivo logo início para garantir que ele esteja criado para funcionar tudo corretamente
arquivo= open("Arquivo_de_usuario.txt", "a")
arquivo.close()
#cria o arquivo de filmes logo no início também para garantir o funcionamento correto
arquivo= open("Arquivo_de_filmes.txt", "a")
arquivo.close()

def verificar_login(email_digitado, senha_digitada):
    arquivo = open("Arquivo_de_usuario.txt", "r")
    sucesso = False
    for linha in arquivo:
        dados = linha.strip().split("\t")
        #if len(dados) == 2: limita a leitura a duas informações
        if len(dados) == 2:
            email_salvo = dados[0]
            senha_salva = dados[1]
            if email_digitado == email_salvo and senha_digitada == senha_salva:
                sucesso = True
    
    arquivo.close()
    #valida a informação contida no login
    if sucesso == True:
        return True
    else:
        return False

while True:
    print("DURAMTUNA")
    print("- cadastro")
    print("- login")
    opcao = input("Digite a opção desejada: ")

    if opcao == "cadastro":
        email = input("Por favor, digite o seu email: ")
        senha = input("Boa! Agora crie uma senha: ")
        
        #abre o arquivo e regustra os dados
        arquivo = open("Arquivo_de_usuario.txt", "a")
        arquivo.write(email + "\t" + senha + "\n")
        arquivo.close()
        
        print("Usuário cadastrado com sucesso!")

    elif opcao == "login":
        email_login = input("Digite o email cadastrado: ")
        senha_login = input("Boa! Agora digite a sua senha: ")

        if verificar_login(email_login, senha_login):
            print("Bem-vindo ao menu de filmes.")
            #arquivo de filmes
            break 
        else:
            print("E-mail ou senha incorretos. Tente outra vez.")