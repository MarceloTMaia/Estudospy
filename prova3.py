numero_secreto = 6
tentativas_jogador = 0
numero_tentativas = 3

print ('Bem-vindo ao jogo de adivinhação!')
print ('Regras:')
print('Escolha um número aleatório de 1 a 10')
print ('Você terá 3 tentativas para adivinhar o número secreto.')

while tentativas_jogador < numero_tentativas:
    tentativa = float(input('Digite um número: '))
    tentativas_jogador += 1

    if tentativa == numero_secreto:
        print (f'Parabéns!!!!!!!!!!!, você acertou, o número secreto era "{numero_secreto}".')
        break
    elif tentativa > numero_secreto:
        print ('Número maior que o secreto. Tente novamente.')
    else:
        print ('Número menor que o secreto. Tente novamente.')

else:
    print (f'Não foi dessa vez, o número secreto era {numero_secreto}. Tente novamente.')