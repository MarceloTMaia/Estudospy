agenda_telefone = {}

while True:
    print ('\nAGENDA DE CONTATOS')

    print (f'''
------------------Menu---------------------
           1 - Adicionar contato:
           2 - Remover contato
           3 - Buscar contato
           4 - Ver lista de contato
           5 - Sair
''')
    escolha = int(input(f'Digite a opção: '))

    if escolha == 5:
        print ('Saindo da agenda')
        break

    
    elif escolha == 1:
        while True:

            print ('\nAdicionar telefone ou escreva "sair" para voltar ao menu.')
            nome = str(input(f'Nome: ')).strip()
            
            if nome.lower() == 'sair':
                break
                        
            telefone = str(input('Telefone: ').strip())
            agenda_telefone[nome] = telefone
            print ('Nome adicionado com sucesso.')
            
            

    elif escolha == 2:
        while True:
            
            print ('Remover contato ou escreva "sair" para voltar ao menu.')
            remov_cont = input('Digite o contato para apagar: ').strip()

            if remov_cont.lower() == 'sair':
                break
            
            elif remov_cont.lower() in agenda_telefone:
                 del agenda_telefone[remov_cont]
                 print(f'Contato {remov_cont} removido com sucesso.')

            else:
                print ('Contato inexistente, tente novamente.')

    elif escolha == 3:
        while True:

            print ('Buscar contato')
            buscar_contato = str(input('Digite o nome do contato para buscar ou "sair" para voltar ao menu. ')).strip()

            if buscar_contato == 'sair':
                break
            elif buscar_contato in agenda_telefone:
                print(f'{buscar_contato}: {agenda_telefone[buscar_contato]}')
                       
            else:
                print (f'Contato inexistente, tente novamente. ')
    
    elif escolha == 4:
        print ('----- Lista de telefones -----')
        for nome,telefone in agenda_telefone.items():
            print (f'''      
Nome: {nome}
Telefone: {telefone}''')
            
    else:
        print('Digite uma opção valida')
                 