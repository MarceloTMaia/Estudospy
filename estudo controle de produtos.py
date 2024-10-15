
lista_de_produto = []

print ('--------------------------CONTROLE DE PRODUTOS----------------------------')

while True:
    
    print(f'''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          
-----------------------------MENU PRINCIPAL-------------------------------
        
* 1 - ADICIONAR PRODUTO (|NOME|QUANTIDADE|DISPONIBILIDADE|CLASSIFICAÇÃO|CATEGORIA|)
* 2 - LISTAR ESTOQUE
* 3 - VERIFICAR DISPONIBILIDADE
* 4 - LISTAR CLASSIFICAÇÃO NUTRICIONAL (PROTEINA | CARBOIDRATO | VITAMINA)
* 5 - LISTAR CATEGORIA (FRUTA | CARNES | LATICINIOS | OUTROS) 
* 6 - SAIR 
--------------------------------------------------------------------------''')
    escolha_menu = input('Digite uma opção do menu acima: ').strip()
    if escolha_menu not in ['1','2','3','4','5','6']:
        print ('ERRO ERRO ERRO ERRO ERRO ERRO ERRO ERRO - Escolha uma opção do MENU')
        continue
        
           
    print ('--------------------------------------------------------------------------')

    match escolha_menu:
        case '6':
            print ('Saindo do programa')
            break
#-----------------------------------------------------------------------------------------------------------------------------------------------------------        
        case '1':
            print ('-----------SUB-MENU-----------')
            
            while True:
                print (f'''
Adicionar Produto MENU
1 - Para adicionar.
2 - Para remover.
3 - Para editar nome.
4 - Para editar Classificação.
5 - Para editar categoria.
6 - Para editar quantidade.
7 - Para sair.
''')
                escolha_sub_menu = input('Escolha a opção: ').strip()
                if escolha_sub_menu not in ['1','2','3','4','5','6','7']:
                    print ('ERRO ERRO ERRO ERRO ERRO ERRO ERRO ERRO - Escolha uma opção do SUB - MENU')
                    continue
                    

                match escolha_sub_menu:
                                        
                    case '7':
                        print ('<---- Voltando para o MENU principal')
                        break

                    case '1':
                        print ('\nADICIONAR UM PRODUTO')
                        nome_produto = input('Digite o nome do produto ou digite "7" para sair: ').strip()

                        if nome_produto == '7':
                            print('Saindo')
                            break
                        
                        
                        
                        while True:
                            quantidade_produto = input('Digite a quantidade: ').strip()

                            if not quantidade_produto.isdigit():
                                print ('\nDigite um numero valido')
                                continue
                                
                            quantidade_produto = int(quantidade_produto)
                            break

                        
                        
                        
                        disponibilidade_produto = False
                        
                        if quantidade_produto > 0:
                            disponibilidade_produto = True

                        if not disponibilidade_produto:
                            disponibilidade_produto = 'Indisponivel'
                        else:
                            disponibilidade_produto = 'disponivel'
                            
                                                    


                        
                        
                        while True:
                            classificação_produto = input('\nDigite a classificação do produto - | P - PROTEINA | C - CARBOIDRATO | V - VITAMINA |: ').strip()

                            if classificação_produto.lower() in ['p','c','v']:
                                
                                                       
                                if classificação_produto == 'p':
                                    classificação_produto = 'Proteina'

                                elif classificação_produto == 'c':
                                    classificação_produto = 'Carboidrato'
                                
                                else:
                                    classificação_produto = 'Vitamina'
                                break

                            else:
                                print('\nERRO ERRO ERRO ------- Digite uma opção valida - | P | C | V |.')
                                continue

                            
                        
                        
                        while True:
                            categoria_produto = input('\nDigite a categoria do produto - | F - FRUTA | C - CARNES | L - LATICINIOS | O - OUTROS |: ').strip()

                            if categoria_produto.lower() in ['f','c','l','o']:
                                
                                if categoria_produto == 'f':
                                    categoria_produto = 'Fruta'

                                elif categoria_produto == 'c':
                                    categoria_produto = 'Carnes'

                                elif categoria_produto == 'l':
                                    categoria_produto = 'Laticinios'

                                else:
                                    categoria_produto = 'Outros'
                                break
                                    

                            else:
                                print ('\nERRO ERRO ERRO ------- Digite uma categoria valida - | FRUTA | CARNES | LATICINIOS | OUTROS |.')
                                continue    



                        produto_cadastrado = {
                            'nome': nome_produto,
                            'quantidade': quantidade_produto,
                            'disponibilidade': disponibilidade_produto,
                            'classificacao': classificação_produto,
                            'categoria': categoria_produto

                        }

                        lista_de_produto.append(produto_cadastrado)
                        print (f'\n-------> Produto - {produto_cadastrado["nome"]} - cadastrado com sucesso <-------')



                    case '2':
                        print ('REMOVER UM PRODUTO')
                        if not lista_de_produto:
                            print('\n--Lista ainda vazia--')
                            break

                        else:
                            print ('\n---PRODUTOS---')

                            for item in lista_de_produto:                                
                                print (f'Nome: {item["nome"]}')

                        while True:

                            produto_apagar = input ('\nDigite o nome do produto para remover ou digite "7" para sair: ').strip()

                            if produto_apagar == '7':
                                print ('Saindo')
                                break
                            
                            for item in lista_de_produto:
                                if item["nome"].lower() == produto_apagar.lower():
                                    lista_de_produto.remove(item)
                                    print(f'Produto "{item["nome"]}" removido com sucesso.')
                                    break
                            
                            else:
                                print('Nome do produto não encontrado.')

                            print ('\n---PRODUTOS---')

                            for item in lista_de_produto:                                
                                print (f'Nome: {item["nome"]}')

                    case '3':

                        print ('EDITAR NOME DO PRODUTO')
                        if not lista_de_produto:
                            print('--Lista ainda vazia--')
                            break

                        print ('\n---PRODUTOS---')
                        for item in lista_de_produto:
                            print (f'Nome - {item["nome"]}')
                        
                        while True:
                            buscar_nome = input('Digite o nome do produto para alterar ou digite "7" para voltar ao menu: ').strip()

                            if buscar_nome == '7':
                                print ('Saindo')
                                break
                            
                            for item in lista_de_produto:
                                if item['nome'] == buscar_nome:
                                    novo_nome = input('Digite o novo nome: ')
                                    item['nome'] = novo_nome
                                    print (f'Nome - "{buscar_nome}" substituido por "{novo_nome}"')
                                    break

                            else:    
                                print ('Digite um nome que esteja na lista')

                    
                    case '4':

                        print ('EDITAR CLASSIFICAÇÃO')
                        if not lista_de_produto:
                            print ('--Lista ainda vazia--')
                            break

                        print ('\n---PRODUTOS---')
                        for item in lista_de_produto:                   
                            print (f'''
Nome: {item["nome"]}
Classificação: {item["classificacao"]} 
''')
                        while True:    
                            buscar_classificacao = input(f'Digite o nome do produto para modificar sua classificação ou digite "7" para voltar ao menu: ').strip()
                            
                            if buscar_classificacao == '7':
                                print ('Saindo')
                                break

                            
                            for item in lista_de_produto:

                                if item['nome'] == buscar_classificacao:

                                    while True:
                                        nova_classificacao = input('Digite a nova classificação | P - PROTEINA | C - CARBOIDRATO | V - VITAMINA |: ').strip().lower()
                                        
                                        
                                        if nova_classificacao in ['p','c','v']:
                                            if nova_classificacao == 'p':
                                                nova_classificacao = 'Proteina'
                                            elif nova_classificacao == 'c':
                                                nova_classificacao = 'Carboidrato'
                                            else:
                                                nova_classificacao = 'Vitamina'

                                            item['classificacao'] = nova_classificacao
                                            print (f'Classificação do produto "{item["nome"]}" foi atualizado para "{nova_classificacao}"')
                                            break
                                        
                                        else:
                                            print ('\nDigite uma classificação valida: ')
                                            
                                    break
                                else:
                                    print('\nDigite um produto valido.')       

        case '2':
            contador = 0
            print ('--LISTAGEM DE PRODUTOS--')
            if not lista_de_produto:
                print ('lista de produtos vazia')
            else:
                for item in lista_de_produto:
                    print (f'''
Produto - {contador+1}
Produto: ---------- {item["nome"]}
Quantidade: ------- {item['quantidade']}
Disponibilidade: -- {item["disponibilidade"]}
Classificação: ---- {item['classificacao']}
Categoria: -------- {item['categoria']}''')
                    contador+=1
                    
          
