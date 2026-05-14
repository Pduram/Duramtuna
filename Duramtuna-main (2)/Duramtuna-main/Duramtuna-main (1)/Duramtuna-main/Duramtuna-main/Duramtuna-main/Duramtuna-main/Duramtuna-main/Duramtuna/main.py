# Garante que os arquivos base existam ao iniciar o programa.
# O modo "a" (append) cria o arquivo caso ele nao exista, sem apagar o conteudo existente.
# O primeiro arquivo guarda os usuarios cadastrados (email e senha).
# O segundo arquivo guarda o catalogo de filmes (titulo, diretor e sinopse).
open("Arquivo_de_usuario.txt", "a").close()
open("Arquivo_de_filmes.txt", "a", encoding="utf-8").close()


# Gera o nome do arquivo de curtidos do usuario a partir do email.
# Troca "." por "_" para o nome ser valido no sistema operacional.
# Exemplo: "joao.silva@email.com" vira "curtidos_joao_silva@email_com.txt"
def arq_curtidos(email):
    nome = ""
    for c in email:                            # Percorre cada caractere do email
        nome = nome + ("_" if c == "." else c) # Substitui "." por "_", mantem os demais
    return "curtidos_" + nome + ".txt"         # Retorna o nome completo do arquivo


# Mesma logica de arq_curtidos, mas para a lista "Assistir mais tarde".
def arq_assistir(email):
    nome = ""
    for c in email:
        nome = nome + ("_" if c == "." else c)
    return "assistir_" + nome + ".txt"


# Garante que um arquivo exista sem apagar seu conteudo.
# O modo "a" cria o arquivo se nao existir; se ja existir, nao faz nada.
# O .close() fecha o arquivo imediatamente apos abri-lo.
def criar_arq(caminho):
    open(caminho, "a", encoding="utf-8").close()


# Verifica se o par email/senha confere com algum registro salvo no arquivo de usuarios.
# Retorna True se encontrar uma combinacao valida, False caso contrario.
def verificar_login(email, senha):
    arquivo = open("Arquivo_de_usuario.txt", "r")  # Abre o arquivo so para leitura
    sucesso = False                                 # Assume falha ate provar o contrario
    for linha in arquivo:
        dados = linha.strip().split("\t")           # Remove espacos/quebras e separa pelo TAB
        # Verifica se a linha tem exatamente 2 campos e se ambos batem com o que foi digitado
        if len(dados) == 2 and dados[0] == email and dados[1] == senha:
            sucesso = True
    arquivo.close()
    return sucesso


# Le o catalogo de filmes e devolve uma lista de listas no formato [[titulo, diretor, sinopse], ...].
# Cada linha do arquivo corresponde a um filme, com campos separados por TAB.
def listar_filmes():
    arquivo = open("Arquivo_de_filmes.txt", "r", encoding="utf-8")
    filmes = []
    for linha in arquivo:
        dados = linha.strip().split("\t")  # Separa os campos da linha pelo TAB
        if len(dados) >= 3:               # So inclui linhas com os 3 campos minimos
            filmes.append(dados)
    arquivo.close()
    return filmes


# Exibe as informacoes de um filme formatadas no terminal.
# Se indice != -1, mostra o numero do filme na frente do titulo (util para listas numeradas).
# Se indice == -1, exibe sem numeracao (util para exibicao simples do catalogo).
def exibir_filme(dados, indice):
    if indice != -1:
        print("[" + str(indice) + "] Titulo: " + dados[0])  # Exibe numero + titulo
    else:
        print("Titulo: " + dados[0])                        # Exibe so o titulo
    print("    Diretor: " + dados[1])
    print("    Sinopse: " + dados[2])
    print("----------------------------------------")        # Separador visual entre filmes


# Exibe o catalogo numerado e pede que o usuario escolha um numero.
# Devolve os dados do filme escolhido (lista com titulo, diretor, sinopse)
# ou None se o usuario cancelar ou digitar algo invalido.
def escolher_filme():
    filmes = listar_filmes()
    if len(filmes) == 0:                  # Catalogo vazio: avisa e encerra a funcao
        print("Nenhum filme disponivel no catalogo.")
        return None
    contador = 0
    for dados in filmes:
        contador = contador + 1           # Incrementa manualmente (sem enumerate)
        exibir_filme(dados, contador)     # Exibe o filme com seu numero
    escolha_texto = input("Digite o numero do filme (0 para cancelar): ")
    # Valida se a entrada e numerica verificando cada caractere individualmente
    # (nao usa isdigit() ou isnumeric() para manter o estilo do restante do codigo)
    valido = True
    for c in escolha_texto:
        if c < "0" or c > "9":           # Qualquer caractere fora do intervalo '0'-'9' invalida
            valido = False
    if not valido or escolha_texto == "": # Entrada vazia tambem e invalida
        print("Entrada invalida.")
        return None
    escolha = int(escolha_texto)          # Converte para inteiro apos validar
    if escolha == 0:                      # 0 significa cancelar
        return None
    if escolha >= 1 and escolha <= len(filmes):  # Verifica se esta dentro do intervalo valido
        return filmes[escolha - 1]               # Retorna o filme (ajuste de indice: lista comeca em 0)
    print("Numero invalido.")
    return None


# Le um arquivo de lista pessoal (curtidos ou assistir depois) e devolve
# os filmes salvos como lista de listas, no mesmo formato de listar_filmes().
def ler_lista(caminho):
    arquivo = open(caminho, "r", encoding="utf-8")
    filmes = []
    for linha in arquivo:
        dados = linha.strip().split("\t")
        if len(dados) >= 3:
            filmes.append(dados)
    arquivo.close()
    return filmes


# Verifica se um titulo ja existe em um arquivo de lista, usando busca sem diferenciar maiusculas.
# Retorna True se o titulo ja estiver salvo, False caso contrario.
# A comparacao em lowercase evita duplicatas como "Matrix" e "matrix".
def ja_esta_na_lista(caminho, titulo):
    arquivo = open(caminho, "r", encoding="utf-8")
    conteudo = arquivo.read()             # Le o arquivo inteiro de uma vez como string
    arquivo.close()
    return titulo.lower() in conteudo.lower()  # Busca case-insensitive


# Adiciona um filme escolhido pelo usuario a uma lista (curtidos ou assistir depois).
# mensagem_titulo e o cabecalho exibido no terminal para identificar a acao.
def adicionar_a_lista(caminho, mensagem_titulo):
    print("\n--- " + mensagem_titulo + " ---")
    filme = escolher_filme()             # Pede ao usuario que escolha um filme do catalogo
    if filme is None:                    # Usuario cancelou ou entrada invalida
        return
    if ja_esta_na_lista(caminho, filme[0]):    # Evita duplicatas na lista
        print("'" + filme[0] + "' ja esta na lista!")
        return
    arquivo = open(caminho, "a", encoding="utf-8")   # Abre em modo append para nao apagar
    arquivo.write(filme[0] + "\t" + filme[1] + "\t" + filme[2] + "\n")  # Salva separado por TAB
    arquivo.close()
    print("'" + filme[0] + "' adicionado!")


# Exibe todos os filmes de uma lista pessoal.
# Se a lista estiver vazia, informa o usuario.
def ver_lista(caminho, titulo_menu):
    print("\n--- " + titulo_menu + " ---")
    filmes = ler_lista(caminho)
    if len(filmes) == 0:
        print("Lista vazia.")
        return
    for dados in filmes:
        exibir_filme(dados, -1)          # Exibe sem numeracao


# Remove um filme de uma lista pessoal.
# A remocao e feita reescrevendo o arquivo inteiro, pulando apenas o item escolhido.
# Essa abordagem e necessaria porque arquivos de texto nao suportam remocao de linhas no meio.
def remover_da_lista(caminho, titulo_menu):
    print("\n--- " + titulo_menu + " ---")
    filmes = ler_lista(caminho)
    if len(filmes) == 0:
        print("Lista vazia.")
        return
    contador = 0
    for dados in filmes:
        contador = contador + 1
        exibir_filme(dados, contador)    # Mostra a lista numerada para o usuario escolher
    escolha_texto = input("Numero para remover (0 para cancelar): ")
    # Mesma validacao de entrada numerica usada em escolher_filme()
    valido = True
    for c in escolha_texto:
        if c < "0" or c > "9":
            valido = False
    if not valido or escolha_texto == "":
        print("Entrada invalida.")
        return
    escolha = int(escolha_texto)
    if escolha == 0:
        return
    if escolha >= 1 and escolha <= len(filmes):
        titulo_removido = filmes[escolha - 1][0]    # Guarda o titulo para exibir na confirmacao
        # Abre o arquivo em modo "w" (sobrescreve tudo) e reescreve todos os filmes, exceto o removido
        arquivo = open(caminho, "w", encoding="utf-8")
        posicao = 0
        for dados in filmes:
            posicao = posicao + 1
            if posicao != escolha:       # Pula o filme que deve ser removido
                arquivo.write(dados[0] + "\t" + dados[1] + "\t" + dados[2] + "\n")
        arquivo.close()
        print("'" + titulo_removido + "' removido.")
    else:
        print("Numero invalido.")


# Submenu de curtidos: permite ver, curtir ou remover filmes curtidos do usuario.
# O loop continua ate o usuario escolher voltar (opcao "0").
def menu_curtidos(email):
    caminho = arq_curtidos(email)        # Obtem o caminho do arquivo pessoal de curtidos
    while True:
        print("\n--- CURTIDOS ---")
        print("1 - Ver curtidos | 2 - Curtir filme | 3 - Remover | 0 - Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            ver_lista(caminho, "SEUS CURTIDOS")
        elif opcao == "2":
            adicionar_a_lista(caminho, "CURTIR FILME")
        elif opcao == "3":
            remover_da_lista(caminho, "REMOVER CURTIDO")
        elif opcao == "0":
            break                        # Encerra o loop e volta ao menu principal
        else:
            print("Opcao invalida.")


# Submenu de assistir mais tarde: permite ver, adicionar ou remover filmes da lista.
# Estrutura identica ao menu_curtidos, mas usando o arquivo de "assistir depois".
def menu_assistir(email):
    caminho = arq_assistir(email)        # Obtem o caminho do arquivo pessoal de assistir depois
    while True:
        print("\n--- ASSISTIR MAIS TARDE ---")
        print("1 - Ver lista | 2 - Adicionar filme | 3 - Remover | 0 - Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            ver_lista(caminho, "ASSISTIR MAIS TARDE")
        elif opcao == "2":
            adicionar_a_lista(caminho, "ADICIONAR A LISTA")
        elif opcao == "3":
            remover_da_lista(caminho, "REMOVER DA LISTA")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


# Pesquisa filmes no catalogo por qualquer campo: titulo, diretor ou sinopse.
# A busca e case-insensitive (converte tudo para lowercase antes de comparar).
def pesquisar_filmes():
    termo = input("Digite o titulo, diretor ou sinopse: ").strip().lower()  # Normaliza a entrada
    arquivo = open("Arquivo_de_filmes.txt", "r", encoding="utf-8")
    encontrado = False                   # Controla se ao menos um resultado foi exibido
    print("\nResultados para '" + termo + "':")
    for linha in arquivo:
        dados = linha.strip().split("\t")
        if len(dados) >= 3:
            # Verifica se o termo aparece em qualquer um dos tres campos
            if termo in dados[0].lower() or termo in dados[1].lower() or termo in dados[2].lower():
                exibir_filme(dados, -1)
                encontrado = True
    arquivo.close()
    if not encontrado:
        print("Nenhum filme encontrado.")


# ---- Loop principal do programa ----
# Fica rodando indefinidamente ate o usuario encerrar o processo.
# Na tela inicial so ha duas opcoes publicas: cadastro e login.

while True:
    print("\nDURAMTUNA  |  cadastro  |  login")
    opcao = input("Digite a opcao desejada: ")

    if opcao == "cadastro":
        email = input("Digite o seu email: ")
        senha = input("Crie uma senha: ")
        arquivo = open("Arquivo_de_usuario.txt", "a")          # Abre em append para nao sobrescrever
        arquivo.write(email + "\t" + senha + "\n")             # Salva email e senha separados por TAB
        arquivo.close()
        # Cria os arquivos pessoais do usuario ja no momento do cadastro,
        # garantindo que existam quando ele fizer login pela primeira vez
        criar_arq(arq_curtidos(email))
        criar_arq(arq_assistir(email))
        print("Usuario cadastrado com sucesso!")

    elif opcao == "login":
        email_login = input("Digite o email: ")
        senha_login = input("Digite a senha: ")

        if verificar_login(email_login, senha_login):
            # Garante os arquivos pessoais caso o usuario seja antigo e nao os tenha ainda
            criar_arq(arq_curtidos(email_login))
            criar_arq(arq_assistir(email_login))
            print("\nBem-vindo, " + email_login + "!")

            # Loop do menu interno, acessivel somente apos login bem-sucedido
            while True:
                print("\n=== MENU ===")
                print("1 - Catalogo | 2 - Pesquisar | 3 - Curtidos | 4 - Assistir mais tarde | 0 - Sair")
                opcao_menu = input("Escolha: ")

                if opcao_menu == "1":
                    print("\n--- CATALOGO ---")
                    filmes = listar_filmes()
                    if len(filmes) > 0:
                        for dados in filmes:
                            exibir_filme(dados, -1)   # Exibe todos os filmes sem numeracao
                    else:
                        print("Catalogo vazio.")
                elif opcao_menu == "2":
                    pesquisar_filmes()
                elif opcao_menu == "3":
                    menu_curtidos(email_login)         # Passa o email para identificar os arquivos do usuario
                elif opcao_menu == "4":
                    menu_assistir(email_login)
                elif opcao_menu == "0":
                    print("Ate mais!")
                    break                              # Sai do menu interno e volta a tela de cadastro/login
                else:
                    print("Opcao invalida.")
        else:
            print("Email ou senha incorretos.")