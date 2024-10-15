inicio_intervalo=int(input('Didite um primeiro numero inteiro do intervalo.'))
fim_intervalo=int(input('Digite um segundo numero inteiro deo intervalo.'))

tem_par = False
soma_pares=0

for numero in range (inicio_intervalo,fim_intervalo+1):
    if numero % 2 == 0:
        soma_pares+=numero
        tem_par = True

else:
    if not tem_par:
         print('Não existe numeros pares.')
        
print (f'A soma dos numeros pares no intervalo é: {soma_pares}.')