

lista_produto = []



while True:
    print (f'''
Menu
1 para adicionar
2 listar
3 remover
4 sair       
''')
    escolha_menu = input('Digite a opção para entrar: ')

    match escolha_menu:
        case '4':
            print('saindo')
            break
        case '1': #------------------------------------------------------------------ADICIONAR PRODUTO
            print ('Adicionar produto')

            nome_produto = input('Digite o nome: ')
            quantidade_produto = int(input('Digite a quantidade: '))
            valor_produto = float(input('Digite o valor: '))

            produto = {
                'nome': nome_produto,
                'quantidade': quantidade_produto,
                'valor': valor_produto
            }

            lista_produto.append(produto)

            print (f"Produto {produto['nome']} adicionado com sucesso")

    
        case '2':#------------------------------------------------------------------LISTAR PRODUTO
            print ('LISTA COMPLETA DE PRODUTOS')
            for item in lista_produto:
                print (f'''
Nome - {item['nome']}
Quantidade  - {item['quantidade']}
Valor - {item['valor']}
''') 
        
        case '3':#------------------------------------------------------------------LISTAR PRODUTO
            print ('\nAPAGAR PRODUTO')
            print ('Produtos')
            for item in lista_produto:
                print (f'''
Nome - {item['nome']}
''') 
            produto_apagar = input('Digite o nome do produto para apagar: ')

            for item in lista_produto:
                if item['nome'] == produto_apagar:
                    lista_produto.remove(item)
                    print (f'{produto_apagar} removido com sucesso')
                    break



