#cria o arquivo logo início para garantir que ele esteja criado para funcionar tudo corretamente
arquivo= open("Arquivo_de_usuario.txt", "a")
arquivo.close()
#cria o arquivo de filmes logo no início também para garantir o funcionamento correto
arquivo= open("Arquivo_de_filmes.txt", "a", encoding='utf-8')
arquivo.write("Pulp-Fiction, em tempos de violencia""\n")
arquivo.write("Sr & Sra Smith""\n")
arquivo.write("Clube da luta""\n")
arquivo.write("Shrek 2""\n")
arquivo.write("Vingadores (2012)""\n")
arquivo.write("Vingadores era de Ultron""\n")
arquivo.write("Vingadores Guerra infinita""\n")
arquivo.write("Vingadores Ultimato""\n")
arquivo.write("Batman, eternamente""\n")
arquivo.write("Batman, o cavaleiro das trevas")
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
            while True:
                print("1 - Acessar catálogo completo")
                print("2 - Pequisar Filmes")
                cat_filmes = input("Escolha a ação desejada: ")
                if cat_filmes == "1":
                    print(" Catálogo de Filmes ")
                    arquivo = open("Arquivo_de_filmes.txt", "r", encoding='utf-8')
                    print(arquivo.read())
                    arquivo.close() # Importante fechar após ler

                elif cat_filmes == "2":
                    filme_procurado = input("Digite o título do filme: ").strip().lower()
                    encontrado = False
                    arquivo = open("Arquivo_de_filmes.txt", "r", encoding='utf-8')
                    print(f"Resultados para '{filme_procurado}':")
                    for linha in arquivo:
                        # Verifica se o termo pesquisado está contido na linha (tudo em minúsculo)
                        if filme_procurado in linha.lower():
                            print(f"Encontrado: {linha.strip()}")
                            encontrado = True
                    
                    arquivo.close() # Importante fechar após percorrer o loop
                    
                    if not encontrado:
                        print("Nenhum filme encontrado com esse título.")

            #arquivo de filmes
            break 
        else:
            print("E-mail ou senha incorretos. Tente outra vez.")