def par_impar (n1:int):
    if n1 % 2 == 0:
        return f' Numero {n1} é par.'
    
    else:
        return f' Numero {n1} é impar'



def positivo_negativo (n1:int):
    if n1 > 0:
        return f'{n1} - positivo.'
    elif n1 == 0:
        return f'{n1} - neutro.'
    else:
        return f'{n1} - negativo.'
    



def maior_num (numeros:list):
    
    return max(numeros)





def menor_num(numeros:list):

    return min(numeros)