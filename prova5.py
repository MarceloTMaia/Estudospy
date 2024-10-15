numero_alunos = int(input('Digite o numero de alunos:'))


soma_medias = 0


for aluno in range (numero_alunos): 
    print(f'\nAluno {aluno+1}:')


    nome_aluno = input("Digite o nome do aluno: ")


    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1+nota2+nota3)/3
    

    if media >= 7:
        print (f'\nAluno aprovado Parabéns.')
    elif media <7:
        print (f'\nAluno Reprovado.')


    print('Dados do Aluno:')
    print(f'Nome: {nome_aluno}')
    print(f'Notas: {nota1}, {nota2}, {nota3}.')
    print(f'Media do Aluno: {media}.')

    soma_medias += media

    
media_geral=soma_medias/numero_alunos
print(f"\nA média geral da turma: {media_geral}")
