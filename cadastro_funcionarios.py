# Inicializa um dicionário para armazenar os dados dos funcionários
cadastro_funcionario = {}

# Exibe a mensagem de cabeçalho para o cadastro
print('----- CADASTRO DE FUNCIONARIOS -----')

# Loop principal que continua até que o usuário escolha sair
while True:
    # Exibe o menu de opções
    print(f'''
MENU:
1 - Para cadastrar funcionarios. 
2 - Para exibir cadastro.
3 - Para Apagar funcionario.
4 - Altera nome e salario.
5 - Para sair. 
''')
    
    # Lê a opção escolhida pelo usuário e converte para um inteiro
    opção = int(input('Digite a opção do MENU: '))

    # Verifica se o usuário escolheu sair
    if opção == 5:
        break  # Sai do loop e termina o programa

    # Opção 1: Cadastrar funcionários
    elif opção == 1:
        # Loop para cadastrar múltiplos funcionários
        while True:
            # Solicita o nome do funcionário
            nome = input(f'Digite o nome do funcionario ou "sair": ').strip()  

            # Se o usuário digitar "sair", sai do loop de cadastro
            if nome.lower() == 'sair':
                print('Voltando para o menu. ')
                break
            
            # Solicita o valor do salário
            salario = int(input('Digite o valor do salario: '))

            # Mensagem de sucesso no cadastro
            print(f'''
-----Cadastro realizado com sucesso.-----
Nome: {nome}
Salario: R$ {salario},00 ''')
            
            # Armazena o nome e salário no dicionário
            cadastro_funcionario[nome] = salario

    # Opção 2: Exibir o cadastro de funcionários
    elif opção == 2:
        # Verifica se o dicionário de cadastro está vazio
        if not cadastro_funcionario:
            print(f'''
----- LISTA DE CADASTRO -----
Cadastro esta vazia''')  # Mensagem caso não haja funcionários cadastrados
        else:
            # Exibe a lista de funcionários cadastrados
            print('\n----- LISTA DE CADASTRO -----')
            for nome, salario in cadastro_funcionario.items():
                # Exibe o nome e salário de cada funcionário
                print(f'''
Nome: {nome}
Salario: R$ {salario},00''')

    # Opção 3: Apagar um funcionário
    elif opção == 3:
        print('----- APAGAR FUNCIONARIO-----')

        # Verifica se não há funcionários cadastrados
        if not cadastro_funcionario:
            print('A lista ainda nao possue pessoas cadastradas.')
        else:     
            # Solicita o nome do funcionário a ser excluído
            nome_func_apagar = input('Digite o nome do funcionario para excluir seu cadastro: ')

            # Verifica se o nome existe no cadastro
            if nome_func_apagar not in cadastro_funcionario:
                print('Nome nao encontrado')  # Mensagem de erro se não encontrado
            else:
                # Remove o funcionário do dicionário
                del cadastro_funcionario[nome_func_apagar]
                print(f'Funcionario {nome_func_apagar} apagado com sucesso')

    # Opção 4: Editar nome e salário de funcionários
    elif opção == 4:
        print('\n----- EDITAR DADOS -----')

        # Verifica se não há funcionários cadastrados
        if not cadastro_funcionario:
            print('A lista ainda nao possue pessoas cadastradas.')
        else:
            # Loop para editar dados de funcionários
            while True:
                # Menu para edição
                print(f'''
1 - Para editar nome.
2 - Para editar valores.
3 - Para sair.''')
                
                # Lê a opção de edição escolhida pelo usuário
                opção_editar = int(input('Digite uma opção: '))

                # Opção 3: Sair do loop de edição
                if opção_editar == 3:
                    print('Saindo')
                    break
                
                # Opção 1: Editar nome
                elif opção_editar == 1:
                    print('\n-- EDITAR NOMES --')
                    print('-- LISTA DE FUNCIONARIOS --')
                    
                    # Exibe a lista de funcionários
                    for nome, salario in cadastro_funcionario.items():
                        print(f'''
Nome: {nome}
Salario: R$ {salario},00''')
                    
                    # Loop para editar nomes de funcionários
                    while True:
                        # Solicita o nome a ser alterado
                        edit_nome = input('Digite o nome para alterar ou "1" para sair: ').strip()
                        
                        # Se o usuário digitar "1", sai do loop de edição de nomes
                        if edit_nome == "1":
                            break

                        # Verifica se o nome existe no cadastro
                        elif edit_nome not in cadastro_funcionario:
                            print('Nome inexistente, digite novamente.')  # Mensagem de erro
                        else:
                            # Exibe os dados do funcionário selecionado
                            print(f'''
-- ESCOLHA--
Nome: {edit_nome}
Salario: R$ {cadastro_funcionario[edit_nome]},00''')

                            # Solicita o novo nome
                            novo_nome = input('Digite o novo nome: ').strip()
                            # Atualiza o dicionário com o novo nome
                            cadastro_funcionario[novo_nome] = cadastro_funcionario.pop(edit_nome)

                            # Mensagem de confirmação da modificação
                            print(f'''
-- MODIFICAÇÃO--
Nome: {novo_nome}
Salario: R$ {cadastro_funcionario[novo_nome]},00''')

                # Opção 2: Editar salários
                elif opção_editar == 2:
                    print('-- EDITAR VALORES -- ')
                    print('-- LISTA DE FUNCIONARIOS --')
                    
                    # Exibe a lista de funcionários
                    for nome, salario in cadastro_funcionario.items():
                        print(f'''
Nome: {nome}
Salario: R$ {salario},00''')
                    
                    # Loop para editar salários de funcionários
                    while True:
                        # Solicita o nome do funcionário para editar
                        editar_valor = input('Digite o nome do funcionario para modificar seus valores ou "1" para sair: ').strip()

                        # Se o usuário digitar "1", sai do loop de edição de salários
                        if editar_valor == '1':
                            break
                        # Verifica se o nome existe no cadastro
                        elif editar_valor not in cadastro_funcionario:
                            print('Nome inexistente, digite novamente: ')  # Mensagem de erro
                        else:
                            # Exibe os dados do funcionário selecionado
                            print(f'''
-- ESCOLHA --
Nome: {editar_valor}
Salário atual: R$ {cadastro_funcionario[editar_valor]},00''')

                            # Solicita o novo salário
                            novo_valor = int(input('Digite o novo salário: '))
                            # Atualiza o dicionário com o novo salário
                            cadastro_funcionario[editar_valor] = novo_valor

                            # Mensagem de confirmação da modificação
                            print(f'''
-- MODIFICAÇÃO --
Nome: {editar_valor}
Salario Modificado: R$ {cadastro_funcionario[editar_valor]},00''')








