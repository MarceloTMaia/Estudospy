# Desenvolva um programa em Python que simule o gerenciamento de uma pequena biblioteca. O programa deve permitir que o usuário adicione livros ao sistema,
# realize empréstimos e liste os livros disponíveis. Para isso, implemente as seguintes funcionalidades:


lista_livro = []  # Lista para armazenar os livros adicionados
lista_emprestado = []  # Lista para armazenar os livros que foram emprestados

while True:
    # Exibe o menu de opções para o usuário
    print(f'''Digite a opção
    01 - adicionar
    02 - emprestimo
    03 - listar
    04 - sair       
    ''')

    escolha = input('Escolha a opção: ')  # Captura a opção do usuário

    match escolha:
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        case '4':
            # Caso o usuário escolha a opção 4, o programa é encerrado
            print('SAIR')
            break  # Sai do loop e encerra o programa
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        case '1':
            # Caso o usuário escolha a opção 1, um novo livro é adicionado à lista
            print('ADICIONAR')

            titulo_livro = input('Digite o título do livro: ')  # Captura o título do livro
            quantidade_livro = int(input('Digite a quantidade: '))  # Captura a quantidade de exemplares disponíveis

            # Verifica se a quantidade de livros é maior que zero para definir a disponibilidade
            if quantidade_livro > 0:
                disponibilidade_livro = 'disponível'
            else:
                disponibilidade_livro = 'indisponível'

            # Cria um dicionário com os detalhes do livro (título, quantidade, disponibilidade)
            livro = {
                'titulo': titulo_livro,
                'quantidade': quantidade_livro,
                'disponibilidade': disponibilidade_livro
            }

            # Adiciona o dicionário do livro à lista de livros
            lista_livro.append(livro)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        case '2':
            # Caso o usuário escolha a opção 2, ele pode realizar o empréstimo de um livro
            print('EMPRÉSTIMO')

            livro_encontrar = input('Digite o nome do livro para alugar: ')  # Captura o título do livro a ser alugado

            # Percorre a lista de livros para encontrar o livro solicitado
            for livro in lista_livro:
                if livro['titulo'] == livro_encontrar:  # Verifica se o título do livro corresponde ao que o usuário digitou
                    # Exibe as informações do livro encontrado
                    print(f'Nome livro: {livro["titulo"]} - Quantidade: {livro["quantidade"]} - Disp: {livro["disponibilidade"]}')

                    alugar = input('Deseja alugar este livro S/N?: ')  # Pergunta se o usuário deseja alugar o livro

                    if alugar.lower() == 's':  # Se o usuário confirmar o aluguel
                        livro['quantidade'] -= 1  # Reduz a quantidade de exemplares do livro em 1
                        if livro['quantidade'] > 0:
                            livro['disponibilidade'] = 'disponível'  # Atualiza a disponibilidade para 'disponível' se ainda houver exemplares
                        else:
                            livro['disponibilidade'] = 'indisponível'  # Atualiza a disponibilidade para 'indisponível' se não houver mais exemplares

                        # Cria um dicionário com as informações do livro alugado
                        livro_alugado = {
                            'nome_livro': livro['titulo'],
                            'quantidade_livro': livro['quantidade'],
                            'disponibilidade_livro': livro['disponibilidade']
                        }
                        
                        # Adiciona o livro alugado à lista de livros emprestados
                        lista_emprestado.append(livro_alugado)

                        # Exibe as informações do livro que foi alugado
                        print(livro_alugado)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
        case '3':
            # Caso o usuário escolha a opção 3, a lista de livros é exibida
            print('LISTAR')

            # Percorre a lista de livros e exibe suas informações
            for item in lista_livro:
                print(f'Título: {item["titulo"]} - Quantidade: {item["quantidade"]} - Disponibilidade: {item["disponibilidade"]}')

                print (f'''
Titulo: {item['titulo']}
Quantidade: {item['quantidade']}
Disponibilidade: {item['disponibilidade']}
''')


                    


