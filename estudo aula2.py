numero_secreto = 6  # Número fixo a ser adivinhado
tentativas_jogador = 0  # Inicializa o contador de tentativas
numero_tentativas = 3  # Define o número máximo de tentativas

print('Bem-vindo ao jogo de adivinhação!')
print('Regras:')
print('Escolha um número aleatório de 1 a 10')
print('Você terá 3 tentativas para adivinhar o número secreto.')

while tentativas_jogador < numero_tentativas:
    tentativa = float(input('Digite um número: '))  # Solicita ao jogador para digitar um número
    tentativas_jogador += 1  # Incrementa o número de tentativas

    if tentativa == numero_secreto:
        print(f'Parabéns! Você acertou o número secreto que é {numero_secreto}.')
        break  # Sai do loop se o jogador acertar
    elif tentativa > numero_secreto:
        print('Número maior que o secreto. Tente novamente.')
    else:
        print('Número menor que o secreto. Tente novamente.')

else:
    # Executado se o loop terminar sem um `break`, ou seja, se as tentativas se esgotarem
    print(f'Suas tentativas acabaram. O número secreto era {numero_secreto}. Tente novamente na próxima vez!')
