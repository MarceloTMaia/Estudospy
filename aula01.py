# Inicialização das listas
lista_livros = []
lista_usuarios = [
    {'nome': 'João', 'idade': '25', 'cpf': '12345678900'},
    {'nome': 'Maria', 'idade': '30', 'cpf': '98765432100'}
]
lista_aluguel = []

while True:
    print('''
----------MENU PRINCIPAL---------
[1] - Cadastrar Livros.
[2] - Buscar | Aluguel | Devolução.
[3] - Sair.''')
    opção_menu = input('Digite uma opção acima: ').strip()
    if opção_menu not in ['1', '2', '3']:
        print('Opção inválida, digite uma das opções acima.')
        continue

    match opção_menu:
        case '3': # SAIR
            print('Saindo do programa.')
            break

        case '1': # CADASTRAR LIVROS
            while True:
                print('----CADASTRAR LIVROS----')
                titulo = input('Digite o título do livro (ou digite "sair" para sair): ').strip()
                if titulo.lower() == 'sair':
                    print('Saindo do cadastro de livros.')
                    break
                autor = input('Digite o nome do autor: ').strip()
                quantidade = input('Digite a quantidade: ').strip()

                # Adiciona livro à lista
                lista_livros.append({
                    'titulo': titulo,
                    'autor': autor,
                    'quantidade': int(quantidade),
                    'disponibilidade': 'Disponível' if int(quantidade) > 0 else 'Indisponível'
                })
                print(f'Livro "{titulo}" cadastrado com sucesso.')

        case '2': # BUSCAR | ALUGUEL | DEVOLUÇÃO
            while True:    
                print(f'''
----------BUSCAR | ALUGUEL | DEVOLUÇÃO---------
[1] - Alugar/Devolver livros.
[2] - Buscar Livros.
[3] - Buscar Usuario.
[4] - Sair.''')
                opção_buscar_alugar_devolver = input('\nDigite uma opção acima: ').strip()
                if opção_buscar_alugar_devolver not in ['1', '2', '3', '4']:
                    print('Opção inválida, digite uma das opções acima.')
                    continue

                match opção_buscar_alugar_devolver:
                    case '4': # SAIR
                        print('Voltando para o menu.')
                        break

                    case '1': # ALUGAR | DEVOLVER LIVROS
                        if not lista_livros or not lista_usuarios:
                            print('\nA lista de livros ou a lista de usuários ainda está vazia.')
                            break
                                               
                        while True:
                            print('''----ALUGAR | DEVOLVER----
[1] - Alugar.
[2] - Devolver.
[3] - Listar livros Alugados.                          
[4] - Sair.''')
                            alugar_devolver = input('Digite uma opção acima: ')
                            if alugar_devolver not in ['1', '2', '3', '4']:
                                print('\nDigite uma das opções acima:')
                                continue

                            match alugar_devolver:
                                case '4': # SAIR
                                    print('Saindo')
                                    break

                                case '1': # ALUGAR 
                                    print('\n----ALUGAR----')
                                    print('\nLista de Livros.')
                                    for item in lista_livros:
                                        print(f'Titulo: {item["titulo"]} | Quantidade: {item["quantidade"]} | Disponibilidade: {item["disponibilidade"]}')

                                    alugar_digite_dados_livro = input('Digite o titulo do livro ou Autor ou digite "sair" para sair: ').strip()
                                    if alugar_digite_dados_livro.lower() == 'sair':
                                        print('Saindo')
                                        continue

                                    encontrou_livro_alugar = False
                                    for item_livro in lista_livros:
                                        if alugar_digite_dados_livro.lower() in (item_livro['titulo'].lower(), item_livro['autor'].lower()):
                                            encontrou_livro_alugar = True
                                            print(f'Nome: {item_livro["titulo"]} | Quantidade: {item_livro["quantidade"]} | {item_livro["disponibilidade"]}')

                                            if item_livro['disponibilidade'] == 'Disponível':
                                                alugar_digite_dados_usuario = input('\nDigite o nome ou cpf ou digite "sair" para sair: ').strip()
                                                if alugar_digite_dados_usuario.lower() == 'sair':
                                                    print('Saindo')
                                                    break

                                                encontrou_usuario_alugar = False
                                                for item_usuario in lista_usuarios:
                                                    if alugar_digite_dados_usuario.lower() in (item_usuario['nome'].lower(), item_usuario['cpf']):
                                                        encontrou_usuario_alugar = True
                                                        print(f'Nome: {item_usuario["nome"]} - CPF: {item_usuario["cpf"]} encontrado')

                                                        opçao_alugar = input('Digite "S" para alugar ou "N" para sair: ')
                                                        if opçao_alugar.lower() == 'n':
                                                            print('Saindo')
                                                            break
                                                        elif opçao_alugar.lower() == 's':
                                                            print(f'''
                                LIVRO ALUGADO--------------------------------------                                                       
                                Livro: {item_livro["titulo"]}
                                Usuario: {item_usuario["nome"]}
                                CPF: {item_usuario["cpf"]}''')
                                                            item_livro['quantidade'] -= 1

                                                            # Atualizando a disponibilidade
                                                            if item_livro['quantidade'] == 0:
                                                                item_livro['disponibilidade'] = 'Indisponível'
                                                            else:
                                                                item_livro['disponibilidade'] = 'Disponível'

                                                            lista_aluguel.append({
                                                                'nome_usuario_aluga': item_usuario["nome"],
                                                                'cpf_usuario_aluga': item_usuario["cpf"],
                                                                'titulo_livro_aluga': item_livro["titulo"]
                                                            })
                                                            break

                                                if not encontrou_usuario_alugar:
                                                    print('Usuário não encontrado')
                                                    break
                                            else:
                                                print('Livro indisponível para alugar')
                                                break

                                    if not encontrou_livro_alugar:
                                        print('Livro não encontrado')
                                        continue
                            
                                case '2': # DEVOLVER
                                    print('----DEVOLVER----')
                                    if not lista_aluguel:
                                        print('Não possui livros alugados.')
                                        break

                                    print('Lista de Livros Alugados:')
                                    for item in lista_aluguel:
                                        print(f'''
Titulo do livro: {item["titulo_livro_aluga"]}
Dados do usuario:
Nome: {item["nome_usuario_aluga"]}
CPF: {item["cpf_usuario_aluga"]}''')
                                        
                                    buscar_livro_alugado = input('\nDigite o Nome do Usuario ou o CPF: ').strip()
                                    achou_locador = False
                                    for item in lista_aluguel:
                                        if item['nome_usuario_aluga'].lower() == buscar_livro_alugado.lower() or item['cpf_usuario_aluga'] == buscar_livro_alugado:
                                            achou_locador = True
                                            print(f'''
Titulo do livro: {item["titulo_livro_aluga"]}
Dados do usuario:
Nome: {item["nome_usuario_aluga"]}
CPF: {item["cpf_usuario_aluga"]}''')
                                                                                    
                                            confirmar_devolução = input('Deseja confirmar a devolução do livro? s/n: ').strip().lower()
                                            if confirmar_devolução not in ['s', 'n']:
                                                print('Escolha uma das opções.')
                                                continue

                                            if confirmar_devolução == 'n':
                                                print('--Livro não devolvido--')
                                                break
                                            else:
                                                for livro in lista_livros:
                                                    if livro['titulo'] == item['titulo_livro_aluga']:
                                                        livro['quantidade'] += 1

                                                lista_aluguel.remove(item)                                    
                                                print('Devolução concluída')                                                 
                                                break

                                    if not achou_locador:
                                        print('Usuário não encontrado na lista de locação.')
                                        continue

                                case '3': # LISTAR LIVROS ALUGADOS
                                    print('----LISTA DE LIVROS ALUGADOS----')
                                    contador_livros_alugador = 0
                                    for livro in lista_aluguel:
                                        contador_livros_alugador += 1
                                        print(f'''
Livro {contador_livros_alugador}                                               
Titulo: {livro['titulo_livro_aluga']}
Nome do Locatário: {livro['nome_usuario_aluga']}
CPF: {livro['cpf_usuario_aluga']}''')
                
                    case '2': # BUSCAR LIVROS
                        while True:
                            print('----BUSCAR LIVROS----')
                            print(f'''
[1] - Buscar por Nome.
[2] - Buscar por Autor.
[3] - Listar todos.
[4] - Sair.''')
                            opção_buscar = input('Digite uma opção pra busca: ').strip()
                            if opção_buscar not in ['1', '2', '3', '4']:
                                print('Opção inválida, digite uma das opções acima.')
                                continue

                            match opção_buscar:
                                case '4': # SAIR
                                    print('Voltando para o menu.')
                                    break
                               
                                case '1': # BUSCAR POR NOME
                                    print('\n----BUSCAR POR NOME----.')
                                    if not lista_livros:
                                        print('Lista de livros vazia.')
                                        break
                                    
                                    buscar_por_titulo = input('Digite o nome do titulo: ').strip()
                                    achou_titulo = False
                                    for item in lista_livros:                                            
                                        if item['titulo'].lower() == buscar_por_titulo.lower():
                                            print(f'''
LIVRO 
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}''')
                                            achou_titulo = True

                                    if not achou_titulo:
                                        print(f'Titulo: "{buscar_por_titulo}" não encontrado.')

                                case '2': # BUSCAR POR AUTOR
                                    print('\n----BUSCAR POR AUTOR----.')
                                    if not lista_livros:
                                        print('Lista de livros vazia.')
                                        break

                                    buscar_por_autor = input('Digite o nome do autor: ').strip()
                                    achou_autor = False
                                    for item in lista_livros:
                                        if item['autor'].lower() == buscar_por_autor.lower():
                                            print(f'''
LIVRO 
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}''')
                                            achou_autor = True

                                    if not achou_autor:
                                        print(f'Autor: "{buscar_por_autor}" não encontrado.')

                                case '3': # LISTAR TODOS
                                    print('----LISTAR TODOS----')
                                    if not lista_livros:
                                        print('Lista de livros vazia.')
                                        break

                                    for item in lista_livros:
                                        print(f'''
Titulo: {item["titulo"]}
Autor: {item["autor"]}
Quantidade: {item["quantidade"]}
Disponibilidade: {item["disponibilidade"]}''')
