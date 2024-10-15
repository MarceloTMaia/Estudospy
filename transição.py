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

while True:
    print('Mercadinho')
    print('''
MENU -------------------
1 - Cadastrar produto.
2 - Sistema de Vendas.
0 - Sair.''')

    menu = input('Digite uma opção: ').strip()

    match menu:
        # --------------------------------------------------------------------------------------------------------------------------------------------CASE 1 CADASTRAR
        case '1':
            while True:
                print('\nCADASTRAR ---------')
                print('''
1 - Adicionar.
2 - Editar.
3 - Apagar.
4 - Listar.
0 - Sair.
''')
                cadastrar = input('Digite uma opção: ').strip()
                match cadastrar:
                    case '1':  # ----------------------------------------------------------- CASE 1 ADICIONAR OK
                        print('\nADICIONAR----------')
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

                        print(f'----Produto "{produto}" adicionado.---- ')

                    case '2':  # ----------------------------------------------------------- CASE 2 EDITAR OK
                        print('\nEDITAR----------')

                        print('''
1 - Editar Nome.
2 - Editar Quantidade.
3 - Editar Preço.
0 - Sair.
''')
                        editar_opcao = input('Digite uma opções: ')

                        match editar_opcao:
                            case '1':  # --------------------------- CASE 1 EDITAR NOME OK
                                print('\nEDITAR NOME----------')
                                print('\nLISTA DE PRODUTOS')
                                for produto in lista_produto:
                                    print(f'- {produto["nome"]} | id - {produto["id"]}')

                                edit_nome = int(input('\nDigite a ID do produto: '))

                                for produto_da_vez in lista_produto:
                                    if produto_da_vez["id"] == edit_nome:
                                        print(f'Produto - {produto_da_vez["nome"]}')
                                        novo_nome = input('Digite o novo nome: ')
                                        produto_da_vez["nome"] = novo_nome
                                        print(f'Nome do produto atualizado - {novo_nome}')

                            case '2':  # --------------------------- CASE 2 EDITAR QUANTIDADE OK
                                print('EDITAR QUANTIDADE----------')
                                print('\nLISTA DE PRODUTOS')
                                for produto in lista_produto:
                                    print(f'- {produto["nome"]} | id - {produto["id"]} | Qnt - {produto["quantidade"]}')

                                edit_quantidade = int(input('\nDigite a ID do produto: '))

                                for produto_da_vez in lista_produto:
                                    if produto_da_vez["id"] == edit_quantidade:
                                        print(f'Produto - {produto_da_vez["nome"]} | {produto_da_vez["quantidade"]}')
                                        nova_quantidade = int(input('Digite a nova quantidade: '))
                                        produto_da_vez["quantidade"] = nova_quantidade
                                        print(f'quantidade do produto atualizada - {nova_quantidade}')

                            case '3':  # --------------------------- CASE 3 EDITAR PREÇO OK
                                print('EDITAR PREÇO----------')
                                print('\nLISTA DE PRODUTOS')
                                for produto in lista_produto:
                                    print(f'- {produto["nome"]} | id - {produto["id"]} | Preço - R$ {produto["preco"]}')

                                edit_preco = int(input('\nDigite a ID do produto: '))

                                for produto_da_vez in lista_produto:
                                    if produto_da_vez["id"] == edit_preco:
                                        print(f'Produto - {produto_da_vez["nome"]} | R$ {produto_da_vez["preco"]}')
                                        novo_preco = float(input('Digite o novo preço: '))
                                        produto_da_vez["preco"] = novo_preco
                                        print(f'Preço do produto atualizado - R$ {novo_preco}')

                            case '0':  # --------------------------- CASE 4 SAIR OK
                                print('\nSAIR----------')
                                break

                            case _:  # --------------------------- ELSE OK
                                print('---OPÇÃO INVALIDA---')
                                continue

                    case '3':  # ----------------------------------------------------------- CASE 3 REMOVER OK
                        print('\nREMOVER----------')
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
                                confirmacao = input().lower()
                                if confirmacao == 's':
                                    lista_produto.remove(produto_apagar)
                                    print('Produto removido.')

                    case '4':  # ----------------------------------------------------------- CASE 4 LISTAR OK
                        print('\nLISTAR----------')
                        print('LISTA')

                        for produto_da_vez in lista_produto:
                            print(f'''
ID: {produto_da_vez["id"]} | Qnt: {produto_da_vez["quantidade"]}
{produto_da_vez["nome"]} | Preço: {produto_da_vez["preco"]}''')

                    case '0':  # ----------------------------------------------------------- CASE 5 SAIR OK
                        print('\nSAIR----------')
                        break

                    case _:  # ------------------------------------------------------------- ELSE OK
                        print('---OPÇÃO INVALIDA---')
                        continue

        # --------------------------------------------------------------------------------------------------------------------------------------------CASE 2 VENDER
        case '2':
            print('\nSISTEMA DE VENDAS----------')
            while True:
                print('''
MENU DE COMPRAS
1 - Adicionar.
2 - Retirar.
3 - Sair.
''')
                menu_de_compras = input('Digite uma opção: ')

                match menu_de_compras:
                    case '1':  # ----------------------------------------------------------- CASE 1 ADICIONAR COMPRAS
                        print('ADICIONAR COMPRAS----------')

                        print('''Digite o "ID" para adicionar produto, "0" para retirar um produto , "00" para pagamento.''')

                        valor_total = 0
                        while True:
                            entrada_produto = int(input('Digite ID | 0 - Retirar produto | 00 - Pagamento: '))

                            if entrada_produto == 00:

                                finalizar_compra = input('Deseja finalizar a compra S/N? ').lower()
                                match finalizar_compra:
                                    case 's':  # --------------------- CASE S FORMAS DE PAGAMENTO
                                        print('\nComo deseja pagar?')
                                        forma_de_pagamento = int(input('''1 - Dinheiro.
2 - Cartão.
3 - PIX.
0 - Sair.
--> '''))
                                        match forma_de_pagamento:
                                            case 1:  # ------- CASE 1 PAGAMENTO EM DINHEIRO
                                                print('PAGAMENTO EM DINHEIRO')
                                                for item in lista_compras:
                                                    print(f'Item:{item["n_item"]} | {item["nome_prod"]} | Valor {item["preco_prod"]}')
                                                print(f'Valor a pagar: R$ {valor_total:.2f}')
                                                dinheiro = float(input('Digite o valor pago pelo cliente: R$ '))
                                                print(f'Troco: R$ {dinheiro - valor_total:.2f}')
                                                lista_compras = []
                                                break

                                            case 2:  # ------- CASE 2 PAGAMENTO COM CARTÃO
                                                print('PAGAMENTO NO CARTÃO')
                                                for item in lista_compras:
                                                    print(f'Item:{item["n_item"]} | {item["nome_prod"]} | Valor {item["preco_prod"]}')
                                                print(f'Valor a pagar: R$ {valor_total:.2f}')
                                                print('Pagamento realizado com sucesso no Cartão!')
                                                lista_compras = []
                                                break

                                            case 3:  # ------- CASE 3 PAGAMENTO COM PIX
                                                print('PAGAMENTO COM PIX')
                                                for item in lista_compras:
                                                    print(f'Item:{item["n_item"]} | {item["nome_prod"]} | Valor {item["preco_prod"]}')
                                                print(f'Valor a pagar: R$ {valor_total:.2f}')
                                                print('Pagamento realizado com sucesso no PIX!')
                                                lista_compras = []
                                                break

                                            case 0:
                                                break

                            if entrada_produto == 0:
                                print('RETIRAR PRODUTO----------')
                                remover_produto_id = int(input('Digite o número do item para remover da compra: '))
                                item_remover = None
                                for item in lista_compras:
                                    if item["n_item"] == remover_produto_id:
                                        item_remover = item
                                        lista_compras.remove(item_remover)
                                        valor_total -= item_remover['preco_prod']
                                        break
                                print(f'Produto {item_remover["nome_prod"]} removido.')

                            else:
                                for produto_da_vez in lista_produto:
                                    if produto_da_vez["id"] == entrada_produto:
                                        lista_compras.append({
                                            "n_item": contador_item,
                                            'nome_prod': produto_da_vez["nome"],
                                            'preco_prod': produto_da_vez["preco"]
                                        })
                                        valor_total += produto_da_vez["preco"]
                                        contador_item += 1
                                        break

                        print(f'COMPRA FINALIZADA, Valor total: R$ {valor_total:.2f}')
                        break

                    case '2':  # ----------------------------------------------------------- CASE 2 RETIRAR COMPRAS
                        if not lista_compras:
                            print('Nenhum item na lista para remover.')
                        else:
                            print('RETIRAR COMPRAS----------')
                            print('Itens:')
                            for item in lista_compras:
                                print(f'Item:{item["n_item"]} | {item["nome_prod"]} | Valor {item["preco_prod"]}')

                    case '3':
                        print('SAIR DO SISTEMA DE VENDAS----------')
                        break

        # --------------------------------------------------------------------------------------------------------------------------------------------CASE 0 SAIR OK
        case '0':
            print('SAIR----------')
            break

        case _:
            print('---OPÇÃO INVALIDA---')

