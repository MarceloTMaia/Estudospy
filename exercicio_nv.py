# Crie um programa que permita aos usuários:
# Adicionar novos livros à biblioteca, com informações como título,
# autor e número de cópias disponíveis.
# Listar todos os livros disponíveis na biblioteca.
# # Permitir aos usuários fazer empréstimos de livros, reduzindo o
# # número de cópias disponíveis quando um livro é emprestado.
# # Permitir aos usuários devolver livros, aumentando o número de
# # cópias disponíveis quando um livro é devolvido.
# # Verificar a disponibilidade de um livro específico na biblioteca.
# # Mostrar a lista de livros emprestados a um usuário específico.

# -------------------------cadastro usuarios
# ---adicionar usuario
# nome 
# cpf
# emprestimos f/t

# ---listar usuarios
# ---pesquisar usuario
# nome
# matricula

# -------------------------cadastro livros

# ---adicionar livro
# titulo
# Autor 
# numero de copias



# ---procurar livros
# 1 - nome
# 2 - autor
# 3 -todos
# 4 -livros disponiveis 
# 5 -livros indiponiveis

lista_usuarios = [
    {'nome': 'João', 'idade': '25', 'cpf': '12345678900'},
    {'nome': 'Maria', 'idade': '30', 'cpf': '98765432100'}
]

lista_livros = [
    {'titulo': 'gow', 'autor': 'Antoine de Saint-Exupéry', 'quantidade': 3, 'disponibilidade': 'Disponivel'},
    {'titulo': '1984', 'autor': 'George Orwell', 'quantidade': 1, 'disponibilidade': 'Disponivel'}
]

lista_aluguel = []


print ('----------BIBLIOTECA----------')

while True: #------------------------------------------------------------------------------MENU--------------------------------------------------------------------------------
    print (f'''
----------MENU---------
[1] - Cadastrar - | Livros | Usuario |.
[2] - Buscar | Alugel | Devolução.
[3] - Sair da Biblioteca. ''')

    opção_menu = input('\nDigite uma opção acima: ').strip()
    if opção_menu not in ['1','2','3']:
        print ('Digite uma das opções acima.')

    match opção_menu:
        #---------------------------------------------------------------------------------------------------------------------------------------------------------01 CASE 3
        case '3': #SAIR DA BIBLIOTECA
            print ('---SAINDO---.')
            break

        #---------------------------------------------------------------------------------------------------------------------------------------------------------01 CASE 1
        case '1': #CADASTRAR | LIVRO | USUARIO

            while True:
                print (f'''
    ----------CADASTRAR---------
    [1] - LIVROS - Adicionar | Remover.
    [2] - USUARIOS - Adicionar | Remover.
    [3] - Sair. ''')

                opção_cadastro = input('\nDigite uma opção: ').strip()
                if opção_cadastro not in ['1','2','3']:
                    print ('Digite uma das opções acima.')
                
                match opção_cadastro:
                    #------------------------------------------------------------------------------------02 CASE 3
                    case "3": #SAIR
                        print ('---SAINDO---.')
                        break

                    #------------------------------------------------------------------------------------02 CASE 1
                    case "1": #ADICIONAR | REMOVER LIVROS
                                
                        while True:
                            print(f'''
        ----ADICIONAR LIVROS----                                  
        [1] - Cadastrar.
        [2] - Remover.
        [3] - Sair.    ''')
                            
                            opção_cadastro_livros = input('Digite uma opção: ').strip()
                            if opção_cadastro_livros not in ['1','2','3']:
                                print ('Digite uma das opções acima.')


                            match opção_cadastro_livros:
                                #--------------------------------------03 CASE 3
                                case '3': #SAIR

                                    print ('---SAINDO---.')
                                    break

                                #--------------------------------------03 CASE 1                             
                                case '1': #CADASTRAR LIVRO
                                    print ('\n----CADASTRAR LIVRO ou DIGITE "sair"---- ')
                                    
                                    titulo_livro = input('Titulo: ').strip() #DEFINE UM TITULO
                                    if titulo_livro.lower() == 'sair':
                                        print ('--Não cadastrado--')
                                        continue 

                                    autor_livro = input('Autor: ').strip() #DEFINE UM AUTOR
                                    if autor_livro.lower() == 'sair':
                                        print ('--Não cadastrado--')
                                        continue

                                    

                                    quantidade_livro = input('Quantidade: ').strip() #DEFINE UMA QUANTIDADE

                                    if quantidade_livro.isdigit():
                                        quantidade_livro = int(quantidade_livro)

                                        if quantidade_livro > 0:
                                            disponibilidade_livro = 'disponivel'
                                        else:
                                            disponibilidade_livro = 'indisponivel'

                                        livro_cadastrado = {#-------------------------------------------------------------------DICIONARIO DE LIVROS
'titulo': titulo_livro,
'autor': autor_livro,
'quantidade': quantidade_livro,
'disponibilidade': disponibilidade_livro
                                        }

                                        lista_livros.append(livro_cadastrado)
                                        print ('Livro cadastrado com sucesso')
                                    
                                    
                                    
                                    else:
                                        print ('digite um numero valido') 


                                #--------------------------------------03 CASE 2
                                case '2': #REMOVER LIVRO
                                    print ('\n----REMOVER LIVRO----')
                                    
                                    if not lista_livros:
                                        print ('Lista de livros ainda vazia.')

                                    else:

                                        print ('Lista de Livros')
                                        for item in lista_livros:
                                            print (f'''
Titulo - {item["titulo"]}''')

                                    while True:

                                        livro_apagar = input('Escolha um titulo da lista para apagar ou digite "sair": ').strip()

                                        if livro_apagar.lower() == 'sair':
                                            print ('Voltando')
                                            break

                                        livro_procurado = False
                                        for item in lista_livros:                                    
                                                                                
                                            if item['titulo'] == livro_apagar:
                                                lista_livros.remove(item)
                                                print (f'Livro - {item["titulo"]} removido da biblioteca.')
                                                livro_procurado = True
                                                break

                                        if not livro_procurado:
                                            print('Digite um titulo valido. ')    

                                #--------------------------------------03 FIM
                                
                    #------------------------------------------------------------------------------------02 CASE 2
                    case '2': #ADICIONAR | REMOVER USUARIO 
                        while True:    
                            print(f'''
        ----ADICIONAR USUARIO----                                  
        [1] - Cadastrar.
        [2] - Remover.
        [3] - Sair.    ''')
                            opção_cadastro_usuario = input('Digite uma opção: ').strip()
                            if opção_cadastro_usuario not in ['1','2','3']:
                                print ('Digite uma das opções acima.')
                            
                            match opção_cadastro_usuario:
                                #--------------------------------------03 CASE 3
                                case '3': #SAIR
                                    print ('---SAINDO---.')
                                    break

                                #--------------------------------------03 CASE 1
                                case '1': #CADASTRAR USUARIO
                                    print ('----CADASTRAR USUARIO ou DIGITE "sair"----')
                                    nome_usuario = input('Digite o nome: ').strip()
                                    if nome_usuario.lower() == "sair":
                                        print ('Não cadastrado')
                                        continue

                                    idade_usuario = input('Digite a idade: ').strip()
                                    if idade_usuario == "sair":
                                        print ('Não cadastrado')
                                        continue


                                    while True:

                                        cpf_usuario = input('Digite o cpf: ').strip()
                                        
                                        try:
                                            cpf_usuario = int(cpf_usuario)
                                        
                                        except:
                                            print("CPF inválido!, insira um número válido.")

                                        else:    

                                            usuario_cadastrado = {#-------------------------------------------------------------------DICIONARIO DE USUARIOS
'nome': nome_usuario,
'Idade': idade_usuario,
'cpf': cpf_usuario
                                            }

                                            lista_usuarios.append(usuario_cadastrado)

                                            print (f'---> Usuario: "{nome_usuario}" adicionado com sucesso.')
                                            break

                                #--------------------------------------03 CASE 2   
                                case '2': #REMOVER USUARIO
                                    print ('\n----REMOVER USUARIO----')

                                    if not lista_usuarios:
                                        print('Lista de usuarios ainda vazia.')

                                    else:
                                        print ('Lista de Usuarios')
                                        for item in lista_usuarios:
                                            print (f'Nome: {item["nome"]}')
                                            
                                    while True:
                                        usuario_apagar = input('Digite o nome do usuario para remover ou digite "sair" para volta: ').strip()       
                                        if usuario_apagar.lower() == 'sair':
                                            print('Voltando')
                                            break

                                        usuario_procurar = False

                                        for item in lista_usuarios:
                                            if item ["nome"] == usuario_apagar:
                                                lista_usuarios.remove(item)
                                                print (f'Usuario {item["nome"]} removido da biblioteca') 
                                                usuario_procurar = True
                                                break
                                            
                                        if not usuario_procurar:
                                            print ('Digite um usuario valido')

                                #--------------------------------------03 FIM
                    #------------------------------------------------------------------------------------02 FIM
                        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------01 CASE 2
        case '2': #BUSCAR | ALUGUEL | DEVOLUÇÃO
                
            while True:    
                print (f'''
    ----------BUSCAR | ALUGUEL | DEVOLUÇÃO---------
    [1] - Alugar/Devolver livros.
    [2] - Buscar Livros.
    [3] - Buscar Usuario.
    [4] - Sair.''')
                opção_buscar_alugar_devolver = input('\nDigite uma opção acima: ').strip()
                if opção_buscar_alugar_devolver not in ['1','2','3','4']:
                    print ('Opção invalida, digite uma das opções acima.')

                match opção_buscar_alugar_devolver:

                    #------------------------------------------------------------------------------------02 CASE 4
                    case '4': #SAIR
                        print ('Voltando para o menu.')
                        break

                    #------------------------------------------------------------------------------------02 CASE 1
                    case '1': #ALUGAR | DEVOLVER LIVROS NAO TA FINALIZADO O DEVOLVER
                        
                        if not lista_livros or not lista_usuarios:
                            print ('\nA lista de livros ou a lista de usuários ainda está vazia.')
                            break
                                               
                        while True:
                            print('''
        ----ALUGAR | DEVOLVER----
        [1] - Alugar.
        [2] - Devolver.
        [3] - Listar livros Aluguados.                          
        [4] - Sair.
''')
                            alugar_devolver = input('Digite uma opção acima: ')
                            if alugar_devolver not in ['1','2','3','4']:
                                print ('\nDigite uma das opções acima: ')

                            match alugar_devolver:
                                
                                #--------------------------------------03 CASE 4
                                case '4': #SAIR
                                    print ('Saindo')
                                    break

                                #--------------------------------------03 CASE 1
                                case '1': #ALUGAR 
                                    
                                    print ('\n----ALUGAR----')

                                    print ('\nLista de Livros.')
                                    for item in lista_livros:
                                        
                                        print(f'Titulo: {item["titulo"]} | Quantidade: {item["quantidade"]} | Disponibilidade: {item["disponibilidade"]}')


                                    procurar_livro_alugar = input ('\nDigite o titulo do livro ou Autor ou digite "sair" para sair: ').strip() # INSERIR DADOS LIVRO PARA ALUGAR

                                    if procurar_livro_alugar.lower() == 'sair':
                                        print ('Saindo')
                                        continue

                                    encontrou_livro_alugar = False

                                    for livro_da_vez in lista_livros:
                                        
                                        if livro_da_vez['titulo'] == procurar_livro_alugar or livro_da_vez['autor'] == procurar_livro_alugar:
                                            encontrou_livro_alugar = True
                                            print (f'Nome: {livro_da_vez["titulo"]} | Quantidade: {livro_da_vez["quantidade"]} | {livro_da_vez["disponibilidade"]}')
                                            
                                                                                        
                                            
                                            dados_usuario_alugar = input('\nDigite o nome ou cpf ou digite "sair" para sair: ').strip() # INSERIR DADOS USUARIO PARA ALUGAR

                                            if dados_usuario_alugar.lower() == 'sair':
                                                print ('Saindo')
                                                break
                                                        
                                            encontrou_usuario_alugar = False

                                            for usuario_da_vez in lista_usuarios:
                                                
                                                if usuario_da_vez['nome'] == dados_usuario_alugar or usuario_da_vez['cpf'] == dados_usuario_alugar:       
                                                    encontrou_usuario_alugar = True
                                                    print (f'Nome: {usuario_da_vez["nome"]} - CPF: {usuario_da_vez["cpf"]} - deseja alugar o livro "{livro_da_vez["titulo"]}"?')
                                                    
                                                    alugar_S_N = input ('\nDigite "S" para alugar ou "N" para sair: ')
                                                    
                                                    if alugar_S_N.lower() == 'n':
                                                        print ('Saindo')
                                                        break
                                                    
                                                    elif alugar_S_N.lower() == 's':
                                                        print (f'''
LIVRO ALUGADO--------------------------------------                                                       
Livro: {livro_da_vez["titulo"]}
Usuario: {usuario_da_vez["nome"]}
CPF: {usuario_da_vez["cpf"]}''')
                                                        livro_da_vez['quantidade'] -=1
                                                        if livro_da_vez['quantidade'] > 0:
                                                            livro_da_vez['disponibilidade'] = 'disponivel'
                                                        else:
                                                            livro_da_vez['disponibilidade'] = 'indisponivel'

                                                        



                                                    aluguel = {#-------------------------------------------------------------------DICIONARIO DE LOCAÇÃO
'nome_usuario_aluga': usuario_da_vez["nome"],
'cpf_usuario_aluga': usuario_da_vez["cpf"],
'titulo_livro_aluga':livro_da_vez["titulo"]

                                                    }
                                                    lista_aluguel.append(aluguel)
                                        

                                            if not encontrou_usuario_alugar:
                                                print (f'Usuario não encontrado')
                                                break
                                    
                                         
                                                                        

                                    if not encontrou_livro_alugar:
                                        print (f'Livro não encontrado')
                                        continue
                                
                                #--------------------------------------03 CASE 2                                 
                                case '2': #DEVOLVER
                                    print ('----DEVOLVER----')

                                    if not lista_aluguel:
                                        print('Não possue livros alugados.')
                                        break

                                    print ('Lista de Livros Alugados')
                                    for item in lista_aluguel:
                                        print (f'''
Titulo do livro: {item["titulo_livro_aluga"]}
Dados do usuario:
Nome: {item["nome_usuario_aluga"]}
CPF: {item["cpf_usuario_aluga"]}''')
                                        
                                    
                                    buscar_livro_alugado = input ('\nDigite o Nome do Usuario ou o CPF: ').strip() #ENTRADA PARA BUSCAR ITEM ALUGADO 12345678900
                                    achou_locador = False

                                    for livro_alugado_da_vez in lista_aluguel:             
                                        if livro_alugado_da_vez['nome_usuario_aluga'] == buscar_livro_alugado or livro_alugado_da_vez ['cpf_usuario_aluga'] == buscar_livro_alugado:
                                            achou_locador = True
                                            
                                            print (f'''
Titulo do livro: {livro_alugado_da_vez["titulo_livro_aluga"]}
Dados do usuario:
Nome: {livro_alugado_da_vez["nome_usuario_aluga"]}
CPF: {livro_alugado_da_vez["cpf_usuario_aluga"]}''')
                                                                                
                                            
                                            confirmar_devolução = input('Deseja confirmar a devolução do livro? s/n: ').strip().lower()
                                            if confirmar_devolução not in ['s','n']:
                                                print ('Escolha uma das opções.')
                                                continue

                                            elif confirmar_devolução.lower() == 'n':
                                                print ('--Livro nao devolvido--')
                                                break

                                            else:
                                                lista_aluguel.remove(livro_alugado_da_vez)# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQQQQQQQQQQQQQQQQQQQQUIIIIIIIIIIIIIIIIIIII

                                                for livro in lista_livros:
                                                    if livro['titulo'].lower() == livro_alugado_da_vez['titulo_livro_aluga'].lower():  
                                                        livro['quantidade'] += 1  

                                                    
                                                    if livro['quantidade'] > 0:
                                                        livro['disponibilidade'] = 'disponível'
                                                    else:
                                                        livro['disponibilidade'] = 'indisponível'
                                            
                                            

                                        
                                    if not achou_locador:
                                        print ('Usuario não encontrado na lista de locação.')
                                        continue


                                #--------------------------------------03 CASE 3                                 
                                case '3': #LISTAR LIVROS ALUGADOS NAO TE FINALIZADO
                                    print ('----LISTA DE LIVROS ALUGADOS----')
                                    
                                    contador_livros_alugador = 0


                                    for livro in lista_aluguel:
                                        contador_livros_alugador+=1
                                        print (f'''
Livro {contador_livros_alugador}                                               
Titulo: {livro['titulo_livro_aluga']}
Nome do Locadir: {livro['nome_usuario_aluga']}
CPF: {livro['cpf_usuario_aluga']}''')
                                

                    #------------------------------------------------------------------------------------02 CASE 2
                    case '2': #BUSCAR LIVROS
                        while True:
                            print ('----BUSCAR LIVROS----')
                            print (f'''
        [1] - Buscar por Nome.
        [2] - Buscar por Autor.
        [3] - Listar todos.
        [4] - Sair.
''')
                            opção_buscar = input('Digite uma opção pra busca: ').strip()
                            if opção_buscar not in ['1','2','3','4']:
                                print ('Opção invalida, digite uma das opções acima.')

                            match opção_buscar:

                                #--------------------------------------03 CASE 4
                                case '4': #SAIR
                                    print ('Voltando para o menu.')
                                    break
                       
                                #--------------------------------------03 CASE 1
                                case '1': #BUSCAR POR NOME
                                    print ('\n----BUSCAR POR NOME----.')
                                    if not lista_livros:
                                        print ('Lista de livros vazia.')
                                        break
                                    
                                    else:                                        
                                        buscar_por_titulo = input('Digite o nome do titulo: ')
                                        achou_titulo = False

                                        for item in lista_livros:                                            
                                            
                                            if item['titulo'].lower() == buscar_por_titulo.lower():
                                                
                                                print (f'''
LIVRO 
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}''')
                                                achou_titulo = True
                                                break

                                        if not achou_titulo:
                                            print (f'Titulo: "{buscar_por_titulo}" não encontrado.')

                                #--------------------------------------03 CASE 2
                                case '2': #BUSCAR POR AUTOR
                                    print ('\n----BUSCAR POR AUTOR----.')
                                    if not lista_livros:
                                        print ('Lista de livros vazia.')
                                        break

                                    else:
                                        achou_autor = False
                                        buscar_por_autor = input('Digite o nome do Autor: ')

                                        for item in lista_livros:
                                            if item['autor'].lower() == buscar_por_autor.lower():
                                                print (f'''
LIVRO 
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}
''')
                                                achou_autor = True

                                        if not achou_autor:
                                            print (f'Autor: "{buscar_por_autor}" não encontrado.')

                                #--------------------------------------03 CASE3
                                case '3': #LISTAR TODOS
                                    print ('----LISTAR TODOS----.')

                                    if not lista_livros:
                                        print ('Lista de livros vazia.')
                                        break

                                    contador_geral = 0

                                    for item in lista_livros:
                                        contador_geral+=1                                                        
                                        print (f'''
LIVRO {contador_geral}-----------------------------------------------------------------------
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}
''')                                
                                        
                                #--------------------------------------03 FIM

                    #------------------------------------------------------------------------------------02 CASE 3
                    case '3': #BUSCAR USUARIO
                        print ('----BUSCAR USUARIO----')
                        if not lista_usuarios:
                            print( 'Lista Vazia')
                        
                        
                        buscar_usuario = input('Digite o nome ou o cpf do usuario: ')
                        achou_usuario = False
                        for item in lista_usuarios:
                            if item['nome'] == buscar_usuario or item['cpf'] == buscar_usuario:
                                print (f'''
Nome: {item['nome']}
Cpf: {item['cpf']}
''')
                                achou_usuario = True
                                break

                        if not achou_usuario:
                            print('Usuario não esta na lista')
                     
                    #------------------------------------------------------------------------------------02  FIM
        #---------------------------------------------------------------------------------------------------------------------------------------------------------01 FIM                    

                        
