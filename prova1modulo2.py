list_frutas = []

max_frutas = 6

for fruta in range (max_frutas): 

    fruta_dig = str(input('Digite o nome de seis frutas ou digite "sair" para encerrar o programa: '))

    list_frutas.append(fruta_dig)

list_final = tuple(list_frutas)

print('Relação de fruta:')
print(list_final)

   