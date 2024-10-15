# def adc_nova_tarefa():
#     nome = input('Digite seu nome: ')
#     descricao = input('Digite o tipo de tarefa: ')
#     prioridade = input('Digite a prioridade da tarefa "ALTA, MEDIA, BAIXA": ').upper()
#     categoria = input('Digite a categoria da tarefa "PROFISSIONAL, LAZER, OBRIGATORIA": ').upper()
#     status = False  # Status da tarefa inicialmente como não concluída (False)
    
#     # Adicionar a tarefa como um dicionário na lista de tarefas
#     tarefa = {
#         'nome': nome,
#         'descricao': descricao,
#         'prioridade': prioridade,
#         'categoria': categoria,
#         'status': status
#     }

#     lista_de_tarefas.append(tarefa)
#     print('Tarefa adicionada com sucesso!\n')


# # -------------------------------------------------------------------------------------------------------

# lista_de_tarefas = []

# while True:
#     print ('''
#     ----- AGENDA DE TAREFAS -----
        
#         ----- MENU -----
        
#     1 - ADICIONAR NOVA TAREFA.
#     2 - EXIBIR A LISTA DE TAREFAS.
#     3 - MARCAR TAREFA COMO CONCLUIDA.
#     4 - LISTAR TAREFA POR PRIORIDADE.
#     5 - LISTAR TAREFA POR CATEGORIA.
#     6 - SAIR.
#     ''')

#     escolha_menu = input('Digite a opção desejada: ').strip()

#     match escolha_menu:
#         case '1':
#             print('\nADICIONAR NOVA TAREFA')
#             adc_nova_tarefa()


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