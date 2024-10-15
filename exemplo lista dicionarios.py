lista_alunos = []  # Inicializa uma lista vazia para armazenar os dicionários de alunos

# Vamos permitir a entrada de 3 alunos (pode ser ajustado conforme necessário)
for i in range(3):
    nome = input("Digite o nome do aluno: ")  # Entrada do nome
    serie = input("Digite a série do aluno: ")  # Entrada da série

    # Solicita as notas em diferentes matérias
    nota_matematica = int(input("Digite a nota de matemática: "))
    nota_geografia = int(input("Digite a nota de geografia: "))
    nota_historia = int(input("Digite a nota de história: "))
    
    # Cria um dicionário para o aluno
    aluno = {
        'nome': nome,
        'serie': serie,
        'notas': {
            'matematica': nota_matematica,
            'geografia': nota_geografia,
            'historia': nota_historia
        }
    }

    # Adiciona o dicionário do aluno à lista de alunos
    lista_alunos.append(aluno)

# Exibe todos os alunos cadastrados com suas informações
print("\nAlunos cadastrados:")
for aluno in lista_alunos:
    print(f"Nome: {aluno['nome']}, Série: {aluno['serie']}")
    print(f"Notas - Matemática: {aluno['notas']['matematica']}, Geografia: {aluno['notas']['geografia']}, História: {aluno['notas']['historia']}")
    print("-" * 30)


