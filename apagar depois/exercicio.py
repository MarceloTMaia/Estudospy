def cont_vogais (palavra:str):
    contador_vogais = 0
    vogais = ['a','e','i','o','u']
    
    for item in palavra:
        if item.lower() in vogais:
           contador_vogais +=1

    return contador_vogais
        
print (cont_vogais('aaaa'))

def cont_consoantes(palavra:str):
    contador_consoantes = 0
    consoantes = 'bcdfghjklmnpqrstwxyz'

    for item in palavra:
        if item.lower() in consoantes:
            contador_consoantes +=1

    return contador_consoantes

print (cont_consoantes('mmmmmmmm'))


def cont_palavras(frase: str) -> int:
    palavras = frase.split()
    return len(palavras)


print(cont_palavras("oi seja vem vindo")) 


def par_impar (n1:int):
    if n1 % 2 == 0:
        return f' Numero {n1} é par.'
    
    else:
        return f' Numero {n1} é impar'

print (par_impar(11))

def positivo_negativo (n1:int):
    if n1 > 0:
        return f'{n1} - positivo.'
    elif n1 == 0:
        return f'{n1} - neutro.'
    else:
        return f'{n1} - negativo.'
    
print (positivo_negativo(-1))


def maior_num (numeros:list):
    
    return max(numeros)

print (maior_num([1,2,10,4,5,6,7,8]))



def menor_num(numeros:list):

    return min(numeros)
