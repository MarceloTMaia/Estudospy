# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, 
# exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

contato = {}



contato ['nome'] = input(f'Digite seu nome: ').strip()
contato ['telefone'] = int(input(f'Digite seu telefone: ').strip())
contato ['email'] = input(f'Digite seu email: ').strip()

print (f'''
       
Dados:       
Nome: {contato['nome']}
Telefone: {contato["telefone"]}
Email: {contato["email"]}
       
''')   


    

   




