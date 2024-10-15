lista_livro = []
lista_emprestado = []


while True:
    print (f'''Digite a opção
    01 - adicionar
    02 - emprestimo
    03 - listar
    04 -sair       
    ''')

    escolha = input('Escolha a opção: ')

    match escolha:
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        case '4':
            print ('SAIR')
            break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        case '1':
            print ('ADICIONAR')

            titulo_livro = input('Digite o titulo do livro: ')
            quantidade_livro = int(input ('Digite a quantidade: '))

            

            if quantidade_livro > 0:
                disponibilidade_livro = 'disponivel'

            else:
                disponibilidade_livro = 'indisponivel'
            
            livro = {
                'titulo': titulo_livro,
                'quantidade': quantidade_livro,
                'disponibilidade': disponibilidade_livro
            }

            
            lista_livro.append(livro)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        case '2':
            print('EMPRESTIMO')

            livro_encontrar = input ('Digite o nome do livro para alugar: ')
            
            for livro in lista_livro:
                if livro['titulo'] == livro_encontrar:
                    print (f'Nome livro: {livro["titulo"]} - Quantidade: {livro["quantidade"]} - Disp: {livro["disponibilidade"]}')

                    alugar = input('Deseja alugar este livro S/N?: ')

                    if alugar.lower() == 's':

                        livro['quantidade'] -= 1
                        if livro['quantidade'] > 0:
                            livro['disponibilidade'] = 'disponivel'
                        else:
                            livro['disponibilidade'] = 'indisponivel'


                        livro_alugado = {
                'nome_livro': livro['titulo'],
                'quantidade_livro': livro['quantidade'],
                'disponibilidade_livro': livro['disponibilidade']
                }
                    lista_emprestado.append(livro_alugado)

                    

                    print (livro_alugado)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
        case '3':
            print ('LISTAR')

            for item in lista_livro:
                print (f'''
Titulo: {item['titulo']}
Quantidade: {item['quantidade']}
Disponibilidade: {item['disponibilidade']}
''')


                    


