# Inicializa um dicionário vazio para contar as palavras
contagem_palavras = {}

# Solicita ao usuário para inserir palavras separadas por espaço
entrada = input("Digite uma lista de palavras separadas por espaço: ")

# Divide a entrada em uma lista de palavras
palavras = entrada.split()

# Conta a ocorrência de cada palavra
for palavra in palavras:
    # Se a palavra já estiver no dicionário, incrementa o contador
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        # Caso contrário, inicializa o contador para essa palavra
        contagem_palavras[palavra] = 1

# Exibe a contagem de ocorrências de cada palavra
print("\nContagem de palavras:")
for palavra, contagem in contagem_palavras.items():
    print(f"{palavra}: {contagem} vez(es)")





