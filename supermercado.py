# FAÇA UM SISTEMA PARA UM MERCADINHO.
# ESSE SISTEMA VAI PERMITIR QUE VOCÊ:
# CADASTRE UM PRODUTO
# VEJA OS PRODUTOS CADASTRADOS
# EDITE UM PRODUTO CADASTRADO
# EXCLUA UM PRODUTO CADASTRADO
# VAI PERMITIR TAMBÉM EFETUAR VENDAS, PARA FAZER UMA VENDA VOCÊ VAI PRECISAR:
# NOME DO CLIENTE
# ITENS COMPRADOS POR ELE
# TOTAL DA VENDA
# GUARDE AS VENDAS DIÁRIAS EM UMA LISTA
# NO FINAL DO EXPEDIENTE FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES DO DIA, O SORTEADO GANHARÁ UM PRÊMIO X.
# MOSTRE TAMBÉM O TOTAL EM REAIS VENDIDO NO DIA, QUAL FOI A COMPRA MAIS CARA E QUAL FOI A COMPRA MAIS BARATA.

lista_produto = [
    {"id": 1, "nome": "Arroz", "quantidade": 2, "preco": 5.50},
    {"id": 2, "nome": "Feijão", "quantidade": 1, "preco": 7.00},
    {"id": 3, "nome": "Macarrão", "quantidade": 3, "preco": 3.20},
    {"id": 4, "nome": "Açúcar", "quantidade": 1, "preco": 4.00},
    {"id": 5, "nome": "Óleo", "quantidade": 1, "preco": 8.50},
    {"id": 6, "nome": "Leite", "quantidade": 6, "preco": 2.00},
    {"id": 7, "nome": "Uva", "quantidade": 5, "preco": 11.50},
]

contador = 8

lista_compras = []
contador_item = 1
valor_total_compras = 0

while True:
  print (f'''\n------------------------------Mercadinho Infinity------------------------------''')

  print (f'''
MENU -------------------         
1 - Cadastrar produto.
2 - Sistema de Vendas.
0 - Sair.''')
  
  menu = input('Digite uma opção: ').strip()

  match menu:
#--------------------------------------------------------------------------------------------------------------------------------------------CASE 1 CADASTRAR
    case '1':
      while True:
        print('\nCADASTRAR ---------')
        print (f'''
1 - Adicionar.
2 - Editar.
3 - Apagar.
4 - Listar.
0 - Sair.         
''')
        cadastrar = input('Digite uma opção: ').strip()
        match cadastrar:

          case '1': #----------------------------------------------------------- CASE 1 ADICIONAR OK

            print ('\nADICIONAR----------')
            produto = input('Nome do produto: ')
            quantidade = int(input('Quantidade: '))
            preco = float(input('Preço: '))

            novo_produto = {
              "id": contador,
              'nome': produto,
              'quantidade': quantidade,
              'preco': preco
            }
            contador += 1

            lista_produto.append(novo_produto)

            print (f'----Produto "{produto}" adicionado.---- ')
          
          case '2': #----------------------------------------------------------- CASE 2 EDITAR OK
            print ('\nEDITAR----------')
            
            menu_editar = print (f'''
1 - Editar Nome.
2 - Editar Quantidade.
3 - Editar Preço. 
0 - Sair.                                      
''')
            editar_opcao = input('Digite uma opções: ')

            match editar_opcao:

              case '1': #--------------------------- CASE 1 EDITAR NOME OK
                print ('\nEDITAR NOME----------')
                print ('\nLISTA DE PRODUTOS')
                for produto in lista_produto:
                  print (f'- {produto["nome"]} | id - {produto["id"]}')

                edit_nome = int(input('\nDigite a ID do produto: '))
                
                for produto_da_vez in lista_produto:
                  if produto_da_vez["id"] == edit_nome:
                    print (f'Produto - {produto_da_vez["nome"]}')
                    novo_nome = input('Digite o novo nome: ')
                    produto_da_vez["nome"] = novo_nome
                    print (f'Nome do produto atualizado - {novo_nome}')

              case '2': #--------------------------- CASE 2 EDITAR QUANTIDADE OK
                print ('EDITAR QUANTIDADE----------')
                print ('\nLISTA DE PRODUTOS')
                for produto in lista_produto:
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Qnt - {produto["quantidade"]}')

                edit_quantidade = int(input('\nDigite a ID do produto: '))
                
                for produto_da_vez in lista_produto:
                  if produto_da_vez["id"] == edit_quantidade:
                    print (f'Produto - {produto_da_vez["nome"]} | {produto_da_vez["quantidade"]}')
                    nova_quantidade = input('Digite a nova quantidade: ')
                    produto_da_vez["quantidade"] = nova_quantidade
                    print (f'quantidade do produto atualizada - {nova_quantidade}')

              case '3': #--------------------------- CASE 3 EDITAR PREÇO OK
                print ('EDITAR PREÇO----------')
                print ('\nLISTA DE PRODUTOS')
                for produto in lista_produto:
                  print (f'- {produto["nome"]} | id - {produto["id"]} | Preço - R$ {produto["preco"]}')

                edit_preco = float(input('\nDigite a ID do produto: '))
                
                for produto_da_vez in lista_produto:
                  if produto_da_vez["id"] == edit_preco:
                    print (f'Produto - {produto_da_vez["nome"]} | R$ {produto_da_vez["preco"]}')
                    novo_preco = input('Digite o novo preço: ')
                    produto_da_vez["preco"] = novo_preco
                    print (f'Preço do produto atualizado - R$ {novo_preco}')
              
              case '0': #--------------------------- CASE 4 SAIR OK
                print ('\nSAIR----------')
                break
                
              case _: #--------------------------- ELSE OK
                      print ('---OPÇÃO INVALIDA---')
                      continue
                      
          case '3': #----------------------------------------------------------- CASE 3 REMOVER OK
            print ('\nREMOVER----------')
            print('LISTA')
            for produto_da_vez in lista_produto:
              
              print(f'''
Nome: {produto_da_vez["nome"]} - {produto_da_vez["id"]}
''')
              encontrar_produto_apagar = int(input("Digite a ID do produto: "))

              for produto_apagar in lista_produto:
                if produto_apagar['id'] == encontrar_produto_apagar:
                  print(f'''
Produto - {produto_apagar["nome"]}
Deseja remover esse produto? S/N: ''')
                  lista_produto.remove(produto_apagar)
                  print ('Produto removido.')
          
          case '4': #----------------------------------------------------------- CASE 4 LISTAR OK
            print ('\nLISTAR----------')
            print('LISTA')
            
            for produto_da_vez in lista_produto:
              print(f'''
ID: {produto_da_vez["id"]} | Qnt: {produto_da_vez["quantidade"]}
{produto_da_vez["nome"]} | Preço: {produto_da_vez["preco"]}''')
          
          case '0': #----------------------------------------------------------- CASE 5 SAIR OK
            print ('\nSAIR----------')
            break
          
          case _: #------------------------------------------------------------- ELSE OK
            print ('---OPÇÃO INVALIDA---')
            continue
#--------------------------------------------------------------------------------------------------------------------------------------------CASE 2 VENDER
    case '2':
      print ('\nSISTEMA DE VENDAS----------')
      while True:
        print (f'''
MENU DE COMPRAS
1 - Carrinho de compras.
2 - Pagar
3 - Remover
0 - Sair.
''')
        menu_de_compras = input('Digite uma opção: ')

        match menu_de_compras:
          case '1': #----------------------------------------------------------- CASE 1 ADICIONAR COMPRAS
            print ('CARRINHO DE COMPRAS----------')
               
            

                                    
            while True:
              entrada_produto = int(input(f'Digite ID ou digite 0 para voltar: '))

              if entrada_produto == 0:
                print ('Voltando')
                break

              for produto_da_vez in lista_produto:
                if produto_da_vez['id'] == entrada_produto:
                  compras = {
                  'id_item': contador_item,
                  'nome_prod': produto_da_vez["nome"],
                  'preco_prod': produto_da_vez["preco"]
                }
                  lista_compras.append(compras)
                  contador_item +=1

                  valor_total_compras += produto_da_vez['preco']
                  for item in lista_compras:
                    print (f'''{item["id_item"]} - {item['nome_prod']} ------------------- R$ {item['preco_prod']}''')
                  print (f'------------------------------------------valor total {valor_total_compras:.2f}')
          
          case '2': #----------------------------------------------------------- CASE 2 PAGAR
            print ('PAGAMENTO----------')
            for item in lista_compras:
              print (f'''{item["id_item"]} - {item['nome_prod']} ------------------- R$ {item['preco_prod']}''')
            print (f'------------------------------------------valor total {valor_total_compras:.2f}')

            forma_de_pagamento = input('Deseja finalizar compra s/n? ')
            if forma_de_pagamento not in ['s','n']:
              print ('Escolha s/n')
              continue
            elif forma_de_pagamento.lower() == 's':
              print (f'''
Forma de pagamento
1 - Dinheiro.
2 - Cartão.  
3 - Pix.
0 - Sair.                                                                               
''')
              escolha_forma_pagamento = input('Digite a forma de pagamento: ')

              match escolha_forma_pagamento:
                case '1': #--------- CASE 1 PAGAMENTO EM DINHEIRO
                  print ('\nPAGAMENTO EM DINHEIRO')

                  for item in lista_compras:
                    print (f'''{item["id_item"]} - {item['nome_prod']} ------------------- R$ {item['preco_prod']}''')
                  print (f'Valor total a pagar -----------------------------------R$ {valor_total_compras:.2f}')
                  valor_cliente = float(input('Digite o valor recebido: '))
                  troco = valor_cliente - valor_total_compras
                  print ('\n---COMPRA FINALIZADA---')
                  print (f'Valor da compra: R$ {valor_total_compras:.2f}')
                  print (f'Valor cliente: R$ {valor_cliente:.2f}')
                  print (f'Troco do cliente: R$ {troco:.2f}')
                
                  break

                case '2': #--------- CASE 2 PAGAMENTO EM CARTÃO
                  print ('PAGAMENTO EM CARTÃO')
                  
                case '3': #--------- CASE 3 PAGAMENTO EM PIX
                  print ('PAGAMENTO EM PIX')
                  
                case '0': #--------- CASE 4 SAIR
                  print ('\nSAIR----------')
                  break
                case _: #--------- ELSE
                  print ('Digite uma das opções:')

            
            else:
              continue
            


            ...
          case '3': #----------------------------------------------------------- CASE 3 REMOVER
            ...

              



                  






#               if entrada_produto == 0:
                
#                 finalizar_compra = input('Deseja finalizar a compra S/N? ')
#                 match finalizar_compra:
#                   case 's': #--------------------- CASE S FORMAS DE PAGAMENTO nao ta finalizada
#                     print ('\nComo deseja pagar?')
#                     forma_de_pagamento = int(input(f'''
# 1 - Dinheiro.
# 2 - Cartão.
# 3 - PIX.
# 0 - Sair.
# --> '''))
#                     match forma_de_pagamento:
#                       case 1: #------- CASE 1 PAGAMENTO EM DINHEIRO
#                         print ('PAGAMENTO EM DINHEIRO')
#                         for item in lista_compras:
#                           print (f'Item:{item["n_item"]} | {item["nome_prod"]} | ------------------------ Valor {item["preco_prod"]}')
#                         print (f'Valor a pagar -------------------------------------------------------------------------R$ {valor_total:.2f}')
#                         print('\nCOMPRA FINALIZADA')
#                         break
#                       case 2: #------- CASE 2 PAGAMENTO EM CARTÃO
#                         print ('PAGAMENTO EM CARTÃO')
#                         for item in lista_compras:
#                           print (f'Item:{item["n_item"]} | {item["nome_prod"]} | ------------------------ Valor {item["preco_prod"]}')
#                         print (f'Valor a pagar -------------------------------------------------------------------------R$ {valor_total:.2f}')
#                       case 3: #------- CASE 3 PAGAMENTO EM PIX
#                         print ('PAGAMENTO EM PIX')
#                         for item in lista_compras:
#                           print (f'Item:{item["n_item"]} | {item["nome_prod"]} | ------------------------ Valor {item["preco_prod"]}')
#                         print (f'Valor a pagar -------------------------------------------------------------------------R$ {valor_total:.2f}')
#                       case 0: #------- CASE 4 SAIR
#                         print ('\nSAIR----------')
#                         break
#                       case _: #------- ELSE
#                         print ('Digite uma das opções:')
#                   case 'n': #--------------------- CASE N CONTINUAR ADICIONANDO OK
#                     continue
#                   case _: #--------------------- ELSE
#                     print ('Digite uma das opções.')
#                     break

#               elif entrada_produto == -1:
#                 item_remover = int(input('Digite o id do item para remover'))
#                 for item in lista_compras:
#                   if item['n_item']==item_remover: 
#                     lista_compras.remove(item)
#                     continue  
                

#               else:
#                 for produto_da_vez in lista_produto:
#                   if produto_da_vez["id"] == entrada_produto:

#                     compras = {
#                   'n_item': contador_item,
#                   'nome_prod': produto_da_vez["nome"],
#                   'preco_prod': produto_da_vez["preco"]
#                 }

#                     contador_item +=1

#                     lista_compras.append(compras)

#                     valor_total += produto_da_vez['preco']
                
#                 for item in lista_compras:
#                   print (f'Item:{item["n_item"]} | {item["nome_prod"]} | ------------------------ Valor {item["preco_prod"]}')
#                 print (f'Valor total -------------------------------------------------------------------------R$ {valor_total:.2f}')
          
          case '0': #----------------------------------------------------------- CASE 0 SAIR
            print ('\nSAIR----------')
            break
          
          case _: #----------------------------------------------------------- ELSE
            print ('---OPÇÃO INVALIDA---')
#--------------------------------------------------------------------------------------------------------------------------------------------CASE 0 SAIR    
    case '0':
      print ('\nSAIR----------')
      break
#--------------------------------------------------------------------------------------------------------------------------------------------ELSE    
    case _:
      print ('---OPÇÃO INVALIDA---')
      continue

  

