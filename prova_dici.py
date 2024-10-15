# Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra. 

lista_produto = {}


for item in range(5):
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: ').strip())
    lista_produto[nome] = preco  


valor_total = 0
for nome in lista_produto:  
    valor_total += lista_produto[nome]  


print("Valor total da compra: R$", valor_total)

   




