def cont_vogais (palavra:str):
    contador_vogais = 0
    vogais = ['a','e','i','o','u']
    
    for item in palavra:
        if item.lower() in vogais:
           contador_vogais +=1

    return contador_vogais
        


def cont_consoantes(palavra:str):
    contador_consoantes = 0
    consoantes = 'bcdfghjklmnpqrstwxyz'

    for item in palavra:
        if item.lower() in consoantes:
            contador_consoantes +=1

    return contador_consoantes

